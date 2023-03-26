from utils import utils


def test_get_date():
    assert utils.get_date({}) == "1953-04-19T12:02:30.129240"
    assert utils.get_date({
        "id": 431131847,
        "state": "EXECUTED",
        "date": "2018-05-05T01:38:56.538074",
        "operationAmount": {
            "amount": "56071.02",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "MasterCard 9454780748494532",
        "to": "Счет 51958934737718181351"
    }) == "2018-05-05T01:38:56.538074"


# def test_load_operations():
#     assert utils.load_operations('list_test.json') == [
#         {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041'},
#         {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


def test_operation_output():
    dict_test = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    dict_test1 = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }

    dict_test2 = {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
    }
    dict_test3 = {
        "id": 596171168,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {
            "amount": "79931.03",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 72082042523231456215"
    }
    dict_test4 = {
        "id": 407169720,
        "state": "EXECUTED",
        "date": "2018-02-03T14:52:08.093722",
        "operationAmount": {
            "amount": "67011.26",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "MasterCard 4047671689373225",
        "to": "Maestro 3806652527413662"
    }
    assert utils.operation_output(
        dict_test) == '26.08.2019 Перевод организации\nMaestro 1596 37** **** 9915 --> Счет **9859\n31957.58 руб.\n'
    assert utils.operation_output(
        dict_test1) == '30.06.2018 Перевод организации\nСчет **2596 --> Счет **2076\n9824.07 USD\n'
    assert utils.operation_output(
        dict_test2) == '19.08.2018 Перевод с карты на карту\nVisa Classic 6831 82** **** 8567 --> Visa Platinum 8990 22** **** 9225\n56883.54 USD\n'
    assert utils.operation_output(dict_test3) == '11.07.2018 Открытие вклада\nСчет **5126\n79931.03 руб.\n'
    assert utils.operation_output(
        dict_test4) == '03.02.2018 Перевод с карты на карту\nMasterCard 4047 71** **** 5223 --> Maestro 3806 52** **** 2663\n67011.26 руб.\n'


def test_print_operations():
    list_test = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 522357576, 'state': 'EXECUTED', 'date': '2019-07-12T20:41:47.882230', 'operationAmount': {'amount': '51463.70', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 48894435694657014368', 'to': 'Счет 38976430693692818358'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}, {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}, {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'}, {'id': 214024827, 'state': 'EXECUTED', 'date': '2018-12-20T16:43:26.929246', 'operationAmount': {'amount': '70946.18', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 10848359769870775355', 'to': 'Счет 21969751544412966366'}, {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}, {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075', 'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}]
    assert utils.text_operations(list_test) == '26.08.2019 Перевод организации\n' \
                                                'Maestro 1596 37** **** 9915 --> Счет **9859\n' \
                                                '31957.58 руб.\n' \
                                                '\n' \
                                                '12.07.2019 Перевод организации\n' \
                                                'Счет **8634 --> Счет **8538\n' \
                                                '51463.70 USD\n' \
                                                '\n' \
                                                '03.07.2019 Перевод организации\n' \
                                                'MasterCard 7158 00** **** 8576 --> Счет **0655\n' \
                                                '8221.37 USD\n' \
                                                '\n' \
                                                '04.04.2019 Перевод со счета на счет\n' \
                                                'Счет **2458 --> Счет **8814\n' \
                                                '79114.93 USD\n' \
                                                '\n' \
                                                '23.03.2019 Перевод со счета на счет\n' \
                                                'Счет **9174 --> Счет **0611\n' \
                                                '43318.34 руб.\n' \
                                                '\n'

