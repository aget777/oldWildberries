import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
__all__ = ["getStockModels"]
urls = Constans.URLs()

def getStockModels():
    # Параметры. Подумать, как задавать

    stockModels = []

    dateStart = '2022-01-01T21:00:00.000Z'
    requestUrl = urls.stocksUrl

    i = 0
    # while True:
    while i < 1:
        # Подумать над асинхронным запросом

        url = stringBuilder.getStoksUrl(dateStart=dateStart, requestUrl=requestUrl)
        # print(url)
        response = requests.get(url)
        # Логировать ошибки!
        if response.status_code != 200:
            break


        jsonResults = response.json()
        print(len(jsonResults) )
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        stockModels += _mapModels(jsonResults)
        print(f'stock: {len(jsonResults)}')
        i += 1
    return stockModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    stockModels = []
    for jsonResult in jsonResults:
        stockModel = ResponseModels.StockModel(jsonResult)
        # print(stockModel)
        stockModels.append(stockModel)
    # print(stockModels)
    return stockModels