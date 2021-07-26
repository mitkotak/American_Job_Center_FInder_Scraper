from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open('test_zipcode.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k


print("Zipcodes : ",columns['Zipcode'])

print("Loading Chrome Driver..")
driver = webdriver.Chrome('./chromedriver/chromedriver_mac')
print("Done")

header = [ 'Zipcode','Center_Name','Google_Maps_Link','Center_Website','Emails']
file = open('scrapped.csv', 'w', newline ='')
with file:
	header = [ 'Zipcode','Center_Name','Google_Maps_Link','Center_Website','Emails']
	writer = csv.DictWriter(file, fieldnames = header)
	writer.writeheader()

	for zipcode in columns['Zipcode']:
		link = 'https://www.careeronestop.org/WorkerReEmployment/Toolkit/find-american-job-centers.aspx?location='+zipcode+'&radius=25&ct=0&y=0&w=0&e=0&sortcolumns=Distance&sortdirections=ASC&centerID=1517839'
		print('opening link')
		driver.get(link)
		print("Let's start scraping :)")
		elems  = driver.find_elements_by_xpath('//a[@class="notranslate"]')
		firstlink = elems[0].get_attribute("href")
		print("Let's go to the first center in this zipcode")
		driver.get(firstlink)
		print("Let's start scraping")
		center_name = driver.find_elements_by_xpath('//div[@id = "detailsheading" and @name = "details-heading" and @class="notranslate detail-heading"]')[0].text
		website =  driver.find_elements_by_xpath('//a[@target = "_blank"]')[0].text
		google_maps_link = driver.find_elements_by_xpath('//a[@target = "_blank" and @class = "directions-link" and text() = "Directions"]')[0].get_attribute('href')
		first_link_elems = driver.find_elements_by_xpath('//span[@class = "notranslate"]')
		emails = ''
		for s in range(len(first_link_elems)):
			Text  = first_link_elems[s].text
			if '@' in Text:
				emails+=Text+','
		email = emails[:-1]
		print('############################################################################################################################################################################################')	
		print(center_name)
		print('Emails : ',emails)
		print('Website : ',website)
		print('Google Maps : ',google_maps_link)
	
		writer.writerow({'Zipcode' : zipcode,'Center_Name': center_name,'Google_Maps_Link': google_maps_link, 'Center_Website' : website, 'Emails' : emails })


print('csv created')

