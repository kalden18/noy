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
rf=soup.find("span",{"class":"price-section__label"})
vf=str(rf)
bf=vf.replace('<span class="price-section__label">',"")
ff=str(bf)
cf=ff.replace("</span>","")
print("current stock price is of "+str(cf)+"is : " + str(c))
