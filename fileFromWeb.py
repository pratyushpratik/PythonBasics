from urllib import request
import urllib
import ssl
# import urllib2
from bs4 import BeautifulSoup
url = "https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1507020469&period2=1509698869&interval=1d&events=history&crumb=DKYltA.cT.F"

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(url)

