#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:56:36 2024

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


# Load the Excel file
file_path = 'flickr_photo_data.xlsx'  # Replace with your actual file path
df = pd.read_excel(file_path)

# Ensure the data is loaded correctly
# print(df.head())

# Sort the dataset based on the relevant columns:
# - Sentiment Score (higher is better)
# - Views (higher is better)
# - Comment Count (higher is better)

# We will assume that sentiment score, views, and comment count columns exist and are numeric.

# Convert the necessary columns to numeric (in case they are not already)
df['Sentiment Score'] = pd.to_numeric(df['Sentiment Score'], errors='coerce')
df['Sentiment Score'] = pd.to_numeric(df['Sentiment Score'], errors='coerce')
df['Views'] = pd.to_numeric(df['Views'], errors='coerce')
df['Comment Count'] = pd.to_numeric(df['Comment Count'], errors='coerce')
 
# Normalize the columns to combine the scores in a weighted manner.
# You can adjust the weights based on importance: here we just use equal weights for simplicity.

df['Ranking Score'] = df['Sentiment Score'] * 0.5 + df['Views'] * 0.3 + df['Comment Count'] * 0.2

# Sort by the 'Ranking Score' and get the top 5
top_10_images = df.sort_values(by='Ranking Score', ascending=False).head(10)

# Print the top 5 images and their URLs
top_5_image_info = top_10_images[['Place Name', 'Image URL', 'Sentiment Score', 'Views', 'Comment Count']]
  

# Optionally, you can save this data into a new Excel file
top_5_image_info.to_excel('top_10_images.xlsx', index=False)

print("Top 5 images data saved to 'top_10_images.xlsx'")

df = pd.read_excel('top_10_images.xlsx')

images_info = []


for i in range(0,10):
   
    place_name = df['Place Name'][i] 
    image_url = df['Image URL'][i]
	 
    # URL encode the place name for the Google Maps search URL
    google_map_url = f"https://www.google.com/maps?q={quote_plus(place_name)}"
    
    # Append to images_info list
    images_info.append((place_name, image_url, google_map_url))

# Print the generated images_info dataset
print(images_info)



    
import os
os.remove('flickr_photo_data.xlsx')  
os.remove('top_10_images.xlsx')
    









# Function to load and display the image

 
# Function to load and display the image
def display_image(image_name, image_url, google_map_link, row, col, checkbuttons):
    try:
        # Fetch image from the URL
        response = requests.get(image_url)
        if response.status_code == 200:
            # Open the image using Pillow
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            
            # Resize image to fit within the window (optional)
            img = img.resize((200, 200))  # Adjusted size for 5 images per row
            
            # Convert the image for Tkinter compatibility
            img_tk = ImageTk.PhotoImage(img)
            
            # Create labels to display the Google Map link (above the image)
            def open_map():
                webbrowser.open(google_map_link)

            label_map = tk.Label(root, text="View on Google Maps", fg="blue", bg='#FFFFFF', cursor="hand2", font=("calibri", 15))
            label_map.grid(row=row*4, column=col, padx=10, pady=5)
            label_map.bind("<Button-1>", lambda e: open_map())  # Bind the click event to open the map link
            
            # Create the image label
            label_image = tk.Label(root, image=img_tk)
            label_image.image = img_tk  # Keep a reference to avoid garbage collection
            label_image.grid(row=row*4+1, column=col, padx=10, pady=10)
            
            # Create the image name label (below the image)
            label_name = tk.Label(root, text=image_name, fg="black", bg='#FFFFFF', font=("calibri", 12), wraplength=200)
            label_name.grid(row=row*4+2, column=col, padx=10, pady=10)

            # Create checkbox for the image (below the image name)
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(root, fg="black", bg='#FFFFFF', text=" ", variable=var)
            checkbox.grid(row=row*4+3, column=col, padx=10, pady=5)

            # Store the checkbox state and the place name in the list
            checkbuttons.append((var, image_name))  # Store place_name (not link)

            root.configure(background='#FFFFFF') 

        else:
            print(f"Error: Unable to fetch image {image_name}")
    except Exception as e:
        print(f"Failed to load image {image_name}: {str(e)}")

