#########################################################
# Author: Rajanikant Tenguria
# Start : 4 March 2019
# Last  : 10 March 2019
#########################################################
# Loading...                                      
# ======>                                           28 %
#########################################################
# Movie name                    - Done
# Year                          - Done
# Genre                         - Done 			
# Release Date                  - Done
# Duration 			
# Rating 			
# Reviewer count 	
# Director                      - Done
# Writer
# User Rev Count
# Critic Rev Count
# Wins                          - Done				
# Nominations                   - Done		
# Certificate		
# Language			
# Country			
# Gross 
# Production		
# Sound Mix			
# Color				
# Aspect Ratio
# Cast
# Rating Demographics
# Summary
# Keywords


import requests
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep
import json
import regex as re
headers = {'headers': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

url = 'https://www.imdb.com/title/tt2582802/'
page = requests.get(url)
xpage = str(page)
soup = BeautifulSoup(page.text, 'html.parser')
lname = soup.find('title')
#lgenre = soup.find(class_='subtext')
ldirector = soup.find(class_='credit_summary_item')
awards_list = soup.find(class_='article highlighted')
lrating = soup.find(class_='ratingValue')
ldate = soup.find(class_='title_wrapper')
director_list = soup.find(class_='credit_summary_item')
#print(awards_list)


p = str(soup.find('script', {'type':'application/ld+json'}))
intp = p.find('duration')+14
ldur = p[intp:intp+4]
x = re.findall(r'\d+',ldur)
lll = (soup.findAll("h4", class_="inline"))
dur = 60*int(x[0])+int(x[1])

genre = []
sound = []
production = []
certificate = []
writer = []
country = []
language = []
color = []

for h4 in lll:
	for text in h4:
		x = h4.find_next_siblings()
		for txt in x:
			#print(text,txt.contents)
			if text == 'Genres:':
				if len(str(txt.contents))>5:
					genre.append(str(txt.contents)[3:-2])
			if text == 'Sound Mix:':
				if len(str(txt.contents))>5:
					sound.append(str(txt.contents)[2:-2])
			if text == 'Production Co:':
				if len(str(txt.contents))>5:
					production.append(str(txt.contents)[2:-2])
				#production = production[:2]
			if text == 'Certificate:':
				if len(str(txt.contents))<11:
					certificate.append(str(txt.contents)[2:-2])
				#certificate = certificate[:1]
			
"""
for h4 in lll:
    for text in h4:
        print(text,h4.find_next_siblings())
"""
# Pull text from all instances of <a> tag within BodyText div
#genre = lgenre.find_all('a')
director = ldirector.find_all('a')
date = ldate.find_all('a')
#awards = awards_list.find_all('a')

# Create for loop to print out all artists' names
wins = 0
nominations = 0

for i in director:
    tdirector = i.contents[0]

for i in date:
    rdate = i.contents[0]

#print (awards_list)
if awards_list != None:
	tawards = awards_list.contents[0].split()
	if len(tawards)>2:
		wins = tawards[0]
		nominations = tawards[3]
	
	else:
		wins = 0
		nominations = tawards[0]

name = str(lname.contents)[2:-16]
year = str(lname.contents)[-14:-10]
day = rdate.strip().split()[0]
month = rdate.strip().split()[1]
year = rdate.strip().split()[2]
