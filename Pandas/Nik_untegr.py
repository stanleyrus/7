import os
from engines.snowflake import Snowflake
from funcs import get_json_from_api, save_list_to_hdfs, retry
from json import dumps


base_url = os.getenv('JK_URL', 'http://wotrp.worldoftanks.eu/settings.json')
realm = os.getenv('JK_ORDEX_SUFFIX', 'eu')
targets = os.getenv('JK_DESTINATION', 'hdfs,snowflake')
hdfs_table = f'src_wot_{realm}.rp_settings'
sn_table_full = 'wot.raw.rp_settings'
sn_warehouse = 'WOT_ETL_WH'
columns = ['period_end_datetime', 'period_number', 'period_start_datetime', 'settings', 'realm_code']

print("Parameters:")
# print parameters
for var in ['base_url', 'realm', 'targets', 'sn_table_full', 'sn_warehouse']:
    print(f"{var} = '" + str(globals().get(f'{var}')) + "'")


@retry(retry_count=3, delay=60)
def main():
    init_json = get_json_from_api(base_url)

    res = []
    for el in init_json['campaigns']:
        res.append({'period_end_datetime': el['period_end_datetime'], 'period_number': el['period_number'], 'period_start_datetime': el['period_start_datetime'], 'settings': dumps(init_json)})

    if 'hdfs' in targets:
        save_list_to_hdfs(data_list = res, hdfs_table = hdfs_table)

    if 'snowflake' in targets:
        print("\n\n-----------------Insert to snowflake-----------------------------")
        # save to snowflake
        sn_database, sn_schema, sn_table = sn_table_full.split('.')
        sn = Snowflake(sn_database=sn_database, sn_schema=sn_schema, sn_warehouse=sn_warehouse)
        sql = f"delete from {sn_table_full} where realm_code = '{realm.upper()}'"
        sn.exec(sql)
        print(f'Insert data to {sn_table_full}:')
        data_list2 = [tuple(i.values()) + (realm.upper(),) for i in res]
        sn.cur.executemany(
            f"insert into {sn_table_full} ({','.join(columns)}) select $1, $2, $3, parse_json($4), $5 from values (?, ?, ?, ?, ?)", data_list2)
        print(f"Processed {sn.cur.rowcount} rows")
        sn.close()

# Execute script
main()