import json  #подключение модуля для работы с объектами типа json
from operator import itemgetter

def get_date(dictionary):
    return dictionary['date']

def load_operations(file_operations):
    """Загружает список операций из файла"""
    #list_operations = []
    with open(file_operations, 'r', encoding='utf-8') as f:
       raw_json = f.read()
    list_operations = json.loads(raw_json)
    #sorted(list_operations, key=get_date)
    #sorted_list_operations = sorted(list_operations, key=itemgetter('date'))
    return list_operations  #выводим список операций

def operation_output(dict: dict):
   if 'from' in dict.keys():
     from_dict = dict['from'].split()
     from_dict_str = from_dict[len(from_dict)-1]
     if len(from_dict_str) == 20:
         str_from = from_dict[0] + ' **' + from_dict_str[len(from_dict_str)-1:len(from_dict_str)-5:-1]
     elif len(from_dict) > 2:
         str_from = from_dict[0] + ' ' + from_dict[1] + ' ' + from_dict_str[0:4] + ' ' + from_dict_str[5:7] + '** **** '+from_dict_str[len(from_dict_str) - 1:len(from_dict_str) - 5:-1]
     else:
         str_from = from_dict[0] + ' ' + from_dict_str[0:4] + ' ' + from_dict_str[5:7] + '** **** ' + from_dict_str[len(from_dict_str) - 1:len(from_dict_str) - 5:-1]
   else:
       str_from = ''

   to_dict = dict['to'].split()
   to_dict_str = to_dict[len(to_dict) - 1]
   if len(to_dict_str) == 20:
       str_to = to_dict[0] + ' **' + to_dict_str[len(to_dict_str)-1:len(to_dict_str)-5:-1]
   elif len(to_dict) > 2:
       str_to = to_dict[0] + ' ' + to_dict[1] + ' ' + to_dict_str[0:4] + ' ' + to_dict_str[5:7] + '** **** ' + to_dict_str[len(to_dict_str) - 1:len(to_dict_str) - 5:-1]
   else:
       str_to = to_dict[0] + ' ' + to_dict_str[0:4] + ' ' + to_dict_str[5:7] + '** **** ' + to_dict_str[len(to_dict_str) - 1:len(to_dict_str) - 5:-1]

   s = dict['date'] + ' ' + dict['description'] + '\n'
   s = s + str_from + '->' + str_to + '\n'
   s = s + dict['operationAmount']['amount'] + ' ' + dict['operationAmount']['currency']['name'] + '\n'
   return s

def print_operations(list_operations):
    i = 0
    for list_item in list_operations:
        print(operation_output(list_item))
        i += 1
        if i == 5:
            break

