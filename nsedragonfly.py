from FOStocks import FOStocks
from Doji import Doji

# Initialize the class
fostock = FOStocks()
Doji= Doji()
lowperct = float(10)
highperct = float(90)

# Construct the input parameters
stockList = fostock.getfostocks()
path = fostock.gettodaypath()
dataframe = fostock.getfopandas(path)

dojiList = Doji.getDoji(stockList, dataframe, lowperct, highperct)
for stockName in dojiList:
    print(stockName)