# Function to generate the Google Map itinerary based on selected checkboxes
def generate_itinerary(checkbuttons):
    # Collect the selected locations (place names) based on the checkbox state
    selected_locations = [place_name for var, place_name in checkbuttons if var.get()]

    if not selected_locations:
        messagebox.showinfo("No Selection", "Please select at least one place to generate the itinerary.")
        return

    # Create Google Maps URL with the selected locations as stops
    base_url = "https://www.google.com/maps/dir/"
    destination_url = base_url + "/".join([quote_plus(location) for location in selected_locations])

    # Open the generated itinerary in the browser
    webbrowser.open(destination_url)

# Create the Tkinter window
root = tk.Tk()
root.title("Image Display with Google Map Itinerary")

# # Define the images and their URLs along with Google Maps links
# images_info = [
#     ("Washington Square Park", "https://farm66.staticflickr.com/65535/54182441139_e85c2ac8b9.jpg", "https://www.google.com/maps?q=Washington+Square+Park,+New+York"),
#     ("DSC08821-2", "https://farm66.staticflickr.com/65535/54178502827_4f8e1ca852.jpg", "https://www.google.com/maps?q=DSC08821-2,+New+York"),
#     ("NYC-DSC00659-2", "https://farm66.staticflickr.com/65535/54185324095_a8042bf796.jpg", "https://www.google.com/maps?q=NYC-DSC00659-2,+New+York"),
#     ("Pre-Thanksgiving Balloon Inflation Parade - Fall 2024-28", "https://farm66.staticflickr.com/65535/54187786639_e03b6b10b1.jpg", "https://www.google.com/maps?q=Pre-Thanksgiving+Balloon+Inflation+Parade,+New+York"),
#     ("Billionaire Row to the North", "https://farm66.staticflickr.com/65535/54179966866_fd8b1a3f85.jpg", "https://www.google.com/maps?q=Billionaire+Row,+New+York"),
#     ("Park", "https://farm66.staticflickr.com/65535/54182441139_e85c2ac8b9.jpg", "https://www.google.com/maps?q=Washington+Square+Park,+New+York"),
#     ("Newport", "https://farm66.staticflickr.com/65535/54178502827_4f8e1ca852.jpg", "https://www.google.com/maps?q=DSC08821-2,+New+York"),
#     ("NYC", "https://farm66.staticflickr.com/65535/54185324095_a8042bf796.jpg", "https://www.google.com/maps?q=NYC-DSC00659-2,+New+York"),
#     ("New York", "https://farm66.staticflickr.com/65535/54187786639_e03b6b10b1.jpg", "https://www.google.com/maps?q=Pre-Thanksgiving+Balloon+Inflation+Parade,+New+York"),
#     ("Hoboken", "https://farm66.staticflickr.com/65535/54179966866_fd8b1a3f85.jpg", "https://www.google.com/maps?q=Billionaire+Row,+New+York")
# ]

# List to store checkbox variables and their corresponding place names (not links)
checkbuttons = []

# Display all the images with their names, Google Maps links, and checkboxes
for index, (image_name, image_url, google_map_link) in enumerate(images_info):
    row = index // 5  # Determine the row number (5 images per row)
    col = index % 5   # Determine the column number (5 images per row)
    display_image(image_name, image_url, google_map_link, row, col, checkbuttons)

# Add a "Generate Google Map Itinerary" button to generate a single itinerary
generate_button = tk.Button(root, text="Generate Google Map Itinerary",fg= 'Black', bg = '#FFFFFF',font=('calibri',15,'bold'), command=lambda: generate_itinerary(checkbuttons))
generate_button.grid(row=(len(images_info)//5)*4+1, column=0, columnspan=5, pady=20)

# Start the Tkinter event loop
root.mainloop()




    