import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
__all__ = ["getIncomesModels"]
urls = Constans.URLs()

def getIncomesModels():
    # Параметры. Подумать, как задавать

    incomesModels = []

    dateStart = '2022-07-25T21:00:00.000Z'
    requestUrl = urls.incomesUrl

    i = 0
    # while True:
    # while i < 1:
        # Подумать над асинхронным запросом

    url = stringBuilder.getStoksUrl(dateStart=dateStart, requestUrl=requestUrl)
    # print(url)
    response = requests.get(url)
    # Логировать ошибки!
    # if response.status_code != 200:
    #     break


    jsonResults = response.json()
    print(f'incomes: {len(jsonResults)}')
    # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
    # if len(jsonResults) == 0:
    #     break

    incomesModels += _mapModels(jsonResults)
    print(f'incomes: {len(jsonResults)}')
    # i += 1
    return incomesModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    incomesModels = []
    for jsonResult in jsonResults:
        incomesModel = ResponseModels.IncomesModel(jsonResult)
        incomesModels.append(incomesModel)

    return incomesModels