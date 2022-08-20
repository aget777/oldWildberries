class URLs:
    def __init__(self) -> None:
        self.baseURL = 'https://suppliers-stats.wildberries.ru/'
        self.stocksUrl = 'api/v1/supplier/stocks'
        self.orderUrl = 'api/v1/supplier/orders'
        self.salesUrl = 'api/v1/supplier/sales'
        self.detailUrl = 'api/v1/supplier/reportDetailByPeriod'
        self.incomesUrl = 'api/v1/supplier/incomes'

        self.APIKey = 'MTYyZGQ3NmQtNzMxOS00M2Y3LWIzNTAtMTE2NmZmMDJhN2Ew'


class StockParameters:
    def __init__(self) -> None:
        self.dateStart = 'dateFrom'
        self.APIkey = 'key'

class OrderParameters:
    def __init__(self) -> None:
        self.dateStart = 'dateFrom'
        self.flag = 'flag'
        self.APIkey = 'key'

class PeriodParameters:
    def __init__(self) -> None:
        self.dateStart = 'dateFrom'
        self.APIkey = 'key'
        self.limit = 'limit'
        self.rrdid = 'rrdid'
        self.dateEnd = 'dateto'





# Вынести в конфиги, либо как-то еще избавиться от них
class PathsToFiles:
    def __init__(self) -> None:
        # self.catalogPath = 'E:\Wildberries\API\WildbberiesData'
        self.catalogPath = r'C:\Users\Lenovo\Downloads'
        self.dealPath = 'dealTest'