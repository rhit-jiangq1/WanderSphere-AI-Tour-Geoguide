#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:39:00 2024

@author: komalwavhal
"""

import flickrapi 
from openpyxl import Workbook
from textblob import TextBlob 
import os
import openpyxl
 

# try:
#     import flickrapi
# except:
#     os.system('python -m pip install -i flickrapi')
#     import flickrapi
   

class Flicker_Data_Download():
    
    def __init__(self,display_text):
 
        self.display_text = display_text 
    
    def get_flickr_data(self, api_key, secret_api_key, output_filepath, lat, lon,pagecnt):
        
        error_status = 'Error Occured'
        
        try:
            print( ' ------->>>>> execution started '  )
            
            
            self.display_text('>>> Executing the flickr data download ' + '\n'  , 'Normal')
            
            
            # display_text('>>> Flickr Dataset download started' + '\n'  , 'Normal')
            flickr = flickrapi.FlickrAPI(api_key, secret_api_key, format='parsed-json')
            
            # Define your search parameters (latitude, longitude, and accuracy)
            
            accuracy = 11  # Accuracy level (1 to 16)
            
            # # Search for photos near the given latitude and longitude
            # photo_list = flickr.photos.search(lat=lat, lon=lon, accuracy=accuracy, per_page=pagecnt)
            
            
            # self.display_text('>>> Photos - ' + str(photo_list) + '\n\n'  , 'Normal')
            
            
            # print( ' ------->>>>> photo list  ' , photo_list )
            
             
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
            photo_list = flickr.photos.search(lat=lat, lon=lon, accuracy=accuracy, per_page=pagecnt)
            
            # Check if photos are found
            if 'photos' in photo_list:
                photos = photo_list['photos']['photo']
                print(f"Found {len(photos)} photos nearby.")
            
                # Iterate through each photo to get more details
                # print(photos)
                
                cnt = 1
                for photo in photos:
 
                    self.display_text('>>> Image procecss - ' + str(cnt) + '\n'  , 'Normal')
                    
                    cnt = cnt + 1
                    
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
                            sentiments,
                            sentiment_scores  
                        ])
                     
                
            else:
                print('No photos found.')
            self.display_text('>>> Image extraction part is completed  ' + '\n'  , 'Normal')
     
            
            
         
            # Save the workbook to an Excel file
            wb.save(output_filepath)
            print("Data has been saved to flickr_photos_with_sentiment.xlsx")
            error_status = 'Error Not Occured'
        except:
            error_status = 'Error Occured'
        
        return(error_status)
            
        






