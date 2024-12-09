#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 22:33:25 2024

@author: komalwavhal
"""


import pandas as pd
from urllib.parse import quote_plus
import flickrapi
import requests
from PIL import Image
from io import BytesIO
from textblob import TextBlob
import openpyxl
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import webbrowser
from urllib.parse import quote_plus


# Set your Flickr API key and secret
api_key = '707492d24c42391a563cddc2bf5e619f'
secret_api_key = '52cb54347825468a'

flickr = flickrapi.FlickrAPI(api_key, secret_api_key, format='parsed-json')

# Define your search parameters (latitude, longitude, and accuracy)
lat = 40.712776
lon = -74.005974
accuracy = 11  # Accuracy level (1 to 16)

# Create a new Excel workbook and worksheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'Flickr Photo Data'

# Add header row
headers = [
    'Photo ID', 'Image URL', 'Place Name','Comment','Comment Count', 'Tags', 'Views', 
     'Sentiment', 'Sentiment Score','Ranking Score'
]

ws.append(headers)

# Search for photos near the given latitude and longitude
photo_list = flickr.photos.search(lat=lat, lon=lon, accuracy=accuracy, per_page=200)

# Check if photos are found
if 'photos' in photo_list:
    photos = photo_list['photos']['photo']
    print(f"Found {len(photos)} photos nearby.")

    # Iterate through each photo to get more details
    # print(photos)
    
    
    for photo in photos:
        
        
        sentiment = ''
        Views = ''
        Count = '' 
        
        title = ''
        
        photo_id = photo['id']
        title = photo['title']
         
        Place_Name = title 
        
        photo_info = flickr.photos.getInfo(photo_id=photo_id)
         
        Tags		= ' , '.join([tag['_content'] for tag in photo_info['photo']['tags']['tag']])
        Views		= photo_info['photo']['views']
        Count		= str(photo_info['photo']['comments']['_content'])
             
        photo_url = f"https://farm{photo['farm']}.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}.jpg"
        

        # print(f"\nTitle: {title}")
        # print(f"Photo URL: {photo_url}")
        
        # Fetch comments for this photo
        comments = flickr.photos.comments.getList(photo_id=photo_id)
        
        
        ################### Get Comments ###########################
        
        comment_list = [] 

        data = comments
        try:
            
            # Initialize an empty list to hold the extracted comment information 
            
            comments_info = []
            comment_List = []
            
            # Extract the comments from the data
            comments_data = data['comments']['comment']
            
            # Initialize an empty list to hold the extracted comment information
            # Loop through each comment and collect the necessary information
            for comment in comments_data:
                comment_info = {
                    'Author Name': comment['authorname'],  # Name of the user who commented
                    'Comment': comment['_content'],  # The actual comment text
                    'Permalink': comment['permalink'],  # Link to the comment
                    'Date Created': comment['datecreate'],  # Date the comment was created (UNIX timestamp)
                    'Real Name': comment.get('realname', 'N/A')  # Real name of the user (if available)
                }
                comments_info.append(comment_info)
            
            # Display the extracted comment information
            for info in comments_info:
                # print(f"Author: {info['Author Name']}")
                # print(f"Comment: {info['Comment']}")
                # print(f"Permalink: {info['Permalink']}")
                # print(f"Date Created: {info['Date Created']}")
                # print(f"Real Name: {info['Real Name']}")
                # print("-" * 80)
                comment_List.append(info['Comment'])
            
         

        except:
            # print('No comments available.')
            comment_List.append('No Commets available')
            
        # print('Comment for photo -  ', comment_List)
        
        cmt = []
        cmt.append(' '.join(comment_List))
        # print(cmt)
    
        sentiment = ''
        sentiment_scores = ''
        string_cmt = ''
        if not( cmt == ['No Commets available']):
            string_cmt = str(' '.join(comment_List))
            blob = TextBlob(string_cmt)
            sentiment = 'Neutral'
            if blob.sentiment.polarity > 0:
                sentiment = 'Positive'
            elif blob.sentiment.polarity < 0:
                sentiment = 'Negative'
            sentiments = str(sentiment)
            sentiment_scores  = str(blob.sentiment.polarity)
        else:
            sentiments = (' ')
            sentiment_scores = (' ')
             
            
        Comment		= string_cmt  
                
 
        # Prepare the data to save into Excel 
        ws.append([
                photo_id, 
                photo_url,
                Place_Name,
                Comment, 
                Count,
                Tags,
                Views,
                sentiment,
                sentiment_scores  
            ])
         
        # print("photo_id", photo_id) 
        # print("photo_url", photo_url)
        # print("title", Place_Name)
        # print("Comment", Comment) 
        # print("Tags", Tags)
        # print("Views", Views)
        # print("Count", Count)
        # print("Sentiment", sentiment)
        # print("Sentiment_Score", sentiment_scores)      
                 
        # print( ' ') 
        # print( ' ') 
            
else:
    print('No photos found.')

# Save the workbook
wb.save('flickr_photo_data.xlsx')
print('Data saved to flickr_photo_data.xlsx')
