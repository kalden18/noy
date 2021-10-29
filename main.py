import requests
from bs4 import BeautifulSoup

symbol=input("stock symbol: ")

URL="https://markets.businessinsider.com/stocks/"+symbol+"-stock"
v=requests.get(URL)

soup=BeautifulSoup(v.text,"html5lib")
r=soup.find("span",{"class":"price-section__current-value"})
v=str(r)
b=v.replace('<span class="price-section__current-value">',"")
f=str(b)
c=f.replace("</span>","")
print("current stock price is:" + str(c))
