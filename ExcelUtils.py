#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:27:49 2024

@author: komalwavhal
"""
 
import pandas as pd
import os 
 
class ExcelOperations() :
    
    def dataprocessing(self, top_5_images_filepath):
    
        
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(top_5_images_filepath)
        
        # Display the first few rows of the dataframe
        print(df.head())
        
        print(df['Place Name']) 
        
        # Function to generate Google Maps link
        def generate_maps_link(place_name):
            return f"https://www.google.com/maps?q={place_name.replace(' ', '+')},+New+York"
        
        # Create the list of tuples
        images_info = [
            (row['Place Name'], row['Image URL'], generate_maps_link(row['Place Name']))
            for _, row in df.iterrows()
        ]
        
        # # Output the generated list of tuples
        # for item in images_info:
        #     print(item)
         
        
        print(images_info)
        return(images_info)
        

    
    
    def read_flickrdata(self, file_path ,  Parent_Folder_Path  ):
  
        error_status = 'Error Occured'
        
        try:
            print( ' ------->>>>> read the excel file execution started '  )
                 
            print('read and perform data processing ') 
             
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
            top_10_image_info = top_10_images[['Place Name', 'Image URL', 'Sentiment Score', 'Views', 'Comment Count']]
                
            top_10_images_filepath = os.path.join(Parent_Folder_Path, "top_10_images.xlsx") 
            # Optionally, you can save this data into a new Excel file
            top_10_image_info.to_excel(top_10_images_filepath, index=False)
            
            print("Top 5 images data saved to 'top_10_images.xlsx'")
            
            df = pd.read_excel('top_5_images.xlsx')
            
            # for i in range(0,5):
            #     print(df['Place Name'][i] , ' - ', df['Image URL'][i]) 
            	 
                
            # os.remove(file_path)  
            # os.remove(top_5_images_filepath)
                    
            error_status = 'Error Not Occured'
            print('error_status',error_status)
        except:
            print('inside else - Excel function')
            error_status = 'Error Occured'
        
        return(error_status)
            




        
        

    
        
    