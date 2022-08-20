
class StockModel:
    def __init__(self, json) -> None:
        self.lastChangeDate = json['lastChangeDate']                       # дата и время обновления информации в сервисе
        self.supplierArticle = json['supplierArticle']                     # ваш артикул
        self.techSize = json['techSize']                                   # Размер
        self.barcode = json['barcode']                                     # штрих-код
        self.quantity = json['quantity']                                   # кол-во, доступное для продажи
        self.isSupply = json['isSupply']                                   # договор поставки
        self.isRealization = json['isRealization']                          # договор реализации
        self.quantityFull = json['quantityFull']                           # Кол-во полное
        self.quantityNotInOrders = json['quantityNotInOrders']             # Кол-во не в заказах
        self.warehouse = json['warehouse']                                 # Склад
        self.warehouseName = json['warehouseName']                         # название склада
        self.inWayToClient = json['inWayToClient']                         # в пути к клиенту (штук)
        self.inWayFromClient = json['inWayFromClient']                     # в пути от клиента (штук)
        self.nmId = json['nmId']                                           # код WB
        self.subject = json['subject']                                     # Товар
        self.category = json['category']                                   # Категория
        self.daysOnSite = json['daysOnSite']                               # кол-во дней на сайте
        self.brand = json['brand']                                         # Бренд
        self.scCode = json['SCCode']                                        # код контракта
        self.price = json['Price']                                         # Цена
        self.discount = json['Discount']                                   # Скидка


# Модель сделок
class DealModel:
    def __init__(self, json) -> None:
        self.date = json['date']                            # дата заказа
        self.lastChangeDate = json['lastChangeDate']        # дата время обновления информации в сервисе
        self.supplierArticle = json['supplierArticle']      # ваш артикул
        self.techSize = json['techSize']                    # размер
        self.barcode = json['barcode']                      # штрих-код
        self.totalPrice = json['totalPrice']                # цена до согласованной скидки/промо/спп
        self.discountPercent = json['discountPercent']      # согласованный итоговый дисконт
        self.warehouseName = json['warehouseName']          # Склад отгрузки
        self.oblast = json['oblast']                        # Область
        self.incomeID = json['incomeID']                    # номер поставки
        self.odid = json['odid']                            # уникальный идентификатор позиции заказа
        self.nmId = json['nmId']                            # Код WB
        self.subject = json['subject']                      # Товар
        self.category = json['category']                    # категория
        self.brand = json['brand']                          # Бренд
        self.isCancel = json['isCancel']                    #  признак отмены заказа (FALSE – отмены не было, TRUE – отмена была)
        self.cancelDt = json['cancel_dt']                   # дата отмены заказа
        self.gNumber = json['gNumber']                      # Номер
        self.sticker = json['sticker']                      # Наклейка



class SaleModel:
    def __init__(self, json) -> None:
        self.date = json['date']                                # дата продажи
        self.lastChangeDate = json['lastChangeDate']            # дата время обновления информации в сервисе
        self.supplierArticle = json['supplierArticle']          # ваш артикул
        self.techSize = json['techSize']                        # размер
        self.barcode = json['barcode']                          # штрих-код
        self.totalPrice = json['totalPrice']                    # цена до согласованной скидки/промо/спп
        self.discountPercent = json['discountPercent']          # согласованный итоговый дисконт
        self.isSupply = json['isSupply']                        # договор поставки
        self.isRealization = json['isRealization']              # договор реализации
        self.promoCodeDiscount = json['promoCodeDiscount']      # согласованный промокод
        self.warehouseName = json['warehouseName']              # Склад отгрузки
        self.countryName = json['countryName']                  # страна
        self.oblastOkrugName = json['oblastOkrugName']          # округ
        self.regionName = json['regionName']                    # регион
        self.incomeID = json['incomeID']                        # номер поставки
        self.saleID = json['saleID']                            # уникальный идентификатор продажи/возврата (S... — продажа, R... —возврат, D... — доплата)
        self.odid = json['odid']                                # уникальный идентификатор позиции заказа
        self.spp = json['spp']                                  # согласованная скидка постоянного покупателя (СПП)
        self.forPay = json['forPay']                            # к перечислению поставщику
        self.finishedPrice = json['finishedPrice']              # фактическая цена из заказа (с учетом всех скидок, включая и от ВБ)
        self.priceWithDisc = json['priceWithDisc']              # цена, от которой считается вознаграждение поставщика forpay (с учетом всех согласованных скидок)
        self.nmId = json['nmId']                                # код WB
        self.subject = json['subject']                          # Товар
        self.category = json['category']                        # категория
        self.brand = json['brand']                              # Бренд
        self.IsStorno = json['IsStorno']                        # 1-продажа сторнирована, 0 – не сторнирована
        self.gNumber = json['gNumber']                          # номер
        self.sticker = json['sticker']                          # наклейка


