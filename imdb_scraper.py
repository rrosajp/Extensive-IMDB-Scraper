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

url = 'https://www.imdb.com/title/tt2637294/'
page = requests.get(url)
xpage = str(page)
soup = BeautifulSoup(page.text, 'html.parser')
lname = soup.find('title')
ldirector = soup.find(class_='credit_summary_item')
lrating = soup.find(class_='ratingValue')
ldate = soup.find(class_='title_wrapper')
director_list = soup.find(class_='credit_summary_item')
lgenre = soup.find(class_='subtext')

director = ldirector.find_all('a')
date = ldate.find_all('a')
genre = lgenre.find_all('a')

# Create for loop to print out all content

for i in director:
    tdirector = i.contents[0]
   
for i in genre:
    tgenre = i.contents[0]

for i in date:
    rdate = i.contents[0]

awards_list = soup.find(class_='awards-blurb')
tawards = awards_list.contents[0].split()   
wins = tawards[0]
nominations = tawards[3]
