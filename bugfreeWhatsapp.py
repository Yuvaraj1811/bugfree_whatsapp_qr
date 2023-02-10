import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
from datetime import datetime
import schedule
import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from unidecode import unidecode
import pandas as pd
options = Options()
import re
# import pymssql
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import getpass
from selenium.webdriver.common.action_chains import ActionChains
import configparser
from multiprocessing import Process
from threading import Thread
import uuid
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import schedule

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)


def qr_img():
    driver=webdriver.Chrome(r"C:\\Users\Admin\Desktop\\Yuvaraj\Scrapping\\chromedriver.exe")
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()
    time.sleep(3)
    while True:
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div").click()
            print("Clicking reload")
        except:
            print("No reload found")
        time.sleep(3)
        try:
            login=driver.find_element_by_css_selector('[data-testid="filter"]')
            print("User has login...")
            break
            
        except:
            try:
                qr_code = driver.find_element_by_css_selector('[data-testid="qrcode"]')
            except:
                print("No qr found")
            save_name = 'qr_img.png'
            try:
               qr_code.screenshot(r"C:\Users\Admin\Desktop\try/{}".format(save_name))
            except:
                print("Unable to save")
                break
    qr_img()
qr_img()
