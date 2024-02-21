# dict1 = {}
# print(dict1, type(dict1))
# dict1 = {'a': 'A', 'b': 'B', 1: '111'}
# print(dict1, type(dict1))

# dict1 = {
#     "jan": "January",
#     "feb": "february",
#     "mar": "March",
#     "apr": "April",
#     "may": "May",
#     "jun": "June",
#     "jul": "July",
#     "aug": "August",
#     "sep": "Septeber",
#     "oct": "October",
#     "nov": "November",
#     "dec": "Decembe",
#     "dec2": "December",
# }
# print(dict1, len(dict1))
# print(dict1["jan"])
# print(dict1['dec2'])
# dict1['dec2'] = 'Test'
# print(dict1['dec2'])
# dict1['dec3'] = 'Test3'
# print(dict1)

# print(dict1.get('test', 'Value not Exist niga'))

# dict2 = {'a': 'A', 'b': 'B', 1: '111'}
# print(dict2[1])

# dict3 = dict(
#     winter=["December", "January", "February"],
#     spring=["March", "April", "May"],
#     summer=["June", "July", "August"],
#     autumn=["Septebber", "October", "November"],
# )
# print(dict3["winter"][2])

dict_months = {
    "winter": {
        "dec": "Decembe",
        "jan": "January",
        "feb": "february",
    },
    "spring": {
        "mar": "March",
        "apr": "April",
        "may": "May",
    },
    "summer": {
        "jun": "June",
        "jul": "July",
        "aug": "August",
    },
    "autumn": {
        "sep": "Septeber",
        "oct": "October",
        "nov": "November",
    }
}
print(dict_months, len(dict_months))
print(dict_months["summer"]["jul"])
