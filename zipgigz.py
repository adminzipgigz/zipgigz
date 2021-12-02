from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests

for _ in range(1,2):
    url = r"https://www.naukri.com/react-dot-js-jobs-"+str(_)+r"?k=React.Js"

    page = requests.get(url)

    driver = webdriver.Chrome(r"D:\Downloads\chromedriver.exe")
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    # print(soup.prettify())
    driver.close()
    results = soup.find(class_='list')
    job_elems = results.find_all('article',class_='jobTuple bgWhite br4 mb-8')
    for job_elem in job_elems:
        Sal = job_elem.find('li',class_='fleft grey-text br2 placeHolderLi salary')
        Sal_span = Sal.find('span',class_='ellipsis fleft fs12 lh16')
        if Sal_span is None:
            continue
        else:
            sal = Sal_span.text
            if(sal != "Not disclosed"):
                print(sal)
