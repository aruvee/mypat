import mechanicalsoup
import zipfile
import urllib3

#browser = mechanicalsoup.StatefulBrowser()
#response = browser.open("http://www.bseindia.com/download/BhavCopy/Equity/EQ310118_CSV.ZIP")

#filecon = response.content
#myresponse = urllib3.get_host("http://www.bseindia.com/download/BhavCopy/Equity/EQ310118_CSV.ZIP")

#archive = zipfile.ZipFile(myresponse, 'r')
#imgdata = archive.read('EQ310118.CSV')

#print(imgdata)

import requests
import zipfile
from io import StringIO
r = requests.get("http://www.bseindia.com/download/BhavCopy/Equity/EQ310118_CSV.ZIP", stream=True)
z = zipfile.ZipFile(StringIO(r.content))
z.extractall()