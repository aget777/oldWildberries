import pandas as pd

def writeStockDataFramesInExcel(stockModels):
    writer = pd.ExcelWriter('./stockFBO.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    stockDataFrame = _getStockDataFrameByDealModels(stockModels)
    # print(stockDataFrame)
    dataSheets = {'stockResult': stockDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер

def _getStockDataFrameByDealModels(stockModels):
    lastChangeDateList = []
    supplierArticleList = []
    techSizeList = []
    barcodeList = []
    quantityList = []
    isSupplyList = []
    isRealizationList = []
    quantityFullList = []
    quantityNotInOrdersList = []
    warehouseList = []
    warehouseNameList = []
    inWayToClientList = []
    inWayFromClientList = []
    nmIdList = []
    subjectList = []
    categoryList = []
    daysOnSiteList = []
    brandList = []
    scCodeList = []
    priceList = []
    discountList = []


    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for stockModel in stockModels:
        lastChangeDateList.append(stockModel.lastChangeDate)
        supplierArticleList.append(stockModel.supplierArticle)
        techSizeList.append(stockModel.techSize)
        barcodeList.append(stockModel.barcode)
        quantityList.append(stockModel.quantity)
        isSupplyList.append(stockModel.isSupply)
        isRealizationList.append(stockModel.isRealization)
        quantityFullList.append(stockModel.quantityFull)
        quantityNotInOrdersList.append(stockModel.quantityNotInOrders)
        warehouseList.append(stockModel.warehouse)
        warehouseNameList.append(stockModel.warehouseName)
        inWayToClientList.append(stockModel.inWayToClient)
        inWayFromClientList.append(stockModel.inWayFromClient)
        nmIdList.append(stockModel.nmId)
        subjectList.append(stockModel.subject)
        categoryList.append(stockModel.category)
        daysOnSiteList.append(stockModel.daysOnSite)
        brandList.append(stockModel.brand)
        scCodeList.append(stockModel.scCode)
        priceList.append(stockModel.price)
        discountList.append(stockModel.discount)


    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({
                'lastChangeDate': lastChangeDateList,
                'supplierArticle': supplierArticleList,
                'techSize': techSizeList,
                'barcode': barcodeList,
                'quantity': quantityList,
                'isSupply': isSupplyList,
                'isRealization': isRealizationList,
                'quantityFull': quantityFullList,
                'quantityNotInOrders': quantityNotInOrdersList,
                'warehouse': warehouseList,
                'warehouseName': warehouseNameList,
                'inWayToClient': inWayToClientList,
                'inWayFromClient': inWayFromClientList,
                'nmId': nmIdList,
                'subject': subjectList,
                'category': categoryList,
                'daysOnSite': daysOnSiteList,
                'brand': brandList,
                'scCode': scCodeList,
                'price': priceList,
                'discount': discountList,

                 })

    return dataFrame


# Подумать, куда вынести отсюда имена как константы
# В принципе, уже сейчас думать над документацией проекта
def writeDataFramesInExcel(dealModels):
    writer = pd.ExcelWriter('./ordersFBO.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    dealDataFrame = _getDataFrameByDealModels(dealModels)
    dataSheets = {'dealResult': dealDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер
def _getDataFrameByDealModels(dealModels):
    dateList = []
    lastChangeDateList = []
    supplierArticleList = []
    techSizeList = []
    barcodeList = []
    totalPriceList = []
    discountPercentList = []
    warehouseNameList = []
    oblastList = []
    incomeIDList = []
    odidList = []
    nmIdList = []
    subjectList = []
    categoryList = []
    brandList = []
    isCancelList = []
    cancelDtList = []
    gNumberList = []
    stickerList = []



    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for dealModel in dealModels:
        dateList.append(dealModel.date)
        lastChangeDateList.append(dealModel.lastChangeDate)
        supplierArticleList.append(dealModel.supplierArticle)
        techSizeList.append(dealModel.techSize)
        barcodeList.append(dealModel.barcode)
        totalPriceList.append(dealModel.totalPrice)
        discountPercentList.append(dealModel.discountPercent)
        warehouseNameList.append(dealModel.warehouseName)
        oblastList.append(dealModel.oblast)
        incomeIDList.append(dealModel.incomeID)
        odidList.append(dealModel.odid)
        nmIdList.append(dealModel.nmId)
        subjectList.append(dealModel.subject)
        categoryList.append(dealModel.category)
        brandList.append(dealModel.brand)
        isCancelList.append(dealModel.isCancel)
        cancelDtList.append(dealModel.cancelDt)
        gNumberList.append(dealModel.gNumber)
        stickerList.append(dealModel.sticker)



    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({
                 'date': dateList,
                 'lastChangeDate': lastChangeDateList,
                 'supplierArticle': supplierArticleList,
                 'techSize': techSizeList,
                 'barcode': barcodeList,
                 'totalPrice': totalPriceList,
                 'discountPercent': discountPercentList,
                 'warehouseName': warehouseNameList,
                 'oblast': oblastList,
                 'incomeID': incomeIDList,
                 'odid': odidList,
                 'nmId': nmIdList,
                 'subject': subjectList,
                 'category': categoryList,
                 'brand': brandList,
                 'isCancel': isCancelList,
                 'cancelDt': cancelDtList,
                 'gNumber': gNumberList,
                 'sticker': stickerList,
                              })
    return dataFrame



def writeSaleDataFramesInExcel(saleModels):
    writer = pd.ExcelWriter('./saleFBO.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    saleDataFrame = _getSaleDataFrameByDealModels(saleModels)
    dataSheets = {'saleResult': saleDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер

def _getSaleDataFrameByDealModels(saleModels):
    dateList = []
    lastChangeDateList = []
    supplierArticleList = []
    techSizeList = []
    barcodeList = []
    totalPriceList = []
    discountPercentList = []
    isSupplyList = []
    isRealizationList = []
    promoCodeDiscountList = []
    warehouseNameList = []
    countryNameList = []
    oblastOkrugNameList = []
    regionNameList = []
    incomeIDList = []
    saleIDList = []
    odidList = []
    sppList = []
    forPayList = []
    finishedPriceList = []
    priceWithDiscList = []
    nmIdList = []
    subjectList = []
    categoryList = []
    brandList = []
    IsStornoList = []
    gNumberList = []
    stickerList = []




    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for saleModel in saleModels:
        dateList.append(saleModel.date)
        lastChangeDateList.append(saleModel.lastChangeDate)
        supplierArticleList.append(saleModel.supplierArticle)
        techSizeList.append(saleModel.techSize)
        barcodeList.append(saleModel.barcode)
        totalPriceList.append(saleModel.totalPrice)
        discountPercentList.append(saleModel.discountPercent)
        isSupplyList.append(saleModel.isSupply)
        isRealizationList.append(saleModel.isRealization)
        promoCodeDiscountList.append(saleModel.promoCodeDiscount)
        warehouseNameList.append(saleModel.warehouseName)
        countryNameList.append(saleModel.countryName)
        oblastOkrugNameList.append(saleModel.oblastOkrugName)
        regionNameList.append(saleModel.regionName)
        incomeIDList.append(saleModel.incomeID)
        saleIDList.append(saleModel.saleID)
        odidList.append(saleModel.odid)
        sppList.append(saleModel.spp)
        forPayList.append(saleModel.forPay)
        finishedPriceList.append(saleModel.finishedPrice)
        priceWithDiscList.append(saleModel.priceWithDisc)
        nmIdList.append(saleModel.nmId)
        subjectList.append(saleModel.subject)
        categoryList.append(saleModel.category)
        brandList.append(saleModel.brand)
        IsStornoList.append(saleModel.IsStorno)
        gNumberList.append(saleModel.gNumber)
        stickerList.append(saleModel.sticker)




    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({
                'date': dateList,
                'lastChangeDate': lastChangeDateList,
                'supplierArticle': supplierArticleList,
                'techSize': techSizeList,
                'barcode': barcodeList,
                'totalPrice': totalPriceList,
                'discountPercent': discountPercentList,
                'isSupply': isSupplyList,
                'isRealization': isRealizationList,
                'promoCodeDiscount': promoCodeDiscountList,
                'warehouseName': warehouseNameList,
                'countryName': countryNameList,
                'oblastOkrugName': oblastOkrugNameList,
                'regionName': regionNameList,
                'incomeID': incomeIDList,
                'saleID': saleIDList,
                'odid': odidList,
                'spp': sppList,
                'forPay': forPayList,
                'finishedPrice': finishedPriceList,
                'priceWithDisc': priceWithDiscList,
                'nmId': nmIdList,
                'subject': subjectList,
                'category': categoryList,
                'brand': brandList,
                'IsStorno': IsStornoList,
                'gNumber': gNumberList,
                'sticker': stickerList,


                 })

    return dataFrame


def writePeriodDataFramesInExcel(periodModels):
    writer = pd.ExcelWriter('./periodFBO.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    periodDataFrame = _getPeriodDataFrameByDealModels(periodModels)
    # print(periodDataFrame)
    dataSheets = {'periodResult': periodDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер

def _getPeriodDataFrameByDealModels(periodModels):
    realizationreportIdList = []
    suppliercontractCodeList = []
    rrdIdList = []
    giIdList = []
    subjectNameList = []
    nmIdList = []
    brandNameList = []
    saNameList = []
    tsNameList = []
    barcodeList = []
    docTypeNameList = []
    quantityList = []
    retailPriceList = []
    retailAmountList = []
    salePercentList = []
    commissionPercentList = []
    officeNameList = []
    supplierOperNameList = []
    orderDtList = []
    saleDtList = []
    rrDtList = []
    shkIdList = []
    retailPriceWithdiscRubList = []
    deliveryAmountList = []
    returnAmountList = []
    deliveryRubList = []
    giBoxTypeNameList = []
    productDiscountForReportList = []
    supplierPromoList = []
    ridList = []
    ppvzSppPrcList = []
    ppvzKvwPrcBaseList = []
    ppvzKvwPrcList = []
    ppvzSalesCommissionList = []
    ppvzForPayList = []
    ppvzRewardList = []
    ppvzVwList = []
    ppvzVwNdsList = []
    ppvzOfficeIdList = []
    # ppvzOfficeNameList = []
    ppvzSupplierIdList = []
    ppvzSupplierNameList = []
    ppvzInnList = []
    declarationNumberList = []
    stickerIdList = []
    siteCountryList = []
    penaltyList = []
    additionalPaymentList = []
    sridList = []





    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for periodModel in periodModels:
        realizationreportIdList.append(periodModel.realizationreportId)
        suppliercontractCodeList.append(periodModel.suppliercontractCode)
        rrdIdList.append(periodModel.rrdId)
        giIdList.append(periodModel.giId)
        subjectNameList.append(periodModel.subjectName)
        nmIdList.append(periodModel.nmId)
        brandNameList.append(periodModel.brandName)
        saNameList.append(periodModel.saName)
        tsNameList.append(periodModel.tsName)
        barcodeList.append(periodModel.barcode)
        docTypeNameList.append(periodModel.docTypeName)
        quantityList.append(periodModel.quantity)
        retailPriceList.append(periodModel.retailPrice)
        retailAmountList.append(periodModel.retailAmount)
        salePercentList.append(periodModel.salePercent)
        commissionPercentList.append(periodModel.commissionPercent)
        officeNameList.append(periodModel.officeName)
        supplierOperNameList.append(periodModel.supplierOperName)
        orderDtList.append(periodModel.orderDt)
        saleDtList.append(periodModel.saleDt)
        rrDtList.append(periodModel.rrDt)
        shkIdList.append(periodModel.shkId)
        retailPriceWithdiscRubList.append(periodModel.retailPriceWithdiscRub)
        deliveryAmountList.append(periodModel.deliveryAmount)
        returnAmountList.append(periodModel.returnAmount)
        deliveryRubList.append(periodModel.deliveryRub)
        giBoxTypeNameList.append(periodModel.giBoxTypeName)
        productDiscountForReportList.append(periodModel.productDiscountForReport)
        supplierPromoList.append(periodModel.supplierPromo)
        ridList.append(periodModel.rid)
        ppvzSppPrcList.append(periodModel.ppvzSppPrc)
        ppvzKvwPrcBaseList.append(periodModel.ppvzKvwPrcBase)
        ppvzKvwPrcList.append(periodModel.ppvzKvwPrc)
        ppvzSalesCommissionList.append(periodModel.ppvzSalesCommission)
        ppvzForPayList.append(periodModel.ppvzForPay)
        ppvzRewardList.append(periodModel.ppvzReward)
        ppvzVwList.append(periodModel.ppvzVw)
        ppvzVwNdsList.append(periodModel.ppvzVwNds)
        ppvzOfficeIdList.append(periodModel.ppvzOfficeId)
        # ppvzOfficeNameList.append(periodModel.ppvzOfficeName)
        ppvzSupplierIdList.append(periodModel.ppvzSupplierId)
        ppvzSupplierNameList.append(periodModel.ppvzSupplierName)
        ppvzInnList.append(periodModel.ppvzInn)
        declarationNumberList.append(periodModel.declarationNumber)
        stickerIdList.append(periodModel.stickerId)
        siteCountryList.append(periodModel.siteCountry)
        penaltyList.append(periodModel.penalty)
        additionalPaymentList.append(periodModel.additionalPayment)
        sridList.append(periodModel.srid)





    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({
                'realizationreportId': realizationreportIdList,
                'suppliercontractCode': suppliercontractCodeList,
                'rrdId': rrdIdList,
                'giId': giIdList,
                'subjectName': subjectNameList,
                'nmId': nmIdList,
                'brandName': brandNameList,
                'saName': saNameList,
                'tsName': tsNameList,
                'barcode': barcodeList,
                'docTypeName': docTypeNameList,
                'quantity': quantityList,
                'retailPrice': retailPriceList,
                'retailAmount': retailAmountList,
                'salePercent': salePercentList,
                'commissionPercent': commissionPercentList,
                'officeName': officeNameList,
                'supplierOperName': supplierOperNameList,
                'orderDt': orderDtList,
                'saleDt': saleDtList,
                'rrDt': rrDtList,
                'shkId': shkIdList,
                'retailPriceWithdiscRub': retailPriceWithdiscRubList,
                'deliveryAmount': deliveryAmountList,
                'returnAmount': returnAmountList,
                'deliveryRub': deliveryRubList,
                'giBoxTypeName': giBoxTypeNameList,
                'productDiscountForReport': productDiscountForReportList,
                'supplierPromo': supplierPromoList,
                'rid': ridList,
                'ppvzSppPrc': ppvzSppPrcList,
                'ppvzKvwPrcBase': ppvzKvwPrcBaseList,
                'ppvzKvwPrc': ppvzKvwPrcList,
                'ppvzSalesCommission': ppvzSalesCommissionList,
                'ppvzForPay': ppvzForPayList,
                'ppvzReward': ppvzRewardList,
                'ppvzVw': ppvzVwList,
                'ppvzVwNds': ppvzVwNdsList,
                'ppvzOfficeId': ppvzOfficeIdList,
                # 'ppvzOfficeName': ppvzOfficeNameList,
                'ppvzSupplierId': ppvzSupplierIdList,
                'ppvzSupplierName': ppvzSupplierNameList,
                'ppvzInn': ppvzInnList,
                'declarationNumber': declarationNumberList,
                'stickerId': stickerIdList,
                'siteCountry': siteCountryList,
                'penalty': penaltyList,
                'additionalPayment': additionalPaymentList,
                'srid': sridList,



                 })

    return dataFrame




def writeIncomesDataFramesInExcel(incomesModels):
    writer = pd.ExcelWriter('./incomesFBO.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    incomesDataFrame = _getIncomesDataFrameByDealModels(incomesModels)
    dataSheets = {'incomesResult': incomesDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер

def _getIncomesDataFrameByDealModels(incomesModels):
    incomeIdList = []
    numberList = []
    dateList = []
    lastChangeDateList = []
    supplierArticleList = []
    techSizeList = []
    barcodeList = []
    quantityList = []
    totalPriceList = []
    dateCloseList = []
    warehouseNameList = []
    nmIdList = []
    statusList = []



    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for incomesModel in incomesModels:
        incomeIdList.append(incomesModel.incomeId)
        numberList.append(incomesModel.number)
        dateList.append(incomesModel.date)
        lastChangeDateList.append(incomesModel.lastChangeDate)
        supplierArticleList.append(incomesModel.supplierArticle)
        techSizeList.append(incomesModel.techSize)
        barcodeList.append(incomesModel.barcode)
        quantityList.append(incomesModel.quantity)
        totalPriceList.append(incomesModel.totalPrice)
        dateCloseList.append(incomesModel.dateClose)
        warehouseNameList.append(incomesModel.warehouseName)
        nmIdList.append(incomesModel.nmId)
        statusList.append(incomesModel.status)




    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({
                'incomeId': incomeIdList,
                'number': numberList,
                'date': dateList,
                'lastChangeDate': lastChangeDateList,
                'supplierArticle': supplierArticleList,
                'techSize': techSizeList,
                'barcode': barcodeList,
                'quantity': quantityList,
                'totalPrice': totalPriceList,
                'dateClose': dateCloseList,
                'warehouseName': warehouseNameList,
                'nmId': nmIdList,
                'status': statusList,

                 })

    return dataFrame