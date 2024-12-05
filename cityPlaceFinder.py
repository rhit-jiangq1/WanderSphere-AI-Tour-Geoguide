import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from openpyxl import load_workbook
from urllib.parse import urlparse, parse_qs
from tkinter import ttk
import pandas as pd

def save_img_from_url(image_url, save_path="image.jpg"):
    # This function saves the image from the URL to the local file system.
    parsed_url = urlparse(image_url)
    if 'mediaurl' in parse_qs(parsed_url.query):
        # For URLs like those from Wikipedia with mediaurl parameter
        image_url_actual = parse_qs(parsed_url.query)['mediaurl'][0]
    else:
        # If the URL is already the direct image URL
        image_url_actual = image_url

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(image_url_actual, headers=headers)

    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        print("Image saved successfully!")
    else:
        print(f"Failed to retrieve the image. HTTP Status code: {response.status_code}")

# Function to create and display Tkinter GUI with the place details read by Excel
def display_places_from_excel(excel_file):
    df = pd.read_excel(excel_file)
    
    # Start setting up tkinter
    root = tk.Tk()
    root.title("Places and Images")
    
    # Build the frame with headers and real contents
    frame = tk.Frame(root)
    frame.pack(expand=True, fill=tk.BOTH)
    
    # Create Header frame and setup pads
    header_frame = tk.Frame(frame)
    header_frame.pack(fill=tk.X, padx=10, pady=10)
    tk.Label(header_frame, text="Place Name", width=30, anchor="w").pack(side=tk.LEFT, padx=10)
    tk.Label(header_frame, text="Reviews", width=20, anchor="w").pack(side=tk.LEFT, padx=10)
    tk.Label(header_frame, text="Location", width=40, anchor="w").pack(side=tk.LEFT, padx=10)
    tk.Label(header_frame, text="Ratings", width=15, anchor="w").pack(side=tk.LEFT, padx=10)
    tk.Label(header_frame, text="Image", width=15, anchor="w").pack(side=tk.LEFT, padx=112)

    
    for index, row in df.iterrows():
        # Go throught df read the data
        place_name = row["Place Name"]
        reviews = row["User Reviews"]
        location = row["Place Location"]
        ratings = row["User Ratings"]
        image_url = row["Image Path"]
        image_path = f"image_{index}.jpg"
        save_img_from_url(image_url, image_path)

        # Pack all info in a single row
        place_frame = tk.Frame(frame)
        place_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(place_frame, text=place_name, width=30, anchor="w").pack(side=tk.LEFT, padx=10)
        tk.Label(place_frame, text=reviews, width=20, anchor="w").pack(side=tk.LEFT, padx=10)
        tk.Label(place_frame, text=location, width=40, anchor="w").pack(side=tk.LEFT, padx=10)
        tk.Label(place_frame, text=ratings, width=30, anchor="w").pack(side=tk.LEFT, padx=10)
        
        image = Image.open(image_path)
        # Size of the image is too big, need resize to a smaller version
        image.thumbnail((100, 100))
        img_tk = ImageTk.PhotoImage(image)
        
        # Need a image label to display the image
        image_label = tk.Label(place_frame, image=img_tk)
        image_label.image = img_tk
        image_label.pack(side=tk.LEFT, padx=10)
    
    root.mainloop()

excel_file = "wandersphere_result_2024-12-05.xlsx"
display_places_from_excel(excel_file)
