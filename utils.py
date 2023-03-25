import json  #подключение модуля для работы с объектами типа json


def load_operations(file_operations):
    """Загружает список операций из файла"""
    list_operations = []
    with open(file_operations, 'r', encoding='utf-8') as f:
       raw_json = f.read()
    list_operations = json.loads(raw_json)
    return list_operations  #выводим список операций

