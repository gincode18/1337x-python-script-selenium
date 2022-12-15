from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import re
import time
import sys
print("enter string")
a=input()

PATH="/home/vishal/python/chromedriver"
options = Options()
options.headless = True
driver=webdriver.Chrome(PATH,options=options)
driver.get("https://www.1377x.to/")
search=driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/form/input")
search.send_keys(a)
search.send_keys(Keys.RETURN)
search2=driver.find_element(By.XPATH,"/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/a[2]")

#/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr[4]/td[1]/a[2]

for i in range(1,9):
    try:
        d="/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr["+ str(i) + "]/td[1]/a[2]"
        search2=driver.find_element(By.XPATH,d)
        print(str(i)+": "+search2.text)
    except:
        break
n=int(input())
for i in range(1,9):
    if(i==n):
        d="/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr["+ str(i) + "]/td[1]/a[2]"
        search2=driver.find_element(By.XPATH,d)
        print(search2.text)


action = ActionChains(driver)
action.click(on_element = search2)
action.perform()

x=driver.page_source

#open text file
text_file = open("txt.html", "w")
 
#write string to file
text_file.write(x)
 
#close file
text_file.close()
driver.close()
y = re.search("magnet:\?xt=urn:btih:[a-zA-Z0-9]*",x)
print(y.group())
os.system(f"webtorrent {y.group()} --mpv --playlist")



