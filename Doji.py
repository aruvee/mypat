class Doji:

    def getDoji(self, stockList, dataframe, lowperct, highperct, place):
        dojiList=[]
        debug = False
        for stockName in stockList:
            try:
                openv = dataframe.loc[stockName, 'OPEN_PRICE']
                high = dataframe.loc[stockName, 'HI_PRICE']
                low = dataframe.loc[stockName, 'LO_PRICE']
                close = dataframe.loc[stockName, 'CLOSE_PRICE']
                difference = high - low
                if difference > 0:
                    closelowperct = (close - low) / difference * 100
                    openlowperct = (openv - low) / difference * 100
                    highopenperct = (high - openv) / difference * 100
                    highcloseperct = (high - close) / difference * 100
                    if debug:
                        print("closelowperct,openlowperct,highopenperct,highcloseperct" + str(closelowperct) +
                              str(openlowperct) + str(highopenperct)+str(highcloseperct))
                    if place == "TOP":
                        if highopenperct < lowperct and highcloseperct < lowperct:
                            if closelowperct > highperct and openlowperct > highperct:
                                dojiList.append(stockName)
                    elif place == "BOTTOM":
                        if closelowperct < lowperct and openlowperct < lowperct:
                            if highopenperct > highperct and highcloseperct > highperct:
                                dojiList.append(stockName)
            except KeyError:
                a = 1
        return dojiList

    def getPrice(self, stockName, filePath):
        priceDict={}

        return priceDict
