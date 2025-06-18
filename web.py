'''import requests
import pandas
import numpy
from bs4 import BeautifulSoup
response=requests.get('https://webscraper.io/test-sites')
print(response)
soup=BeautifulSoup(response.content,'html.parser')
print(soup)
names=soup.find_all('p',class_='description card-text')

print(names)

name=[]
for i in names[0:4]:
    d=i.get_text()
    name.append(d)
print(name)

'''


import requests
import pandas
import numpy
from bs4 import BeautifulSoup
response=requests.get('https://www.flipkart.com/tyy/4io/~cs-7j890l5vve/pr?sid=tyy,4io&collection-tab-name=realme+P3x+5G&pageCriteria=default&param=7612&otracker=clp_banner_3_8.bannerX3.BANNER_mobile-phones-store_FWF1F2KPQFG5&fm=neo%2Fmerchandising&iid=M_8836e8cd-3b62-492a-93bf-d68f1d1f6c29_8.FWF1F2KPQFG5&ppt=browse&ppn=browse&ssid=sw4t4rxadc0000001746730901073')
print(response)
soup=BeautifulSoup(response.content,'html.parser')
print(soup)
names=soup.find_all('div',class_='KzDlHZ')
#names=soup.find_all('div','span', True, class_='KzDlHZ')
print("these are my names",names)

name=[]
for i in names[0:4]:
    d=i.get_text()
    print("the value us",d)
    name.append(d)
print(name)
