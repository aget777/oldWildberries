from Services import StocksServise, OrderService, SaleService, PeriodService, IncomesService
from Repositories import FileRepository
from Repositories import ExcelRepository

if __name__ == '__main__':

    stockModels = StocksServise.getStockModels()
    dealModels = OrderService.getDealModels()
    saleModels = SaleService.getSaleModels()
    periodModels = PeriodService.getPeriodModels()
    incomesModels = IncomesService.getIncomesModels()




    ExcelRepository.writeStockDataFramesInExcel(stockModels)
    ExcelRepository.writeDataFramesInExcel(dealModels)
    ExcelRepository.writeSaleDataFramesInExcel(saleModels)
    ExcelRepository.writePeriodDataFramesInExcel(periodModels)
    ExcelRepository.writeIncomesDataFramesInExcel(incomesModels)



