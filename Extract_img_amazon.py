import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import csv
import time as t
a=webdriver.Chrome()
a.get("https://www.amazon.in/")
t.sleep(5)
image=a.find_elements(By.TAG_NAME,'img')
url=[]
for i in image:
    x=i.get_attribute("src")
    url.append(x)
print(url)

with open("C:\\Users\\manojana\\OneDrive\\Desktop\\test1.csv", "w",
          newline="") as f:
    file = csv.writer(f)
    file.writerow(["Amazon images"])
    for i in url:
        file.writerow([i])
