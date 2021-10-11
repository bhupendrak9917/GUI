from tkinter import *
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

root = Tk()

def yt():
    chromepath = r"Chrome/chromedriver.exe"
    driver = webdriver.Chrome(chromepath)

    Names=[]
    urls=[]
    driver.get("https://www.youtube.com/feed/trending")

    content =driver.page_source
    soup = BeautifulSoup(content)
    html = soup.prettify('utf-8')
    ytdata = soup.findAll("a", class_ = "yt-simple-endpoint style-scope ytd-video-renderer")

    for x in ytdata:
        yt_href = x.get("href")
        yt_name = x.get("title")
        Names.append(yt_name)
        urls.append(yt_href)

    a=[]
    for i in range(len(urls)):
        compLink = "https://www.youtube.com"+urls[i]
        a.append(compLink)

    df = pd.DataFrame({"Video Title": Names, "URL":a})
    df.to_csv("yt_scrap.csv")
    return df

myButton = Button(root,text="YT Title", command=yt, fg="blue", bg="green", padx=100, pady=100)
myButton.pack()
root.mainloop()