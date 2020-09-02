from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import random as rndm
from random import seed
import random
from time import sleep
driver = webdriver.Chrome("C:\\Users\\Rajdeep\\Desktop\\chromedriver.exe")

fnames = []
lnames = []
locations = []
colleges = []
numbers = []

with open('C:\\Users\\Rajdeep\\Documents\\Python Code\\selenium\\jaro\\firstnames.txt', 'r') as f:
    for item in f:
        fnames.append(item)

with open('C:\\Users\\Rajdeep\\Documents\\Python Code\\selenium\\jaro\\lastnames2.txt', 'r') as f:
    for item in f:
        lnames.append(item)

with open('C:\\Users\\Rajdeep\\Documents\\Python Code\\selenium\\jaro\\colleges.txt', 'r') as f:
    for item in f:
        colleges.append(item)

with open('C:\\Users\\Rajdeep\\Documents\\Python Code\\selenium\\jaro\\locations.txt', 'r') as f:
    for item in f:
        locations.append(item)

with open('C:\\Users\\Rajdeep\\Documents\\Python Code\\selenium\\jaro\\numbers.txt', 'r') as f:
    for item in f:
        numbers.append(item)

while True:
    fname = random.choice(fnames).strip()
    lname = random.choice(lnames).strip()
    driver.get("https://docs.google.com/forms/d/e/M5YKuPkrAOiStNGgokb_0aOK173lsj-1FAIpQLScicob_MvnDQ7p-asw/viewform?vc=0&c=0&w=1")
    elem = driver.find_element_by_xpath("//input[@aria-label='Your Full Name ']")
    elem.clear()
    elem.send_keys(fname + ' ' + lname)
    elem = driver.find_element_by_xpath("//input[@aria-label='Your Contact Number']")
    elem.clear()
    elem.send_keys(random.choice(numbers).strip())
    elem = driver.find_element_by_xpath("//input[@aria-label='Your Email ID']")
    elem.clear()
    elem.send_keys((fname + lname).lower() + str(rndm())[2:5] + '@gmail.com')
    picker = '//div[@aria-posinset="' + str(int(str(rndm())[2:3]) % 3 + 1) + '"]'
    driver.find_element_by_xpath(picker).click()
    elem = driver.find_element_by_xpath("//input[@aria-label='College Name and City']")
    elem.clear()
    elem.send_keys(random.choice(colleges).strip())
    elem = driver.find_element_by_xpath("//input[@aria-label='Current Location']")
    elem.clear()
    elem.send_keys(random.choice(locations).strip())
    driver.find_element_by_xpath("//div[@aria-label='Full -Time']").click()
    driver.find_element_by_xpath("//span[@class='appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel']").click()
