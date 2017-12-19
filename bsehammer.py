from FOStocks import FOStocks
from Doji import  Doji

# Initialize the class
fostock = FOStocks()
Doji= Doji()
lowperct = float(20)
highperct = float(80)
stockList = []

# Construct the input parameters

path = fostock.getbsetodaypath()
dataframe = fostock.getbsepandas(path)

path = fostock.getbseprevpath()
prevdataframe = fostock.getbsepandas(path)

path = fostock.getbsepprevpath()
pprevdataframe = fostock.getbsepandas(path)

for index, row in dataframe.iterrows():
    stockList.append(index)

#print(stockList.__len__())

#change the dataframe names
dataframe = dataframe.rename(columns={'OPEN': 'OPEN_PRICE', 'HIGH': 'HI_PRICE', 'LOW': 'LO_PRICE', 'CLOSE': 'CLOSE_PRICE'})

dojiList = Doji.getDoji(stockList,dataframe, lowperct, highperct, "TOP")
#print(dojiList.__len__())

for stockName in dojiList:
    try:
        open = prevdataframe.loc[stockName,"PREVCLOSE"]
        close = prevdataframe.loc[stockName, "CLOSE"]
        if close < open:
            #print(open,close)
            open = pprevdataframe.loc[stockName, "PREVCLOSE"]
            close = pprevdataframe.loc[stockName, "CLOSE"]
            #print(open, close)
            if close < open:
                print(stockName)
    except KeyError:
        a = 1