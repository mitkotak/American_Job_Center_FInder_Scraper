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

file = open('scrapped.csv', 'w+', newline ='')
with file:
	#header = [ 'Zipcode','Center_Name','Google_Maps_Link','Center_Website','Emails','Address','Phone','Telephones','Fax Machines','On-site Childcare','Video Viewing Stations','Rooms where employers can interview job seekers','Career Resource Room','Copy Machine','Personal Computers','Internet Access','Post your resume for employers to see','Get help in preparing for job interviews','Learn about strategies for finding a job','Find out how to get a work permit','Find out about job openings (including work experience, internships and community service)','Get help preparing your resume','Improve your current job skills','Learn about the world of business','Learn new job skills','Improve your English skills (ESL)','Improve your reading, writing and math skills','Get information about schools and training programs','Prepare for a high school equivalency (HSE) exam','Learn about financial aid for training','Get help finding child care','Get help with living expenses while in training','Get information about employers in your local area','Assess your reading and math skills','Learn about jobs and careers suitable for you','Learn about what employers expect of their workers','Assess your career interests and skills','Learn about jobs in demand and rates of pay','Find out about summer learning opportunities','Get help in finding a summer job','File Unemployment Insurance (UI) Claim','Get help in coping with the stress of job loss','Get help coping financially with job loss','Learn about community resources','Share job-search strategies with other job seekers (job club)','Get help preparing your resume','Learn about strategies for finding a job','Find out about job openings','Get help in preparing for job interviews','Post your resume for employers to see','Get information about education and training schools, such as their tuition and success in placing students in jobs','Prepare for a high school equivalency (HSE) exam','Improve your current job skills','Improve your English skills (ESL)','Improve your reading writing and math skills','Learn how to start your own business','Receive training in new job skills','Get help finding childcare','Get help with living expenses while in training','Assess your reading and math skills','Learn about jobs in demand and rates of pay','Learn about what employers expect of their workers','Get information about employers in your local area','Learn about jobs and careers suitable for you','Assess your career interests','Get outplacement services for employees you are laying off','Get information on employment, wage and salary trends','Receive information on the Work Opportunity Tax Credit and other hiring incentives','Learn about legal requirements for hiring and firing workers','Learn about EEO and ADA requirements','Get your employee training needs analyzed','Learn about Unemployment Insurance taxes and eligibility rules','Get training costs reimbursed for qualified job candidates','Develop programs to train new workers for your business','Get help in analyzing and writing job descriptions','Learn how to interview job applicants effectively','Learn about strategies for recruiting workers','Have job applicants` skills tested','Get job applicants pre-screened','Get access to resumes posted by job applicants','Post your job openings','Have background checks conducted on job applicants','Use on-site facilities for recruiting and interviewing job applicants']	
	
	#writer = csv.DictWriter(file, fieldnames = header)
	#writer.writeheader()

	for zipcode in columns['Zipcode']:
		link = 'https://www.careeronestop.org/WorkerReEmployment/Toolkit/find-american-job-centers.aspx?location='+zipcode+'&radius=5&ct=0&y=0&w=0&e=0&sortcolumns=Distance&sortdirections=ASC&centerID=1517839'
		print('opening link')
		driver.get(link)
		print("Let's start scraping :)")
		elems  = driver.find_elements_by_xpath('//a[@class="notranslate"]')
		if elems == []:
			continue
		firstlink = elems[0].get_attribute("href")
		print("Let's go to the first center in this zipcode")
		driver.get(firstlink)
		print("Let's start scraping")
		center_name_elems = driver.find_elements_by_xpath('//div[@id = "detailsheading" and @name = "details-heading" and @class="notranslate detail-heading"]')
		if center_name_elems == []:
			continue	
		center_name = center_name_elems[0].text
		website_elems  =  driver.find_elements_by_xpath('//a[@target = "_blank"]')
		if website_elems == []:
			continue
		website = website_elems[0].text 
		google_maps_link_elems  = driver.find_elements_by_xpath('//a[@target = "_blank" and @class = "directions-link" and text() = "Directions"]')
		if google_maps_link_elems == []:
			continue
		google_maps_link = google_maps_link_elems[0].get_attribute('href')
		first_link_elems = driver.find_elements_by_xpath('//span[@class = "notranslate"]')
		if first_link_elems == []:
			continue
		emails = ''
		for s in range(len(first_link_elems)):
			Text  = first_link_elems[s].text
			if '@' in Text:
				emails+=Text+','
		email = emails[:-1]
		address_elems = driver.find_elements_by_xpath('//*[@id="ctl27_tbAJCDetail"]/tr[1]/td[2]/span')
		if address_elems == []:
			continue
		address = address_elems[0].text
		phone_element = driver.find_elements_by_xpath('//*[@id="ctl27_tbAJCDetail"]/tr[2]/td[2]/a')
		if phone_element == []:
			continue 
		phone = phone_element[0].text
		gr_elements = driver.find_elements_by_xpath('//*[@id="GenInfo"]/table/tbody//child::td')
		if gr_elements == []:
			continue
		print('############################################################################################################################################################################################')
		
		grs = []
		GR = {}
		for i in range(0,len(gr_elements),2):
			gr_col1 = gr_elements[i].get_attribute("innerHTML")[4:-4]
			gr_col2 = gr_elements[i+1].get_attribute("innerHTML")
			if gr_col2[0] == 'N':
				gr_col2 = gr_col2[0:2]
			elif gr_col2[0] == 'Y':
				gr_col2 = gr_col2[0:3]
			else:
				gr_col2 = gr_col2
			print(gr_col1)
			grs.append(gr_col1)
			print(gr_col2)
			GR[gr_col1] = gr_col2

		#srs = ['Telephones','Fax Machines','On-site Childcare','Video Viewing Stations','Rooms where employers can interview job seekers','Career Resource Room','Copy Machine','Personal Computers','Internet Access']	
		SR = {}
		srs = []
		for i in range(1,10):
			sr_col1_link = '//*[@id="SR"]/table/tbody/tr['+str(i)+']/td[1]'
			sr_col1 = driver.find_elements_by_xpath(sr_col1_link)[0].get_attribute("innerHTML")[4:-4]
			print(sr_col1)
			sr_col2_link = '//*[@id="SR"]/table/tbody/tr['+str(i)+']/td[2]'
			sr_col2 = driver.find_elements_by_xpath(sr_col2_link)[0].get_attribute("innerHTML")[0:3]
			if sr_col2[0] == 'N':
				sr_col2 = sr_col2[0:2]
			print(sr_col2)				
			SR[sr_col1] = sr_col2
			srs.append(sr_col1)

		#yss = ['Post your resume for employers to see','Get help in preparing for job interviews','Learn about strategies for finding a job','Find out how to get a work permit','Find out about job openings (including work experience, internships and community service)','Get help preparing your resume','Improve your current job skills','Learn about the world of business','Learn new job skills','Improve your English skills (ESL)','Improve your reading, writing and math skills','Get information about schools and training programs','Prepare for a high school equivalency (HSE) exam','Learn about financial aid for training','Get help finding child care','Get help with living expenses while in training','Get information about employers in your local area','Assess your reading and math skills','Learn about jobs and careers suitable for you','Learn about what employers expect of their workers','Assess your career interests and skills','Learn about jobs in demand and rates of pay','Find out about summer learning opportunities','Get help in finding a summer job']
		YS = {}
		yss = []
		for i in range(1,25):
			ys_col1_link ='//*[@id="YS"]/table/tbody/tr['+str(i)+']/td[1]'	
			ys_col1 = driver.find_elements_by_xpath(ys_col1_link)[0].get_attribute("innerHTML")[4:-4]
			print(ys_col1)
			ys_col2_link ='//*[@id="YS"]/table/tbody/tr['+str(i)+']/td[2]'
			ys_col2 = driver.find_elements_by_xpath(ys_col2_link)[0].get_attribute("innerHTML")[0:3]
			if ys_col2 == 'N':
				ys_col2 = ys_col2[0:2]
			print(ys_col2)
			YS[ys_col1] = ys_col2	
			yss.append(ys_col1)

		#wss = ['File Unemployment Insurance (UI) Claim','Get help in coping with the stress of job loss','Get help coping financially with job loss','Learn about community resources','Share job-search strategies with other job seekers (job club)','Get help preparing your resume','Learn about strategies for finding a job','Find out about job openings','Get help in preparing for job interviews','Post your resume for employers to see','Get information about education and training schools, such as their tuition and success in placing students in jobs','Prepare for a high school equivalency (HSE) exam','Improve your current job skills','Improve your English skills (ESL)','Improve your reading writing and math skills','Learn how to start your own business','Receive training in new job skills','Get help finding childcare','Get help with living expenses while in training','Assess your reading and math skills','Learn about jobs in demand and rates of pay','Learn about what employers expect of their workers','Get information about employers in your local area','Learn about jobs and careers suitable for you','Assess your career interests']
		WS = {}	
		wss = []
		for i in range(1,27):
			ws_col1_link ='//*[@id="WS"]/table/tbody/tr['+str(i)+']/td[1]'
			ws_col1 = driver.find_elements_by_xpath(ws_col1_link)[0].get_attribute("innerHTML")[4:-4]
			print(ws_col1)
			ws_col2_link ='//*[@id="WS"]/table/tbody/tr['+str(i)+']/td[2]'
			ws_col2 = driver.find_elements_by_xpath(ws_col2_link)[0].get_attribute("innerHTML")[0:3]
			if ws_col2 == 'N':
				ws_col2 = ws_col2[0:2]
			print(ws_col2)
			WS[ws_col1] = ws_col2
			wss.append(ws_col1)

		#bss = ['Get outplacement services for employees you are laying off','Get information on employment, wage and salary trends','Receive information on the Work Opportunity Tax Credit and other hiring incentives','Learn about legal requirements for hiring and firing workers','Learn about EEO and ADA requirements','Get your employee training needs analyzed','Learn about Unemployment Insurance taxes and eligibility rules','Get training costs reimbursed for qualified job candidates','Develop programs to train new workers for your business','Get help in analyzing and writing job descriptions','Learn how to interview job applicants effectively','Learn about strategies for recruiting workers','Have job applicants` skills tested','Get job applicants pre-screened','Get access to resumes posted by job applicants','Post your job openings','Have background checks conducted on job applicants','Use on-site facilities for recruiting and interviewing job applicants']
		BS = {}
		bss = []
		for i in range(1,19):
			bs_col1_link ='//*[@id="BS"]/table/tbody/tr['+str(i)+']/td[1]'
			bs_col1 = driver.find_elements_by_xpath(bs_col1_link)[0].get_attribute("innerHTML")[4:-4]
			print(bs_col1)
			bs_col2_link ='//*[@id="BS"]/table/tbody/tr['+str(i)+']/td[2]'
			bs_col2 = driver.find_elements_by_xpath(bs_col2_link)[0].get_attribute("innerHTML")[0:3]
			if bs_col2 == 'N':
				bs_col2 = bs_col2[0:2]
			print(bs_col2)
			BS[bs_col1] = bs_col2
			bss.append(bs_col1)

		print(center_name)
		print('Emails : ',emails)
		print('Website : ',website)
		print('Google Maps : ',google_maps_link)
		print('Address : ',address)
		print('Phone : ',phone)
		dict_csv = {'Zipcode'              : zipcode,
                                'Center_Name'           : center_name,
                                'Google_Maps_Link'      : google_maps_link,
                                'Center_Website'        : website,
                                'Emails'                : emails,
                                'Address'               : address,
                                'Phone'                 : phone }
       
		header = ['Zipcode','Center_Name','Google_Maps_Link','Center_Website','Emails','Address','Phone']
		for gr in grs:
			dict_csv[gr] = GR[gr]
			if gr not in header:
				header.append(gr)

		for sr in srs:
			dict_csv[sr] = SR[sr]
			if sr not in header:
				header.append(sr)
		
		for ys in yss:
			dict_csv[ys] = YS[ys]
			if ys not in header:
				header.append(ys)

		for ws in wss:
			dict_csv[ws] = WS[ws]
			if ws not in header:
				header.append(ws)
	
		for bs in bss:
			dict_csv[bs] = BS[bs]
			if bs not in header:
				header.append(bs)
            
		writer = csv.DictWriter(file, fieldnames = header)
		writer.writerow(dict_csv)
	writer.writeheader()
print('csv created')

