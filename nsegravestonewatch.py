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
path = fostock.gettodaypath()
prevDataFrame = fostock.getfopandas(path)

dojiList = Doji.getDoji(stockList, prevDataFrame, lowperct, highperct, "BOTTOM")

print("Gravestone Watch")
for stockName in dojiList:
    print(stockName)