import json  # подключение модуля для работы с объектами типа json
import datetime  # подключение модуля для работы с датами


def get_date(dictionary):
    """Функция, которая необходима для сортировки списка словарей по значению ключа date"""
    if dictionary == {}:  # проверяем на наличие пустового словаря и выводим рамдомное очень старую дату
        return "1953-04-19T12:02:30.129240"
    else:
        return dictionary['date']


def load_operations(file_operations):
    """Загружает список (словарей) операций из файла json"""
    with open(file_operations, 'r', encoding='utf-8') as f:
        raw_json = f.read()
    list_operations = json.loads(raw_json)
    sorted_list_operations = sorted(list_operations, key=get_date, reverse=True)  # делаем обратную сортировку по дате
    return sorted_list_operations  # выводим список операций


def operation_output(dict_item: dict):
    """Функция возвращает из одного словаря операции строку для вывода, учитывая требования ТЗ"""
    date = datetime.datetime.strptime(dict_item["date"], "%Y-%m-%dT%H:%M:%S.%f")
    date_str = date.strftime('%d.%m.%Y')  # форматируем дату
    if 'from' in dict_item.keys():
        from_dict = dict_item['from'].split()
        from_dict_str = from_dict[len(from_dict) - 1]
        if len(from_dict_str) == 20:  # проверяем если это счёт
            str_from = from_dict[0] + ' **' + from_dict_str[len(from_dict_str) - 1:len(from_dict_str) - 5:-1] + ' --> '
        elif len(from_dict) > 2:  # проверяем если это карта с двумя словами, например visa gold
            str_from = from_dict[0] + ' ' + from_dict[1] + ' ' + from_dict_str[0:4] + ' ' + from_dict_str[
                                                                                            5:7] + '** **** ' + from_dict_str[
                                                                                                                len(from_dict_str) - 1:len(
                                                                                                                    from_dict_str) - 5:-1] + ' --> '
        else:  # иначе это карта с одним словом, например Mastercard
            str_from = from_dict[0] + ' ' + from_dict_str[0:4] + ' ' + from_dict_str[5:7] + '** **** ' + from_dict_str[
                                                                                                         len(from_dict_str) - 1:len(
                                                                                                             from_dict_str) - 5:-1] + ' --> '
    else:
        str_from = ''

    to_dict = dict_item['to'].split()
    to_dict_str = to_dict[len(to_dict) - 1]
    if len(to_dict_str) == 20:
        str_to = to_dict[0] + ' **' + to_dict_str[len(to_dict_str) - 1:len(to_dict_str) - 5:-1]
    elif len(to_dict) > 2:
        str_to = to_dict[0] + ' ' + to_dict[1] + ' ' + to_dict_str[0:4] + ' ' + to_dict_str[
                                                                                5:7] + '** **** ' + to_dict_str[
                                                                                                    len(to_dict_str) - 1:len(
                                                                                                        to_dict_str) - 5:-1]
    else:
        str_to = to_dict[0] + ' ' + to_dict_str[0:4] + ' ' + to_dict_str[5:7] + '** **** ' + to_dict_str[
                                                                                             len(to_dict_str) - 1:len(
                                                                                                 to_dict_str) - 5:-1]
    # формируем итоговую строку по операции из данных словаря
    summary_str = date_str + ' ' + dict_item['description'] + '\n'
    summary_str = summary_str + str_from + str_to + '\n'
    summary_str = summary_str + dict_item['operationAmount']['amount'] + ' ' + dict_item['operationAmount']['currency']['name'] + '\n'
    return summary_str


def text_operations(list_operations):
    """Функция формирует итоговую строку для вывода 5 последних операций"""
    i = 0
    summary_str = ''
    for list_item in list_operations:
        if list_item['state'] != 'CANCELED':
            summary_str = summary_str + operation_output(list_item) + '\n'
            i += 1
            if i == 5:
                break
    return summary_str
