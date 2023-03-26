from utils.utils import load_operations, print_operations
import datetime


file_operations = 'operations.json'
file_operations_test = 'tests/list_test.json'

#print_operations(load_operations(file_operations))
print(load_operations(file_operations_test))

# dict_ = load_operations(file_operations)[1]
# print(dict_['date'])
# date = datetime.datetime.strptime(dict_["date"], "%Y-%m-%dT%H:%M:%S.%f")
# date_str = date.strftime('%d.%m.%Y')
# print(type(date_str))
