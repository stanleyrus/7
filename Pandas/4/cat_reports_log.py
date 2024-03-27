import os
from engines.snowflake import Snowflake
from funcs import get_json_from_api, save_list_to_hdfs, retry
import datetime

# registered_at__gt={unixtime_start} ? registered_at__lt={unixtime_end}

load_date = os.getenv('JK_LOAD_DATE', (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
dt_end = f"{load_date}, 23:59:59"
formated_end_date = datetime.datetime.strptime(dt_end, "%Y-%m-%d, %H:%M:%S")
unixtime_end = f"{int(datetime.datetime.timestamp(formated_end_date))}"
unixtime_start = f"{int(unixtime_end) - (3600 * 24)}"
pg = 1
base_url = os.getenv('JK_URL',
                     f'https://api-catweb-wows.wargaming.net/api/reports/wows/?fields=id%2Ccluster_name%2Cregistered_at%2Capp_version%2Chw_id%2Cmeta_data&registered_at__gt={unixtime_start}&registered_at__lt={unixtime_end}&page_size=1000&page={pg}')
targets = os.getenv('JK_DESTINATION', 'hdfs,snowflake')
hdfs_table = os.getenv('JK_HDFS_TABLE_FULL', 'wows_raw.cat_reports_log_test')
sn_table_full = os.getenv('JK_SF_TABLE_FULL', 'WOWS.RAW.CAT_REPORTS_LOG_TEST')
sn_warehouse = 'WOWS_ETL_WH'
columns = ['id', 'app_version', 'hw_id', 'registered_at', 'os', 'platform', 'nickname_hash', 'realm']

print("Parameters:")
# print parameters
for var in ['load_date', 'targets', 'hdfs_table', 'sn_table_full', 'sn_warehouse', 'base_url', 'columns']:
    print(f"{var} = '" + str(globals().get(f'{var}')) + "'")


@retry(retry_count=3, delay=60)
def main():
    global load_date, dt_end, formated_end_date, unixtime_end, unixtime_start, pg, base_url
    init_json = get_json_from_api(base_url)

    res = []
    print(len(res))
    while True:
        if init_json['_meta']['length'] != 0:
            for el in init_json['data']:
                custom_event_data = el['meta_data'].get('custom_event_data', None)
                if custom_event_data and type(custom_event_data) == dict:
                    installationId = custom_event_data.get('installationId', None)
                    clientRealm = custom_event_data.get('clientRealm', None)
                else:
                    installationId = None
                    clientRealm = None
                res.append({'id': el['id'],
                            'app_version': el['app_version'],
                            'hw_id': el['hw_id'],
                            'registered_at': el['registered_at'],
                            'os': el['meta_data']['os'],
                            'platform': el['meta_data']['platform'],
                            'nickname_hash': installationId,
                            'realm': clientRealm})
            print(f'Finished cheking of page number {pg}')
            pg += 1
            base_url = f'https://api-catweb-wows.wargaming.net/api/reports/wows/?fields=id%2Ccluster_name%2Cregistered_at%2Capp_version%2Chw_id%2Cmeta_data&registered_at__gt={unixtime_start}&registered_at__lt={unixtime_end}&page_size=1000&page={pg}'
            init_json = get_json_from_api(base_url)
        else:
             break
    print('***' * 30)
    print(f'Length of collection for {load_date} is {len(res)} rows')

    if 'hdfs' in targets:
        print("\n\n-----------------Insert to HDFS-----------------------------")
        save_list_to_hdfs(data_list=res, hdfs_table=hdfs_table, partitions={'dt': f"{load_date}"})

    if 'snowflake' in targets:
        print("\n\n-----------------Insert to snowflake-----------------------------")
        # save to snowflake
        sn_database, sn_schema, sn_table = sn_table_full.split('.')
        sn = Snowflake(sn_database=sn_database, sn_schema=sn_schema, sn_warehouse=sn_warehouse)
        sql = f"delete from {sn_table_full} where dt = '{load_date}'"
        sn.exec(sql)
        print(f'Insert data to {sn_table_full}:')
        data_list2 = [tuple(i.values()) + (load_date,) for i in res]
        sn.cur.executemany(
            f"insert into {sn_table_full} ({','.join(columns) + ',dt'}) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", data_list2)
        print(f"Processed {sn.cur.rowcount} rows")
        sn.close()


# Execute script
main()