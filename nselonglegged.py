from FOStocks import FOStocks
from Doji import Doji

# Initialize the class
fostock = FOStocks()
Doji= Doji()
lowperct = float(40)
highperct = float(40)


# Construct the input parameters
stockList = fostock.getfostocks()
path = fostock.gettodaypath()
dataFrame = fostock.getfopandas(path)

dojiList = Doji.getDoji(stockList, dataFrame, lowperct, highperct, "MIDDLE")

path = fostock.getprevpath()
prevDataFrame = fostock.getfopandas(path)
perctincr = int(5)
highValue = "CLOSE_PRICE"
lowValue = "OPEN_PRICE"
for stockName in dojiList:
    check = Doji.getCondition(stockName, prevDataFrame, highValue, lowValue, perctincr)
    if check:
        print(stockName)
