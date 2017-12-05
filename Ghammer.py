from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data,get_closing_data
from datetime import datetime
import sys

# Given a stock name will provide absolute return for three years

param = {
'q': "ICICIBANK", # Stock symbol (ex: "AAPL")
'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
'x': "NSE", # Stock exchange symbol on which stock is traded (ex: "NASD")
'p': "1Y" # Period (Ex: "1Y" = 1 year)
}

# get price data (return pandas dataframe)
#dfr=get_closing_data(param,86400)
#print(dfr)
#Open    High     Low   Close    Volume


stockList=["ACC",
"ADANIPORTS",
"ADANIENT",
"ADANIPOWER",
"APOLLOHOSP",
"AMARAJABAT",
"ALBK",
"AMBUJACEM",
"ANDHRABANK",
"APOLLOTYRE",
"ASHOKLEY",
"AUROPHARMA",
"BAJAJ-AUTO",
"BAJAJFINSV",
"BATAINDIA",
"ASIANPAINT",
"BEML",
"AXISBANK",
"BAJFINANCE",
"BALKRISIND",
"BALRAMCHIN",
"BERGEPAINT",
"BEL",
"BHARATFORG",
"BHARTIARTL",
"BANKINDIA",
"BHEL",
"BHARATFIN",
"BOSCHLTD",
"BPCL",
"CANFINHOME",
"CAPF",
"CEATLTD",
"CESC",
"CGPOWER",
"CHENNPETRO",
"COALINDIA",
"CONCOR",
"CUMMINSIND",
"BIOCON",
"CADILAHC",
"DHFL",
"CANBK",
"DISHTV",
"DIVISLAB",
"DLF",
"DRREDDY",
"EICHERMOT",
"CASTROLIND",
"ESCORTS",
"EXIDEIND",
"FEDERALBNK",
"FORTIS",
"GLENMARK",
"GODFRYPHLP",
"GODREJIND",
"GRASIM",
"CENTURYTEX",
"HCC",
"HDFC",
"HDFCBANK",
"HDIL",
"CHOLAFIN",
"HEROMOTOCO",
"CIPLA",
"HINDALCO",
"COLPAL",
"HINDPETRO",
"HINDZINC",
"DABUR",
"IBREALEST",
"ICICIPRULI",
"IDEA",
"IDFC",
"IDFCBANK",
"INDUSINDBK",
"INFIBEAM",
"IRB",
"ITC",
"JINDALSTEL",
"ENGINERSIN",
"JUSTDIAL",
"KOTAKBANK",
"KPIT",
"GAIL",
"KTKBANK",
"L&TFH",
"LICHSGFIN",
"LUPIN",
"GMRINFRA",
"M&MFIN",
"GODREJCP",
"MANAPPURAM",
"MARUTI",
"GRANULES",
"MCX",
"EQUITAS",
"MFSL",
"MGL",
"MOTHERSUMI",
"HAVELLS",
"GSFC",
"MRF",
"HEXAWARE",
"HINDUNILVR",
"IBULHSGFIN",
"ICIL",
"INDIGO",
"NATIONALUM",
"INFRATEL",
"JISLJALEQS",
"JSWENERGY",
"NBCC",
"NCC",
"JSWSTEEL",
"NESTLEIND",
"NIITTECH",
"NMDC",
"NTPC",
"OFSS",
"OIL",
"ICICIBANK",
"M&M",
"ONGC",
"ORIENTBANK",
"PAGEIND",
"IGL",
"PCJEWELLER",
"INDIACEM",
"PEL",
"PFC",
"POWERGRID",
"PTC",
"RAYMOND",
"INFY",
"JETAIRWAYS",
"JUBLFOOD",
"RELIANCE",
"RELINFRA",
"MRPL",
"RPOWER",
"SAIL",
"SHREECEM",
"MUTHOOTFIN",
"KSCL",
"SIEMENS",
"SOUTHBANK",
"SREINFRA",
"SRF",
"SRTRANSFIN",
"STAR",
"SUNTV",
"TATACHEM",
"TATAMOTORS",
"TATAMTRDVR",
"TATASTEEL",
"PETRONET",
"TCS",
"TECHM",
"TORNTPHARM",
"PIDILITIND",
"TVSMOTOR",
"UBL",
"UJJIVAN",
"UNIONBANK",
"LT",
"UPL",
"RAMCOCEM",
"VEDL",
"RBLBANK",
"MARICO",
"VOLTAS",
"WIPRO",
"RECLTD",
"RELCAPITAL",
"YESBANK",
"ARVIND",
"BANKBARODA",
"BRITANNIA",
"TV18BRDCST",
"PNB",
"RCOM",
"INDIANB",
"IOC",
"SUNPHARMA",
"MINDTREE",
"TATAGLOBAL",
"TITAN",
"NHPC",
"WOCKPHARMA",
"ULTRACEMCO",
"RNAVAL",
"DALMIABHA",
"DCBBANK",
"MCDOWELL-N",
"REPCOHOME",
"KAJARIACER",
"PVR",
"SBIN",
"TATACOMM",
"VGUARD",
"AJANTPHARM",
"TATAELXSI",
"TATAPOWER",
"TORNTPOWER",
"JPASSOCIAT",
"SYNDIBANK",
"HCLTECH",
"ZEEL",
"SUZLON",
"IDBI",
"IFCI"
]

arglen=len(sys.argv)
#print(arglen)
if arglen == 1 :
        year=input("Get the year: ")
        year=int(year)
        month=input("Get the month: ")
        day=input("Get the Current Day: ")
else:
        today=datetime.now()
        year=today.year
        month=today.month
        day=today.day
        #print(year,month,day)

lowperct=20
lowperct=float(lowperct)
highperct=80
highperct=float(highperct)
if arglen == 1 :
        print("Hammer Start Processing")
errorlist=[]
for stockname in stockList:
        param['q']=stockname
        try:
                df = get_price_data(param)
        except Exception:
                errorlist.append(stockname)
        #print(stockname)
        if arglen == 1 :
                print(".",end='')

        try:
                ## Get the day data 
                cinput=str(year)+'-'+str(month)+'-'+str(day)
                dfa= df.loc[cinput]
                
                if (len(dfa) >0):
                        #print(dfa)
                        openv=dfa.get_value(0,0,'true')
                        high=dfa.get_value(0,1,'true')
                        low=dfa.get_value(0,2,'true')
                        close=dfa.get_value(0,3,'true')
                        difference=high-low
                        if(difference>0):
                                closelowperct=(close-low)/difference*100
                                openlowperct=(openv-low)/difference*100
                                highopenperct=(high-openv)/difference*100
                                highcloseperct=(high-close)/difference*100
                                if(highopenperct<lowperct and highcloseperct<lowperct):
                                        if(closelowperct>highperct and openlowperct>highperct):
                                                print(" ")
                                                print(stockname)
                                                #print(openv,high,low,close,difference,closelowperct,openlowperct,highopenperct,highcloseperct)
        except Exception:
               # print("Error: "+ stockname)
               errorlist.append(stockname)
if arglen == 1 :
        print("Hammer End Processing")
if arglen == 1 :
        print("Error List")
        for stock in errorlist:
                print(stock+",",end='')

        
            
        




