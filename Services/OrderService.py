import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
__all__ = ["getDealModels"]
urls = Constans.URLs()

def getDealModels():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    dealModels = []

    requestUrl = urls.orderUrl
    dateStart = '2022-04-25T21:00:00.000Z'

    i = 0
    # while True:
    while i < 1:
        # Подумать над асинхронным запросом
        url = stringBuilder.getOrderUrl(dateStart=dateStart, requestUrl=requestUrl)
        response = requests.get(url)


        # Логировать ошибки!
        if response.status_code != 200:
            break


        jsonResults = response.json()
        # print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        dealModels += _mapModels(jsonResults)
        print(f'orders: {len(jsonResults)}')
        i += 1
    return dealModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    dealModels = []
    for jsonResult in jsonResults:
        dealModel = ResponseModels.DealModel(jsonResult)
        dealModels.append(dealModel)

    return dealModels