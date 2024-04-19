import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
 
#logsin to linkedin account
#REPLACE 'Insert username here' WITH USERNAME
#REPLACE 'Insert password here' WITH PASSWORD
def login(driver):
    try:
        driver.get("https://linkedin.com/uas/login")
        wait = WebDriverWait(driver, 10)
        username = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username.send_keys("insert username here")
        pword = wait.until(EC.presence_of_element_located((By.ID, "password")))
        pword.send_keys("insert password here")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    except Exception as e:
        print(f"Login failed: {e}")
        driver.quit()
        raise SystemExit("Script execution stopped due to login failure.")

#opensprofile and scrolls to bottom of the page
def openprofile(profile_url,driver):
    try:
        driver.get(profile_url)  
        start = time.time()
        initialScroll = 0
        finalScroll = 1000
         
        while True:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
            initialScroll = finalScroll
            finalScroll += 1000
            time.sleep(1)
            end = time.time()
            if round(end - start) > 5:
                break
    except:
        print('Failed to load profile')
        raise SystemExit()

#extracts the headcount insights
def extract(driver):
    try:
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')
        text = soup.find("a", class_="ember-view full-width link-without-hover-visited")
        if text:
            parsed = BeautifulSoup(str(text), 'html.parser')       
            anchor = parsed.find('a', attrs={'aria-label': True})
            if anchor:
                aria_label_text = (anchor['aria-label']).split()
                if aria_label_text[1] == 'increase':
                    Trend = (aria_label_text[0])
                elif aria_label_text[1] == 'decrease':
                    Trend = '-'+str((aria_label_text[0]))
                return Trend
    except Exception as e:
        print(f"Error extracting info: {e}")
        raise SystemExit('Script stopped due to extraction failure')

#calls the extract function and stores the extracted data in a dictionary
def storedata(driver):
    names = []
    trend = []

    try:
        with open('links.csv',"r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                names.append(row[0])
                openprofile(row[1],driver)
                value = str(extract(driver)).strip('%')
                trend.append(value)
    except FileNotFoundError:
        print('links.csv not found ensure it is in the same folder')
        raise SystemExit()
    
    with open('IndustryTrends.csv',"a", newline='') as file:
        csv_writer = csv.writer(file,delimiter=',')
        if os.path.getsize('IndustryTrends.csv') == 0:
            csv_writer.writerow(names)
        csv_writer.writerow(trend)

with webdriver.Chrome() as driver:
    login(driver)
    storedata(driver)






