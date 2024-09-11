from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchWindowException
import time
import numpy as np

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://quotes.toscrape.com/')

allquotes=[]

quotes=driver.find_elements(by="xpath",value="//span[@class='text']")
authors=driver.find_elements(by="xpath",value="//small")

for i , j in zip(quotes,authors):
    allquotes.append({
        "text":i.text,
        "author":j.text
    })
# print(allquotes)
guesses=3

quote=np.random.choice(allquotes)
print(quote["text"])
userguess=''
while guesses !=0 and userguess.lower() != quote["author"].lower():
    userguess=input("enter the author\n")
    if userguess==quote["author"]:
        print("congratulations")
        break
    
    elif guesses>1:
        print("try again\n")
    else:
        print("loser\n")
    guesses-=1

