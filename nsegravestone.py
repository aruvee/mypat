from FOStocks import FOStocks
from Doji import Doji

# Initialize the class
fostock = FOStocks()
Doji= Doji()
lowperct = float(20)
highperct = float(80)
graveStoneList = []
graveStoneListCo = []

# Construct the input parameters
stockList = fostock.getfostocks()
path = fostock.getprevpath()
prevDataFrame = fostock.getfopandas(path)

dojiList = Doji.getDoji(stockList, prevDataFrame, lowperct, highperct, "BOTTOM")

path = fostock.gettodaypath()
todayDataFrame = fostock.getfopandas(path)
for stockName in dojiList:
    dayOpen = todayDataFrame.loc[stockName, 'OPEN_PRICE']
    dayClose = todayDataFrame.loc[stockName, 'CLOSE_PRICE']
    prevClose = prevDataFrame.loc[stockName, 'CLOSE_PRICE']
    if dayClose < dayOpen:
        if dayOpen < prevClose:
            graveStoneList.append(stockName)
        else:
            graveStoneListCo.append(stockName)


for stockName in graveStoneList:
    print(stockName)

print("Close Only")
for stockName in graveStoneListCo:
    print(stockName)