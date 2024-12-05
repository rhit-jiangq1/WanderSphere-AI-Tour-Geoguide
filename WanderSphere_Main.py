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
from selenium import webdriver
import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font 
from openpyxl.styles import PatternFill
from openpyxl.styles.borders import Border, Side, BORDER_THIN
from openpyxl.styles import Alignment 
import os 
import pandas as pd
from datetime import datetime
# from selenium.webdriver.common.window import WindowType


def getSearch_Data(page_url):
    
    ################################################################################
    ####  Variable Initilization  
    
    # Create an empty dictionary
    my_data_dict = {}
    places_data = {}
    user_reviews_tmp = []
    my_data_dict["place_Name"] = []
    my_data_dict["user_reviews"] = []
    my_data_dict["place_location"] = ""
    my_data_dict["ratings"] = ""
    my_data_dict["img_path_of_location"] = ""
    my_data_dict["wikipedia_result"] = "" 
    
 
    user_option_selection = "park"
    user_city_selection = "New York"
    country_name = "United States"
    user_query = "Top " + user_option_selection + " Tourist Attractions in " + user_city_selection + " city from country " + country_name +" with image and details like address" 
    print(user_query)
    
    ################################################################################

        
    driver = webdriver.Chrome()
    
    # send a request to open URL
    driver.get(page_url)
    
    # maximize the chrome browser window 
    driver.maximize_window()     
    time.sleep(7)   
    
    driver.execute_script("document.body.style.zoom='30%'")  # Adjust the percentage as needed
    time.sleep(3)
    
    #### check point if page is loaded or not
    pagecheck=False
    while pagecheck!=True:
        if "wait" in driver.title:
            driver.refresh()
        elif "Bing Maps - Directions, trip planning, traffic cameras & more" in driver.title:
            print('title found now move to next step')
            pagecheck=True
            
    time.sleep(3)        
        
    
    ######## search the query on page 
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
     
    ################################################################################
    
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
    
    time.sleep(2)   
    
    
    ################################################################################
    
    """
    ####get the data for top 10 results
    """
    ### checkpoint to validate if the search result is found or not
    pagecheck=False
    while pagecheck!=True:
        try: 
            for i in range(1,11): 
                
                xpath =  '//*[@class="entity-listing-container"]/div/ul/li[' + str(i) + ']'
                top_15_search_results = driver.find_element(By.XPATH,xpath)
                
                if (top_15_search_results):
                    driver.find_element(By.XPATH,xpath).click()
                    time.sleep(3)
                    
                    try:
                        
                                            
                        ################################################################################
                        
                        ### place name xpath
                        xpath_placename = '//h2[@class="nameContainer"]'
                        #'(//div[@class="bm_scrollbarMask"]//div/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div/h2)[3]'
                        place_Name = driver.find_element(By.XPATH,xpath_placename).text
                        place_Name = place_Name.strip()
                                                                        
                        val = place_Name.replace("More", "")
                        val = val.replace("Share", "")
                        val = val.replace("Save", "")
                        place_Name = val.strip()
                        
                        print(place_Name)
                        print('============== Running for the ' , i , ' search: ' , place_Name , ' location now ================')                        
                         
                        
                        
                         
                        
                        ################################################################################
                        """
                        ##### Collect reviews of user to perform the sentiment analysis and check the positive and negative comments 
                        """
                        print('COllect user reviews in list ')
                        ###### Error handling as the reviews are not present on all location 
                        try:
                            xpath_user_reviews = '//*[contains(@class,"b_reviewText")]//div[2]/span'
                            element = driver.find_element(By.XPATH,xpath_user_reviews)
                            for elem in element:
                                user_reviews_tmp = []
                                val = elem.get_attribute('text')
                                user_reviews_tmp.append(val)
                            print('user_reviews_tmp: ' , user_reviews_tmp)
                        except: pass 
                        
                        
                         
                         
                        ################################################################################
                        print('code to get the location title ')
                        ### location title xpath
                        xpath_location = '//*[@id="IconItem_1"]/div' 
                        place_location = driver.find_element(By.XPATH,xpath_location).text
                        print('place_location: ', place_location)
                       
                        
                        ################################################################################
                        
                        ### rating of location xpath  
                        try:
                            xpath_rating = '(//div[@class="b_wftp_tms b_wftp_init"]//span[@class="csrc sc_rc1" and @role="img"])[1]' 
                            ratings = driver.find_element(By.XPATH, xpath_rating).get_attribute("aria-label")
                        except:
                            xpath_rating = '//*[@id="wpc_tp"]/div[1]/div[1]/div/div[2]/div/span'
                            ratings = driver.find_element(By.XPATH, xpath_rating).get_attribute("aria-label")
                         
                        print('ratings: ',ratings)
                      
                           
                        ################################################################################
                        ### first image xpath  
                        try:
                            xpath_img_url = '((//*[@class="overlay-container"])[2]//a)[1]'
                            img_path_of_location = driver.find_element(By.XPATH, xpath_img_url).get_attribute("href")
                        except:
                            xpath_img_url = '((//*[@class="overlay-container"])[3]/div//img[1])[1]'
                            img_path_of_location = driver.find_element(By.XPATH, xpath_img_url).get_attribute("href")

                        print('img_path_of_location: ', img_path_of_location)
                    except:pass
                
                
                    
                    print("-------- query_search_ for top 10 results found----------")
                    
                    print('============== Run for next location now ================')
                 
                
                    ################################################################################
                    """
                    ### use place name to search the wikipedia first column - open the second tab and close the tab once the work is done 
                    """
                    
                    try:
                        # Get all window handles --->>> all the window open in chrome 
                        ## this function is very helpful to work with multiple windows in same project 
                        window_handles = driver.window_handles
                          
                        # Open a new tab using JavaScript
                        driver.execute_script("window.open('');")
                        
                        # Switch to the new tab
                        driver.switch_to.window(driver.window_handles[1])
                        
                        # Open a URL in the new tab
                        search_url_query = "https://www.bing.com/search?q=" + place_Name + " Wikipedia"
                        driver.get(search_url_query)
                        time.sleep(5)
                                       
                        """
                        ### minimize the chrome window - because the seleniujm only pickup the data that is visible on scree for this page
                        ### so screen minimization will help to get more results visible on window 
                        """
                        
                        driver.execute_script("document.body.style.zoom='30%'")  # Adjust the percentage as needed
                        time.sleep(10)
                        
                        
                        xpath_wiki = '(//div[text()="Wikipedia"])[1]'
                        driver.find_element(By.XPATH,xpath_wiki).click()
                                      
                        """
                        ### New Window Tab:  Minimize the chrome window - because the seleniujm only pickup the data that is visible on scree for this page
                        ### so screen minimization will help to get more results visible on window 
                        """
                        
                        driver.execute_script("document.body.style.zoom='30%'")  # Adjust the percentage as needed
                        time.sleep(5)
                        
                                 
                        """
                        ### check if the wikipedia page is available if not then wait untill its get available 
                        """
                        pagecheck1=False
                        while pagecheck1!=True:
                            if "wait" in driver.title:
                                time.sleep(5)
                                driver.refresh()
                            elif "Wikipedia" in driver.title:
                                print('title found now move to next step')
                                pagecheck1=True
                         
                        time.sleep(5)   
                    except:pass 
                     
                    
                      
                    """
                    # Switch to the third tab as in my system when we click on any hyperlink it opens into new window page  
                    """
                    try:
                        driver.switch_to.window(window_handles[2])
                        time.sleep(5)
                    except:pass
                    
                    ### minimize the window zoom 
                    driver.execute_script("document.body.style.zoom='30%'")  # Adjust the percentage as needed
                    time.sleep(3)
                    
                    print('new window page is opened ')
                     
                             
                    """
                    ### check if the wikipedia page is available if not then wait untill its get available 
                    """
                    pagecheck1=False
                    while pagecheck1!=True:
                        if "wait" in driver.title:
                            driver.refresh()
                        elif "Wikipedia" in driver.title:
                            print('title found now move to next step')
                            pagecheck1=True
                            
                    wikipedia_result = ''
                    
                    ###### collect the place/location details from wikipedia page 
                    try: 
                        xpath =  '//*[@id="mw-content-text"]/div[1]/p[2]'
                        query_search_result = driver.find_element(By.XPATH,xpath)
                        
                        if (query_search_result):
                            wikipedia_result = query_search_result.text
                            print('wikipedia_result: ', wikipedia_result) 
                            print("-------- query_search_result found----------") 
                    except:pass
                     
                    
                    ################################################################################
                    
                    # try:
                    print('  user_reviews_tmp  : ', user_reviews_tmp)
                    print('   place_Name : ',place_Name )
                    print('  place_location  : ', place_location)
                    print('   ratings : ',ratings )
                    print('  img_path_of_location  : ', img_path_of_location)
                    print('   wikipedia_result : ', wikipedia_result)
                    
                    """
                    # Add the key "user_reviews" and assign the value from the variable
                    """  
                    print('adding the value in dict')
                    my_data_dict["user_reviews"] = user_reviews_tmp
                    print('value added in dictionary')
                    
                    """
                    ##### Add the key "place_name" and assign the value from the variable
                    """
                    my_data_dict["place_Name"] = place_Name
                    """
                    # Add the key "place_location" and assign the value from the variable
                    """
                        
                    my_data_dict["place_location"] = place_location
                        
                    """
                    # Add the key "ratings" and assign the value from the variable
                    """
                    my_data_dict["ratings"] = ratings 
                    """
                    # Add the key "img_path_of_location" and assign the value from the variable
                    """
                    my_data_dict["img_path_of_location"] = img_path_of_location 
                    """ 
                    ### Add the key "img_path_of_location" and assign the value from the variable
                    """ 
                    my_data_dict["wikipedia_result"] = wikipedia_result
                
                                        
                    ################################################################################     
                    #### print my_data_dict dictionary
                    print(my_data_dict)
                    
                        
                    # ################################################################################
                    
                    # Create a dictionary to store the data for the place
                    places_data = {
                        my_data_dict["place_Name"]: {
                            "user_reviews": my_data_dict["user_reviews"],
                            "place_location": my_data_dict["place_location"],
                            "ratings": my_data_dict["ratings"],
                            "img_path_of_location": my_data_dict["img_path_of_location"],
                            "wikipedia_result": my_data_dict["wikipedia_result"]
                        }
                    }
                    
                    print('places_data', places_data)
                    
                    # except:pass 
                    
                    ################################################################################
                    
                    
                    
                    
                    
                    
                    ######## error handling for multiple windows opened 
                    try:
                        ### Close the first tab
                        driver.switch_to.window(window_handles[1])
                        driver.close()
                    except:pass
                     
                    try:
                        ### Close the second tab
                        driver.switch_to.window(window_handles[2])
                        driver.close()
                    except:pass
                    
                    """
                    ########## make sure to switch to 0th tab to do next search --->>> otherwise this will go in infinite loop as
                    ########## as the 0th window search is next step and if code did not find the xpath on open window then it throws error
                    
                    ###START:  this try catch block is for handling the error - sometimes the webpage clicks the link and open new page. to handle that error code is written again to hit the query search 
                    """
                    
                    try:
                        driver.switch_to.window(window_handles[0])
                        time.sleep(5)
                        
                        try:
                            """
                            ### check if the search window is at different page- if yes then click on return button to come back on the main page
                            ### or the second method is to search the query again and continue the process 
                            """
                            
                            xpath_return = '//*[@title="Search results"]/div[@class="overlayBackButtonText"]'
                            if (driver.find_element(By.XPATH,xpath_return) ):
                                
                                #########======START: process to search the querry again 
                                
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
                                 
                                #########======END: process to search the querry again 
                                
                                 
                        except:pass 
                        
                    except:pass 
                    """
                    ###END:  this try catch block is for handling the error - sometimes the webpage clicks the link and open new page. to handle that error code is written again to hit the query search 
                    """
                     
            """
            #### update the pagecheck value to true so that the while condition will pass and code exit from the loop 
            """
            pagecheck = True
                     
                    
        except:
            print("--------Finding query_search_ for top 10 results on page-----------")
            pagecheck=False
            """
            ###Error Handling: this checkpoint is if the code is in infinite loop but the search for 10 items is already completed
            """
            if (i ==10):
                pagecheck == True
                
            
    #print("-------- query_search_ for top 10 results on page found-----------",Query)
    
    time.sleep(2)   

    
    # ################################################################################
    # # Print the dictionary to confirm its content
    # print("Dictionary Data:")
    # print(places_data)
    
    # """
    # # Convert the dictionary into a DataFrame for saving as Excel
    # # Convert the nested dictionary to a format that pandas can handle
    # """
    
    # df = pd.DataFrame({
    #     'Place Name': [my_data_dict["place_Name"]],
    #     'User Reviews': [", ".join(my_data_dict["user_reviews"])],  # Join list of reviews into a single string
    #     'Place Location': [my_data_dict["place_location"]],
    #     'User Ratings': [my_data_dict["ratings"]],
    #     'Image Path': [my_data_dict["img_path_of_location"]],
    #     'Wikipedia Information': [my_data_dict["wikipedia_result"]]
    # })
    

    # ################################################################################
    # # Get the current date and time for the file name
    # current_datetime = datetime.now().strftime("%Y-%m-%d")
    
    # # Define the file name with the current date and time
    # file_name = f"wandersphere_result_{current_datetime}.xlsx"
    
    # ########## Save the DataFrame to an Excel file  ##########
    
    # # Check if the Excel file already exists
    # if os.path.exists(file_name):
    #     # If the file exists, load the existing data
    #     with pd.ExcelWriter(file_name, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
    #         # Read the existing content of the file
    #         existing_df = pd.read_excel(file_name, sheet_name='Sheet1')
    
    #         # Append the new data (the new data is always in `df`)
    #         updated_df = pd.concat([existing_df, df], ignore_index=True)
    
    #         # Save the updated data back to the same sheet
    #         updated_df.to_excel(writer, index=False, sheet_name='Sheet1')
    
    #     print(f"Data has been appended to the existing file: {file_name}")
        
    # else:
    #     # If the file does not exist, create a new file and save the data
    #     df.to_excel(file_name, index=False, sheet_name='Sheet1')
    #     print(f"Data has been saved to a new file: {file_name}")
    
    
    # ################################################################################
    # print(f"Data has been saved to {file_name}")
    
    
    
