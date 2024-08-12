from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
START_URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser=webdriver.Chrome()
browser.get(START_URL)
time.sleep(10)
planets_data=[]
def scrape():
    for i in range(0,346):
        soup=BeautifulSoup(browser.page_source,"html")
        for h3_tag in soup.find_all("h3",attrs={"class","heading-22 margin-0"}):
            temp_list=[]
            temp_list.append(h3_tag.contents)
            planets_data.append(temp_list)
    print(planets_data[69])
scrape()
headers=["Planets Information"]
planet=pd.DataFrame(planets_data,columns=headers)
planet.to_csv("Knowldge_Hub.csv",index=True,index_label="id")