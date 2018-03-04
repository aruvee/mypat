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
        dataframe=dataframe.loc[dataframe['EXP_DATE'] == '28/03/2018']
        return dataframe

    def getbsepandas(self, path):
        dataframe= pandas.read_csv(path, index_col=1)
        return dataframe

    def getbsetodaypath(self):
        prefix = "data\\EQ"
        suffix = ".csv"
        today = datetime.now()
        year = today.year - 2000
        month = today.month
        if month < 10:
            month = "0" + str(month)
        day = today.day
        if day < 10:
            day = "0" + str(day)
        filepath = prefix + str(day) + str(month) + str(year) + suffix
        return filepath

    def getbseprevpath(self):
        prefix = "data\\EQ"
        suffix = ".csv"
        today = datetime.now() - timedelta(days=1)
        year = today.year - 2000
        month = today.month
        if month < 10:
            month = "0" + str(month)
        day = today.day
        if day < 10:
            day = "0" + str(day)
        filepath = prefix + str(day) + str(month) + str(year) + suffix
        return filepath

    def getbsepprevpath(self):
        prefix = "data\\EQ"
        suffix = ".csv"
        today = datetime.now() - timedelta(days=2)
        year = today.year - 2000
        month = today.month
        if month < 10:
            month = "0" + str(month)
        day = today.day
        if day < 10:
            day = "0" + str(day)
        filepath = prefix + str(day) + str(month) + str(year) + suffix
        return filepath

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

    def getbsezip(self):
        prefix = "C:\\Users\\veeramani_k\\Downloads\\EQ"
        suffix = "_CSV.ZIP"
        today = datetime.now()
        year = today.year
        year = today.year - 2000
        month = today.month
        if month < 10:
            month = "0" + str(month)
        day = today.day
        if day < 10:
            day = "0" + str(day)
        filepath = prefix + str(day) + str(month) + str(year) + suffix
        return filepath

    def getbsenewfile(self):
        filepath = "data\\" + self.getbsefilename()
        return filepath

    def getbsefilename(self):
        prefix = "EQ"
        suffix = ".CSV"
        today = datetime.now()
        year = today.year
        year = today.year - 2000
        month = today.month
        if month < 10:
            month = "0" + str(month)
        day = today.day
        if day < 10:
            day = "0" + str(day)
        filepath = prefix + str(day) + str(month) + str(year) + suffix
        return filepath

    def getnsezip(self):
        prefix = "C:\\Users\\veeramani_k\\Downloads\\fo"
        suffix = ".ZIP"
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

    def getnsenewfile(self):
        filepath = "data\\" + self.getnsefilename()
        return filepath

    def getnsefilename(self):
        prefix = "fo"
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