page_url = "https://www.bing.com/maps?cp=40.753474%7E-73.982309&lvl=13.1"        
getSearch_Data(page_url)        
        





















########### Draft code ########

     
# def save_img_from_url(image_url):    
#    This function is written to save the top rank result images into folder 
     
#     # Extract the actual image URL from the query string in the URL
#     from urllib.parse import urlparse, parse_qs
    
#     parsed_url = urlparse(image_url)
#     image_url_actual = parse_qs(parsed_url.query)['mediaurl'][0]
    
#     # Send a GET request to the image URL
#     response = requests.get(image_url_actual)
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Specify the local file path where you want to save the image
#         local_image_path = "image.jpg"
        
#         # Write the image content to the file
#         with open(local_image_path, "wb") as file:
#             file.write(response.content)
        
#         print("Image saved successfully!")
#     else:
#         print("Failed to retrieve the image. HTTP Status code:", response.status_code)
    
 
# # URL of the image
# image_url = "https://www.bing.com/images/search?view=detailV2&mediaurl=https%3a%2f%2flh3.googleusercontent.com%2fp%2fAF1QipNBjb_dPTpx-33DnSHKhcDGK0fpeOiG7_iwjIIp%3ds1600-w592&expw=474&exph=469&cbid=OLC.ghS4sT%2B0U6XnAw480x360&cbn=local&idpp=local&thid=OLC.ghS4sT%2B0U6XnAw480x360&ypid=YN873x9751698798145775288&useBFPR=0&eeptype=PhotoGroups&dataGroup=local:datagroup.photos&PhotoGroupName=AllPhotos&PageTag=AllPhotos&selectedIndex=0&id=OLC.ghS4sT%2B0U6XnAw480x360&q=City%20Hall%20Park%20Visitor%20Information%20Center%20top%20park%20tourist%20attractions%20country%20united%20states&pseg=HomeAndProfessionalServices&noidpclose=0&FORM=LOCIMG"
# save_img_from_url(image_url)    

    

