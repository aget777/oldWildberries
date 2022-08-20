import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
__all__ = ["getPeriodModels"]
urls = Constans.URLs()

def getPeriodModels():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    periodModels = []
    requestUrl = urls.detailUrl

    dateStart = '2022-07-18T21:00:00.000Z'
    dateEnd = '2022-08-08T21:00:00.000Z'
    limit = 10000

    i = 0
    # while True:
    # while i < 1:
    # Подумать над асинхронным запросом
    url = stringBuilder.getPeriodUrl(dateStart=dateStart, dateEnd=dateEnd, limit=limit, requestUrl=requestUrl)
    # print(url)
    response = requests.get(url)



    # Логировать ошибки!
    # if response.status_code != 200:
    #     break


    jsonResults = response.json()
    print(len(jsonResults))
    # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
    # if len(jsonResults) == 0:
    #     break

    periodModels += _mapModels(jsonResults)
    print(f'period: {len(jsonResults)}')

    # i += 1
    return periodModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    periodModels = []

    for jsonResult in jsonResults:
        periodModel = ResponseModels.PeriodModel(jsonResult)
        # print(jsonResult)
        periodModels.append(periodModel)

    return periodModels