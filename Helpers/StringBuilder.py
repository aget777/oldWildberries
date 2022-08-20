from Models import Constans

# Разобраться почему не работает сокрытие
# __all__ = ["getOrderUrl"]

urls = Constans.URLs()
orderParameters = Constans.OrderParameters()
stocksParameters = Constans.StockParameters()
periodParameters = Constans.PeriodParameters()


def _addParameter(url, delimiter, name, value) -> str:
    if not value:
        return url

    return url + delimiter + name + '=' + value

def getStoksUrl(dateStart, requestUrl='') -> str:
    url = urls.baseURL + requestUrl

    url = _addParameter(url, '?', stocksParameters.dateStart, str(dateStart))
    url = _addParameter(url, '&', stocksParameters.APIkey, str(urls.APIKey))

    return url


def getOrderUrl(dateStart, flag=0, requestUrl='') -> str:
    url = urls.baseURL + requestUrl

    url = _addParameter(url, '?', orderParameters.dateStart, dateStart)
    url = _addParameter(url, '&', orderParameters.flag, str(flag))
    url = _addParameter(url, '&', orderParameters.APIkey, str(urls.APIKey))

    return url


def getPeriodUrl(dateStart, dateEnd, limit=0, rrdid=0, requestUrl='') -> str:
    url = urls.baseURL + requestUrl

    url = _addParameter(url, '?', periodParameters.dateStart, dateStart)
    url = _addParameter(url, '&', periodParameters.APIkey, str(urls.APIKey))
    url = _addParameter(url, '&', periodParameters.limit, str(limit))
    url = _addParameter(url, '&', periodParameters.rrdid, str(rrdid))
    url = _addParameter(url, '&', periodParameters.dateEnd, dateEnd)

    return url

