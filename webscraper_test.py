from seleniumwire import webdriver
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

#print("Loading Chrome Driver..")
#driver = webdriver.Chrome('./drivers/chromedriver_mac')
print("Loading Firefox Driver")
driver = webdriver.Firefox(executable_path=r'./drivers/geckodriver')
print("Done")

header = [ 'Zipcode','Center_Name','Google_Maps_Link','Center_Website','Emails']
file = open('scrapped.csv', 'w', newline ='')
with file:
	header = [ 'Zipcode','Center_Name','Google_Maps_Link','Center_Website','Emails']
	#writer = csv.DictWriter(file, fieldnames = header)
	#writer.writeheader()

	for zipcode in ['IL']:
		link_main = 'https://www.careeronestop.org/WorkerReEmployment/Toolkit/find-american-job-centers.aspx?location='+zipcode+'&radius=25&ct=0&y=0&w=0&e=0&sortcolumns=Distance&sortdirections=ASC&centerID=1517839&curPage=1&pagesize=500'
		print('opening link')
		driver.get(link_main)
		print('Going to American Job Centers in ' + zipcode)
		elems = driver.find_elements_by_xpath('//*[@id="AJCTable"]/table/tbody//child::td')
		if elems == []:
			continue
		links = []
		for i in range(0,len(elems),3):
			driver.back()
			print(driver.find_elements_by_xpath('//*[@id="AJCTable"]/table/tbody//child::td'))
			link_html = driver.find_elements_by_xpath('//*[@id="AJCTable"]/table/tbody//child::td')[i].get_attribute("innerHTML")
			link = 'https://www.careeronestop.org'+link_html.replace(';','&')[29:311]
			driver.get(link)
			print("Let's start scraping :)")
			center_name_link = driver.find_elements_by_xpath('//div[@id = "detailsheading" and @name = "details-heading" and @class="notranslate detail-heading"]')
			if center_name_link == []:
				continue
			center_name = center_name_link[0].text
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
	
			writer = csv.DictWriter(file, fieldnames = header)
			writer.writerow({'Zipcode' : zipcode,'Center_Name': center_name,'Google_Maps_Link': google_maps_link, 'Center_Website' : website, 'Emails' : emails })
			writer.writeheader()

print('csv created')

