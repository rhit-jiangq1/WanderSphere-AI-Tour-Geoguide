#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:37:15 2024

@author: komalwavhal
"""


"""

import requests
from bs4 import BeautifulSoup
import google_images_download

def get_tourist_places(country, city, category):
     
    # Scrapes Google Search Results for top tourist places.

    # Args:
    #     country: The country name.
    #     city: The city name.
    #     category: The preferred tourist category.

    # Returns:
    #     A list of tuples, each containing (place_name, image_url, description).
     

    search_query = f"{category} in {city}, {country}"
    response = requests.get(f"https://www.google.com/search?q={search_query}")
    soup = BeautifulSoup(response.content, 'html.parser')

    tourist_places = []
    for result in soup.find_all('div', {'class': 'g'}):
        try:
            title = result.find('div', {'class': 'title'}).text
            link = result.find('a')['href']
            image_url = google_images_download.googleimagesdownload().download({
                'keywords': title,
                'limit': 1,
                'output_directory': 'images',
                'print_urls': False
            })
            tourist_places.append((title, image_url, link))
        except AttributeError:
            pass

    return tourist_places[:10]




"show the top beach tourist places in India in city Mumbai"



if __name__ == "__main__":
    country = input("Enter the country: ")
    city = input("Enter the city: ")
    category = input("Enter the category (fall, summer, winter, beach, landscape, zoo, waterfall, waterpark, themepark): ")

    tourist_places = get_tourist_places(country, city, category)

    for place in tourist_places:
        print(f"Place: {place[0]}")
        print(f"Image: {place[1]}")
        print(f"Description: {place[2]}")
        print()
        
"""        
        
import requests
from bs4 import BeautifulSoup  
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
import requests
import time
from bs4 import BeautifulSoup  
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 


def getSearch_Data(page_url):
        
    driver = webdriver.Chrome()
    
    # send a request
    driver.get(page_url)

    # enter your code
    driver.maximize_window()         
    
    pagecheck=False
    while pagecheck!=True:
        if "wait" in driver.title:
            driver.refresh()
        elif "Bing Maps - Directions, trip planning, traffic cameras & more" in driver.title:
            print('title found now move to next step')
            pagecheck=True
            
    time.sleep(10)        
        
    ################################################################################
    ##reviewer's name (see (1) in Figure)
    user_option_selection = "park"
    user_city_selection = "New York"
    country_name = "United States"
    user_query = "Top " + user_option_selection + " Tourist Attractions in " + user_city_selection + " city from country " + country_name +" with image and details like address" 
    print(user_query)
    
    pagecheck=False
    while pagecheck!=True:
        try: 
            xpath =  '//input[@id="maps_sb"]'
            query_search = driver.find_element(By.XPATH,xpath)
            query_search.clear()
            query_search.send_keys(user_query)
            time.sleep(2) 
            pagecheck = True
            print("-------- user_query found----------")
        except:
            print("--------Finding quesry Search bar on page-----------")
            pagecheck=False
    #print("-------- Quesry Search bar on page found-----------",Query)
     
    ################################################################################
   
    
    pagecheck=False
    while pagecheck!=True:
        try: 
            xpath =  '//*[@id="maps_sb_container"]/div[1]/div[2]/a'
            query_search_button = driver.find_element(By.XPATH,xpath)
            query_search_button.click() 
            pagecheck = True
            print("-------- query_search_button found----------")
        except:
            print("--------Finding quesry Search button on page-----------")
            pagecheck=False
    #print("-------- Quesry Search button on page found-----------",Query)
     
    
    ### checkpoint to validate if the search result is found or not
    pagecheck=False
    while pagecheck!=True:
        try: 
            xpath =  '//*[@id="maps_sb_container"]/div[1]/a/div/div/div' 
            query_search_result = driver.find_element(By.XPATH,xpath)
            if (query_search_result):
                pagecheck = True
                print("-------- query_search_result found----------")
        except:
            print("--------Finding if search result on page-----------")
            pagecheck=False
    #print("-------- Quesry Search search result on page found-----------",Query)
    
    time.sleep(10)   
    
        
page_url = "https://www.bing.com/maps?cp=40.753474%7E-73.982309&lvl=13.1"        
getSearch_Data(page_url)        
        





        
        
        