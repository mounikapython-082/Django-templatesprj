'''Webscraping is noting but extracting the data from websites or it transforms the unstructed data into structured data by using 
requests,Beautifulsoup,Pandas
Requests:we can check eithe the website is allowing to access the data (200-success,400,500-error)
Beautifulsoup:we can do scraping of all content data
pandas: we can do the unstructred data inthe form of structred data in the form of spredsheet CSV/Excel file (rows/columns format)'''



import requests
import pandas
import numpy
from bs4 import BeautifulSoup
response=requests.get('https://www.flipkart.com/tyy/4io/~cs-vrw4mislv8/pr?sid=tyy%2C4io&collection-tab-name=Samsung+Galaxy+S24&param=8983&hpid=GANHf4PXZyaGUuZ2l7S-GKp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTQ0LDk5OSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdYMkYzRkVVSDZQS1MiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJTYW1zdW5nIEdhbGF4eSBTMjQgNUciXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19')
#print(response)# wee can see the response 
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)#we can get all data


#Finding the product names

names=soup.find_all('div',class_='KzDlHZ')
name=[]
for i in names[0:6]:
    d = i.get_text(strip=True)
    name.append(d)
#print(name)


#finding the prices of the products
prices = soup.find_all('div', class_='Nx9bqj _4b5DiR')
price = []
for i in prices[0:6]:
    d = i.get_text(strip=True)
    price.append(d)
#print(price)


#finding the ratings of the products
ratings = soup.find_all('div', class_='XQDdHH')
rating = []
for i in ratings[0:6]:
    d = i.get_text(strip=True)
    rating.append(float(d))
#print(rating)


#finding the features of the products
features=soup.find_all('li',class_='J+igdf')
feature=[]
for i in features[0:6]:
    d=i.get_text()

    feature.append(d)
#print(feature)

#finding the images of the products
images=soup.find_all('img',class_='DByuf4')
image=[]
for i in images[0:6]:
    d=i['src']

    image.append(d)
#print(image)


#finding the Links of the products
links=soup.find_all('a',class_='CGtC98')
link=[]
for i in links[0:6]:
    d = "https://www.flipkart.com/" + i['href']

    link.append(d)
#print(link)



#print(df)
data = {
    'Names': pandas.Series(name),
    'Prices': pandas.Series(price),
    'Ratings': pandas.Series(rating),
    'Features': pandas.Series(feature),
    'Images': pandas.Series(image),
    'Links': pandas.Series(link)
}
#print(data)
df = pandas.DataFrame(data)
print(df)
df.to_csv("Mobile_data.CSV")
#df.to_excel("Mobile_data.xlsx")
#df.to_json("Mobile_data.json")git