# def get_country_names():    
    
#     ##_--------get the country names -------------
#     import pycountry
#     # Function to list all countries
#     def list_all_countries():
#         countries = [country.name for country in pycountry.countries]
#         return countries
    
#     # Example usage
#     all_countries = list_all_countries()
#     print(all_countries)  # Print the first 10 countries
    
#     #_--------get the country names -------------


   
   

    
    
    
    
    
    
    # ### checkpoint to get the wikipedia details 
    # pagecheck=False
    # while pagecheck!=True:
    #     try: 
            
            
    #         # Open a new tab using JavaScript
    #         driver.execute_script("window.open('');")
            
    #         # Switch to the new tab
    #         driver.switch_to.window(driver.window_handles[1])
            
    #         # Open a URL in the new tab
    #         driver.get("https://www.facebook.com/")
                
             
            
    #         # # Open a new tab and switch to it
    #         # driver.switchTo().newWindow(WindowType.TAB)
             
    #         # pagecheck=False
    #         # while pagecheck!=True:
    #         #     if "wait" in driver.title:
    #         #         driver.refresh()
    #         #     elif "Wikipedia" in driver.title:
    #         #         print('title found now move to next step')
    #         #         pagecheck=True
             
    #         # #### get location details from wikipedia page
    #         # xpath =  '//*[@id="mw-content-text"]/div[1]/p[2]'
    #         # query_search_result = driver.find_element(By.XPATH,xpath)
    #         # if (query_search_result):
    #         #     pagecheck = True
    #         #     print("-------- query_search_result found----------")
            
            
    #     except:
    #         print("--------Finding if search result on page-----------")
    #         pagecheck=False
    # #print("-------- Quesry Search search result on page found-----------",Query)
    
    
    
    
     
        
        
        