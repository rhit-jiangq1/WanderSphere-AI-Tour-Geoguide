#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 18:09:06 2024

@author: komalwavhal
"""


 
import flickrapi
import requests
import json
from PIL import Image
from io import BytesIO
import flickrapi
import requests
from PIL import Image
from io import BytesIO

your_flickr_api_key = '707492d24c42391a563cddc2bf5e619f'
secret_api_key = '52cb54347825468a'
    
api_key = your_flickr_api_key
secret_api_key = secret_api_key
flickr = flickrapi.FlickrAPI(api_key, secret_api_key)

lat = 48.83417
lon = 2.221111
photo_list = flickr.photos.search(api_key=api_key, lat=lat, lon=lon, accuracy=11, format='parsed-json')

# print(photo_list) 

# Set your Flickr API key and secret
api_key = '707492d24c42391a563cddc2bf5e619f'
secret_api_key = '52cb54347825468a'

flickr = flickrapi.FlickrAPI(api_key, secret_api_key, format='parsed-json')

# Define your search parameters (latitude, longitude, and accuracy)
lat = 40.712776
lon = -74.005974

accuracy = 11  # Accuracy level (1 to 16)

# Search for photos near the given latitude and longitude
photo_list = flickr.photos.search(lat=lat, lon=lon, accuracy=accuracy, per_page=10)

# Check if photos are found
if 'photos' in photo_list:
    photos = photo_list['photos']['photo']
    print(f"Found {len(photos)} photos nearby.")

    # Iterate through each photo to get more details
    for photo in photos:
        photo_id = photo['id']
        title = photo['title']
        photo_url = f"https://farm{photo['farm']}.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}.jpg"
        
        print(f"\nTitle: {title}")
        print(f"Photo URL: {photo_url}")

        # Fetch comments for this photo
        comments = flickr.photos.comments.getList(photo_id=photo_id)
        
        try:
            # Check if there are comments in the response
            if 'comments' in comments and 'comment' in comments['comments']:
                comment_texts = [comment['text'] for comment in comments['comments']['comment']]
                print(f"Comments: {', '.join(comment_texts)}")
            else:
                 
                print("No comments available.")
        except:pass 
        
        # Fetch photo location (geo-data)
        print(photo_id)
                 
        # Get photo information (views, favorites, title, description, tags, etc.)
        photo_info = flickr.photos.getInfo(photo_id=photo_id)
        
        # Extracting the relevant features from the response
        photo_details = {
            'id': photo_info['photo']['id'],
            'title': photo_info['photo']['title']['_content'],
            'description': photo_info['photo']['description']['_content'],
            'tags': [tag['_content'] for tag in photo_info['photo']['tags']['tag']],
            'views': photo_info['photo']['views'], 
            'comments_count': photo_info['photo']['comments']['_content'],
             
        }
        
        # Fetch comments for this photo
        comments = flickr.photos.comments.getList(photo_id=photo_id)
         
        
        # Print the photo details
        print(photo_details)
        
         
        
        # location = flickr.photos.geo.getLocation(photo_id=photo_id)
        # if 'photo' in location:
        #     geo = location['photo']['location']
        #     latitude = geo['latitude']
        #     longitude = geo['longitude']
        #     print(f"Location: Latitude = {latitude}, Longitude = {longitude}")
        # else:
        #     print("No geolocation data available.")
        
        # # Optionally display the image
        # # img_data = requests.get(photo_url).content
        # # img = Image.open(BytesIO(img_data))
        # # img.show()

else: 

    print(' ')
    print(' ')
    print("No photos found in this area.")
    print(' ')
    print(' ')













print(' ')

print(' Stop Code Now')

print(' ')