class PeriodModel:
    def __init__(self, json) -> None:
        self.realizationreportId = json['realizationreport_id']                     # Номер отчета
        self.suppliercontractCode = json['suppliercontract_code']                   # Договор
        self.rrdId = json['rrd_id']                                                 # Номер строки
        self.giId = json['gi_id']                                                   # номер поставки
        self.subjectName = json['subject_name']                                     # Предмет
        self.nmId = json['nm_id']                                                   # Артикул
        self.brandName = json['brand_name']                                         # Бренд
        self.saName = json['sa_name']                                               # Артикул поставщика
        self.tsName = json['ts_name']                                               # Размер
        self.barcode = json['barcode']                                              # Баркод
        self.docTypeName = json['doc_type_name']                                    # Тип документа
        self.quantity = json['quantity']                                            # Количество
        self.retailPrice = json['retail_price']                                     # Цена розничная
        self.retailAmount = json['retail_amount']                                   # Сумма продаж(Возвратов)
        self.salePercent = json['sale_percent']                                     # Согласованная скидка
        self.commissionPercent = json['commission_percent']                         # Процент комиссии
        self.officeName = json['office_name']                                       # Склад
        self.supplierOperName = json['supplier_oper_name']                          # Обоснование для оплаты
        self.orderDt = json['order_dt']                                             # Даты заказа
        self.saleDt = json['sale_dt']                                               # Дата продажи
        self.rrDt = json['rr_dt']                                                   # Дата операции
        self.shkId = json['shk_id']                                                 # ШК
        self.retailPriceWithdiscRub = json['retail_price_withdisc_rub']             # Цена розничная с учетом согласованной скидки
        self.deliveryAmount = json['delivery_amount']                               # Кол-во доставок
        self.returnAmount = json['return_amount']                                   # Кол-во возвратов
        self.deliveryRub = json['delivery_rub']                                     # Стоимость логистики
        self.giBoxTypeName = json['gi_box_type_name']                               # Тип коробов
        self.productDiscountForReport = json['product_discount_for_report']         # Согласованный продуктовый дисконт
        self.supplierPromo = json['supplier_promo']                                 # Промокод
        self.rid = json['rid']                                                      # Номер
        self.ppvzSppPrc = json['ppvz_spp_prc']                                      # Скидка постоянного Покупателя (СПП)
        self.ppvzKvwPrcBase = json['ppvz_kvw_prc_base']                             # Размер  кВВ без НДС, % Базовый
        self.ppvzKvwPrc = json['ppvz_kvw_prc']                                      # Итоговый кВВ без НДС, %
        self.ppvzSalesCommission = json['ppvz_sales_commission']                    # Вознаграждение с продаж до вычета услуг поверенного, без НДС
        self.ppvzForPay = json['ppvz_for_pay']                                      # К перечислению Продавцу за реализованный Товар
        self.ppvzReward = json['ppvz_reward']                                       # Возмещение Расходов услуг поверенного
        self.ppvzVw = json['ppvz_vw']                                               # Вознаграждение Вайлдберриз (ВВ), без НДС
        self.ppvzVwNds = json['ppvz_vw_nds']                                        # НДС с Вознаграждения Вайлдберриз
        self.ppvzOfficeId = json['ppvz_office_id']                                  # Номер офиса
        # self.ppvzOfficeName = json['ppvz_office_name']                              # Наименование офиса доставки
        self.ppvzSupplierId = json['ppvz_supplier_id']                              # Номер партнера
        self.ppvzSupplierName = json['ppvz_supplier_name']                          # Партнер
        self.ppvzInn = json['ppvz_inn']                                             # ИНН партнера
        self.declarationNumber = json['declaration_number']                         # Номер таможенной декларации
        self.stickerId = json['sticker_id']                                         # ID стикера
        self.siteCountry = json['site_country']                                     #
        self.penalty = json['penalty']                                              #
        self.additionalPayment = json['additional_payment']                         #
        self.srid = json['srid']                                                    #



class IncomesModel:
    def __init__(self, json) -> None:
        self.incomeId = json['incomeId']                                # номер поставки
        self.number = json['number']                                    # номер УПД
        self.date = json['date']                                        # дата поступления
        self.lastChangeDate = json['lastChangeDate']                    # дата и время обновления информации в сервисе
        self.supplierArticle = json['supplierArticle']                  # ваш артикул
        self.techSize = json['techSize']                                # Размер
        self.barcode = json['barcode']                                  # штрих-код
        self.quantity = json['quantity']                                # кол-во, доступное для продажи
        self.totalPrice = json['totalPrice']                            # цена из УПД
        self.dateClose = json['dateClose']                              # дата принятия (закрытия) у нас
        self.warehouseName = json['warehouseName']                      # название склада
        self.nmId = json['nmId']                                        # код WB
        self.status = json['status']                                    # Текущий статус поставки