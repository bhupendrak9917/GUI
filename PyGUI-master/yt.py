from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

chromepath=r"chromedriver.exe"
driver= webdriver.Chrome(chromepath)

Names=[]
urls=[]
driver.get('https://www.youtube.com/feed/trending')



content=driver.page_source
soup = BeautifulSoup(content)
html = soup.prettify('utf-8')
ytData = soup.findAll("a", class_ = "yt-simple-endpoint style-scope ytd-video-renderer")
for x in ytData:
    yt_href = x.get('href')
    yt_name = x.get('title')
    Names.append(yt_name)
    urls.append(yt_href)



a=[]
for i in range(len(urls)):
    compLink = 'https://www.youtube.com'+urls[i]
    a.append(compLink)



df=pd.DataFrame({'Video Title': Names,'URL':a})
