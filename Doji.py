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
                #print(stockName)
                if difference > 0:
                    closelowperct = (close - low) / difference * 100
                    openlowperct = (openv - low) / difference * 100
                    highopenperct = (high - openv) / difference * 100
                    highcloseperct = (high - close) / difference * 100
                    if debug:
                        print("closelowperct,openlowperct,highopenperct,highcloseperct" + "\n" + str(closelowperct) + "\n" +
                              str(openlowperct) + "\n" +  str(highopenperct)+ "\n" +  str(highcloseperct))
                    if place == "TOP":
                        if highopenperct < lowperct and highcloseperct < lowperct:
                            if closelowperct > highperct and openlowperct > highperct:
                                dojiList.append(stockName)
                    elif place == "BOTTOM":
                        if closelowperct < lowperct and openlowperct < lowperct:
                            if highopenperct > highperct and highcloseperct > highperct:
                                dojiList.append(stockName)
                    elif place == "MIDDLE":
                        if highopenperct > lowperct and highcloseperct > lowperct \
                                and openlowperct > lowperct and closelowperct > lowperct:
                                dojiList.append(stockName)
            except KeyError as e:
               a = 1
        return dojiList

    def getCondition(self, stockName, dataframe, highValue, lowValue, percentage):
        check = False
        try:
            high = dataframe.loc[stockName, highValue]
            low = dataframe.loc[stockName, lowValue]
            openv = dataframe.loc[stockName, 'OPEN_PRICE']
            difference = high - low
            if difference > 0:
                highlowperct = (high - low) / openv * 100
                if highlowperct > percentage:
                    check = True
        except KeyError:
            a = 1
        return check
