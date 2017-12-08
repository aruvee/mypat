import pandas
from datetime import datetime
from datetime import timedelta
class FOStocks:
    def getfostocks(self):
        stockList=[]
        file = open("data\\fostocks.txt", "r")
        for line in file:
            stockList.append(line.strip())
        return stockList

    def getfopandas(self, path):
        dataframe= pandas.read_csv(path, index_col=1)
        dataframe=dataframe.loc[dataframe['EXP_DATE'] == '28-12-17']
        return dataframe

    def gettodaypath(self):
        prefix = "data\\fo"
        suffix = ".csv"
        today = datetime.now()
        year = today.year
        month = today.month
        if month < 10:
            month = "0" + str(month)
        day = today.day
        if day < 10:
            day = "0" + str(day)
        filepath = prefix + str(day) + str(month) + str(year) + suffix
        return filepath

    def getprevpath(self):
        prefix = "data\\fo"
        suffix = ".csv"
        today = datetime.now() - timedelta(days=1)
        year = today.year
        month = today.month
        if month < 10:
            month = "0" + str(month)
        day = today.day
        if day < 10:
            day = "0" + str(day)
        filepath = prefix + str(day) + str(month) + str(year) + suffix
        return filepath
