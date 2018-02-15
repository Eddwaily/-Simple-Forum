from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()

i=0
while i<3:
    sleep(10)
    driver.get("https://www.youtube.com/watch?v=O3EeZqX-u5k")
    i+=1
sleep(20)
