from utils import utils


def test_get_date():
    assert utils.get_date({}) == "2017-04-19T12:02:30.129240"
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

