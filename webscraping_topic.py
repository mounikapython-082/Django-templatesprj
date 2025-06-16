'''Webscraping is noting but extracting the data from websites or it transforms the unstructed data into structured data by using 
requests,Beautifulsoup,Pandas
Requests:we can check eithe the website is allowing to access the data (200-success,400,500-error)
Beautifulsoup:we can do scraping of all content data
pandas: we can do the unstructred data inthe form of structred data in the form of spredsheet CSV/Excel file (rows/columns format)'''


'''
import requests
import pandas
import numpy
from bs4 import BeautifulSoup
response=requests.get('https://www.flipkart.com/tyy/4io/~cs-vrw4mislv8/pr?sid=tyy%2C4io&collection-tab-name=Samsung+Galaxy+S24&param=8983&hpid=GANHf4PXZyaGUuZ2l7S-GKp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTQ0LDk5OSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdYMkYzRkVVSDZQS1MiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJTYW1zdW5nIEdhbGF4eSBTMjQgNUciXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19')
#print(response)# wee can see the response 
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)#we can get all data
names=soup.find_all('div',class_='-KzDlHZ')
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
print(name)

'''




'''
import requests
import pandas
import numpy
from bs4 import BeautifulSoup
response=requests.get('https://www.flipkart.com/tyy/4io/~cs-vrw4mislv8/pr?sid=tyy%2C4io&collection-tab-name=Samsung+Galaxy+S24&param=8983&hpid=GANHf4PXZyaGUuZ2l7S-GKp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTQ0LDk5OSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdYMkYzRkVVSDZQS1MiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJTYW1zdW5nIEdhbGF4eSBTMjQgNUciXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19')
print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)#we can get all data
names=soup.find_all('div',Class_='_KzDlHZ')
print(names)
name=[]
for i in names[0:2]:
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
#print(soup)
names=soup.find_all('li',class_='_J+igdf')
print(names)
'''
name=[]
for i in names[0:5]:
    d=i.get_text()
    name.append(d)
print(name)
'''