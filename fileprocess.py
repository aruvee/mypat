import zipfile
from FOStocks import FOStocks
from zipfile import ZipFile

fostocks = FOStocks()

bsezip = fostocks.getbsezip()
content = ""
bsenewfile = open(fostocks.getbsenewfile(), "w")
with zipfile.ZipFile(bsezip) as z:
    with z.open(fostocks.getbsefilename()) as f:
        for line in f:
            content = line.decode("ascii").strip()
            content = content.replace(" ", "")
            bsenewfile.write(content)
            #print(content)
            bsenewfile.write("\n")
bsenewfile.close()

nsezip = fostocks.getnsezip()
content = ""
nsenewfile = open(fostocks.getnsenewfile(), "w")
with zipfile.ZipFile(nsezip) as z:
    with z.open(fostocks.getnsefilename()) as f:
        for line in f:
            content = line.decode("ascii").strip()
            content = content.replace(" ", "")
            nsenewfile.write(content)
            #print(content)
            nsenewfile.write("\n")
nsenewfile.close()