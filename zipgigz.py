from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import csv

job = input()

csv_file = open('Naukri_scrape.csv', 'a', encoding="utf-8", newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title','Company','Experience','Salary','Location','URL'])

flag = True

c = 0

i = 1

while(flag):

    url = r"https://www.naukri.com/" + job + "-jobs-"+str(i)
    i += 1
    page = requests.get(url)

    driver = webdriver.Chrome(r"D:\Downloads\chromedriver.exe")

    driver.get(url)

    time.sleep(5)
    
    soup = BeautifulSoup(driver.page_source,'html.parser')
    # print(soup.prettify())
    driver.close()
    results = soup.find(class_='list')
    job_elems = results.find_all('article',class_='jobTuple bgWhite br4 mb-8')
    for job_elem in job_elems:

        URL = job_elem.find('a',class_='title fw500 ellipsis').get('href')

        Title_ = job_elem.find('a',class_='title fw500 ellipsis')
        if Title_ is None:
            continue
        else:
            Title = Title_.text

        Company_ = job_elem.find('a',class_='subTitle ellipsis fleft')
        if Company_ is None:
            continue
        else:
            Company = Company_.text

        Exp = job_elem.find('li',class_='fleft grey-text br2 placeHolderLi experience')
        if(Exp is None):
            continue
        Exp_span = Exp.find('span',class_='ellipsis fleft fs12 lh16')
        if Exp_span is None:
            continue
        else:
            Experience = Exp_span.text

        Sal = job_elem.find('li',class_='fleft grey-text br2 placeHolderLi salary')
        Sal_span = Sal.find('span',class_='ellipsis fleft fs12 lh16')
        if Sal_span is None:
            continue
        else:
            sal = Sal_span.text
            if(sal == "Not disclosed"):
                continue

        Loc = job_elem.find('li',class_='fleft grey-text br2 placeHolderLi location')
        Loc_exp = Loc.find('span',class_='ellipsis fleft fs12 lh16')
        if Loc_exp is None:
            continue
        else:
            Location = Loc_exp.text

        c += 1
        csv_writer.writerow([Title, Company, Experience, sal, Location,URL])
        

    if(c == 100):
        flag = False
    

    

csv_file.close()