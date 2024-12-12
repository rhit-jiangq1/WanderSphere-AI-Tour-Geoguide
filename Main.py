#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:31:12 2024

@author: komalwavhal
"""
 
#try:
#    import docx
#except:
#    os.system('python -m pip install -i python-docx')
#    import docx
   
import tkinter.scrolledtext as tkscrolled
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.scrolledtext as tkscrolled
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename
import threading
from time import sleep 
import subprocess
import time
import sys
import tkinter, sys
from tkinter import scrolledtext
import time
from pathlib import Path   
from tkinter import filedialog
import io
import threading     
import tkinter as tk  
from tkinter import messagebox
from PIL import Image, ImageTk    
from tkinter import messagebox as msg   
import datetime
from tkinter import ttk 
import tkinter as tk
#import Config
import tkinter as tk
from tkinter import ttk
import shutil
from datetime import datetime
#from win32com.shell import shell, shellcon
LARGEFONT =("Verdana", 35) 
#import pyautogui
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import webbrowser
from urllib.parse import quote_plus
import pandas as pd 

class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
    
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {} 
        
        for F in (StartPage, Page1): 
            frame = F(container, self)  
            self.frames[F] = frame 
            frame.grid(row = 0, column = 0, sticky ="nsew")
            
        self.show_frame(StartPage)
    
    # to display the current frame passed as  parameter
    def show_frame(self, cont): 
    
        frame = self.frames[cont]
        frame.tkraise() 
            
        try:
            ### for Windows users
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            print(desktop)
            Parent_Folder_Path = desktop + "/AAI_551_Project_Repository"
            print(Parent_Folder_Path)
        
        except: 
            ### for Mac users
            desktop = os.path.expanduser("~/Desktop")
            desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
            Parent_Folder_Path = desktop + "/AAI_551_Project_Repository"
            print(Parent_Folder_Path)
            
        Parent_Folder_Path = Parent_Folder_Path
        

# first window frame startpage 
class StartPage(tk.Frame):

	def display_text(self, text,tag):

		self.text.tag_config('Error', background="white", foreground="red",font=('calibri',12))
		self.text.tag_config('Normal', background="white",foreground="#819ec4",font=('calibri',12))

		if (tag == 'Error') : 
			self.text.insert(INSERT, text,'Error')
			
		if (tag == 'Normal') : 
			self.text.insert(INSERT, text,'Normal')
			 
		self.text.see("end")  

 
    
	def __init__(self, parent, controller): 
        
		win_user = 0
		import os
		try:
            ### for Windows users
		    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
		    print(desktop)
		    Parent_Folder_Path = desktop + "/AAI_551_Project_Repository"
		    print(Parent_Folder_Path)
        
		except: 
		    win_user = 1            
            ### for Mac users
		    desktop = os.path.expanduser("~/Desktop")
		    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
		    Parent_Folder_Path = desktop + "/AAI_551_Project_Repository"
		    print(Parent_Folder_Path)
            
		Parent_Folder_Path = Parent_Folder_Path
         
		if win_user == 0:		 
		    Img_Path = Parent_Folder_Path + '\\Images'      
		    userManual_Button_imgFilePath = (Img_Path+ "\\UserManual.png") 
		    imgFilePath =  (Img_Path+ "\\pic-11.png")  
		    AFFIRM_ICON_imgFilePath =   (Img_Path+ "\\AFFIRM_ICON.png")
		    userManual_Button_imgFilePath = (Img_Path+ "\\UserManual.png") 
        
		else:
		    Img_Path = Parent_Folder_Path + '//Images'     
		    userManual_Button_imgFilePath = (Img_Path+ "//UserManual.png") 
		    imgFilePath =  (Img_Path+ "//pic-11.png")  
		    AFFIRM_ICON_imgFilePath =   (Img_Path+ "//AFFIRM_ICON.png")
		    userManual_Button_imgFilePath = (Img_Path+ "//UserManual.png") 
            
		print('Img_Path',Img_Path)

 

		tk.Frame.__init__(self, parent)
		  
		##Background Image 
		img = Image.open(imgFilePath)

		photo = ImageTk.PhotoImage(img)
		lab1 = ttk.Label(self,image=photo)
		lab1.pack()
		lab1.place(x=0)
		lab1.image = photo        
   
 
        #####affirm_Button_image    
		affirm_Button_image = Image.open(AFFIRM_ICON_imgFilePath) 
		photo = ImageTk.PhotoImage(affirm_Button_image)        
		affirm_Button = tk.Button(self,image=photo,command= lambda : controller.show_frame(Page1)) ###,bg = "white", bd = 0
		affirm_Button.place(x=667,y=420)        
		affirm_Button.image = photo  
        
          
		self.configure(background='#FFFFFF')

# second window frame page1
class Page1(tk.Frame):
      
    def domain_changed_1(self,event):
        self.mainGetData_1 = list()
        self.mainGetData_1.append(self.domainselected_1.get())
		 	
        
    def browsefunc_1(self): 
         
        win_user = 0
        import os
        try:
            ### for Windows users
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            print(desktop)
            Parent_Folder_Path = desktop + "/AAI_551_Project_Repository"
            print(Parent_Folder_Path)
        
        except: 
            win_user = 1            
            ### for Mac users
            desktop = os.path.expanduser("~/Desktop")
            desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
            Parent_Folder_Path = desktop + "/AAI_551_Project_Repository"
            print(Parent_Folder_Path)
            
          
        Parent_Folder_Path = Parent_Folder_Path
        User_Manual_Path = Parent_Folder_Path +'\\' + 'User_Manual' 
         
        export_File_path =  User_Manual_Path
        path = export_File_path
        path = os.path.realpath(path)
        os.startfile(path)
        
         
        
    
    def get_cities_by_country(self, country_name, file_path):
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path, engine='openpyxl')
          
        # Filter the DataFrame based on the country name
        filtered_df = df[df['country'] == country_name]
        return filtered_df[['city', 'lat', 'lng']]
    
    # Step 3: Update the cities dropdown when a country is selected
    def update_city_dropdown(self,event,   country_name, file_path, city_combobox, lat_entry, lng_entry):
        
        # Get the cities for the selected country
        cities_df = self.get_cities_by_country(country_name, file_path)
        
        # Update the city dropdown options
        city_combobox['values'] = cities_df['city'].tolist()
        city_combobox.set('')  # Clear current selection
        
        # Clear latitude and longitude
        lat_entry.delete(0, tk.END)
        lng_entry.delete(0, tk.END)
    
        # Re-enable the latitude and longitude fields in case they were previously disabled
        lat_entry.config(state='normal')
        lng_entry.config(state='normal')
    
    # Step 4: Update latitude and longitude when a city is selected
    def update_lat_lng(self,event, file_path, city_name, lat_entry, lng_entry):
        
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path, engine='openpyxl')
        
        # Get the latitude and longitude of the selected city
        city_info = df[df['city'] == city_name].iloc[0]
        lat_entry.delete(0, tk.END)
        lng_entry.delete(0, tk.END)
        
        # Set latitude and longitude in the entry fields
        lat_entry.insert(0, city_info['lat'])
        lng_entry.insert(0, city_info['lng'])
    
        # Disable the latitude and longitude fields after they are populated
        lat_entry.config(state='disabled')
        lng_entry.config(state='disabled')
        
        
         
        

    def __init__(self, parent, controller):
         
        win_user = 0
        import os
        try:
            ### for Windows users
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            print(desktop)
            Parent_Folder_Path = desktop + "/AAI_551_Project_Repository"
            print(Parent_Folder_Path)
            Img_Path = Parent_Folder_Path + '\\Images'  
            imgFilePath =  (Img_Path+"\\pic-1.png") 
            Bck_Button_imgFilePath = (Img_Path+'\\Bck_Button.png') 
            run_Button_imgFilePath = (Img_Path+'\\run.PNG') 
             
        except: 
            win_user = 1            
            ### for Mac users
            desktop = os.path.expanduser("~/Desktop")
            desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
            Parent_Folder_Path = desktop + "/AAI_551_Project_Repository"
            print(Parent_Folder_Path)
            Img_Path = Parent_Folder_Path + '//Images'  
            imgFilePath =  (Img_Path+"//pic-1.png") 
            Bck_Button_imgFilePath = (Img_Path+'//Bck_Button.png') 
            run_Button_imgFilePath = (Img_Path+'//run.PNG') 
          
        Parent_Folder_Path = Parent_Folder_Path
       
        
        ##------------------------------------------------------------------------------------------------------------
          
        ###-----------------------------------------------------------------------------------------------------------

        		
        tk.Frame.__init__(self, parent)
         
        ##Background Image 
        
        img = Image.open(imgFilePath)
        
        photo = ImageTk.PhotoImage(img)
        lab1 = ttk.Label(self,image=photo)
        lab1.pack()
        lab1.place(x=0)
        lab1.image = photo           
         
          
        #####Bck_Button_image    
        Bck_Button_image = Image.open(Bck_Button_imgFilePath) 
        photo = ImageTk.PhotoImage(Bck_Button_image)        
        Bck_Button = tk.Button(self,image=photo,command= lambda : controller.show_frame(StartPage))  ###,bg = "white", bd = 0
        Bck_Button.place(x=37,y=30)        
        Bck_Button.image = photo  
          
        self.configure(background='#FFFFFF') 
        
        import getpass 
        user = str(getpass.getuser() )
        fullname = ''

        if win_user == 0:	
            print('----------Write down code for windows user name here--------')
        else:	            
            import platform
            sys_owner_fname = ( platform.node().replace("s-MacBook-Pro.local",' ') ).lower()
            print('sys_owner_fname' , sys_owner_fname)
            import getpass
            sys_owner_lastname = str( getpass.getuser() )
            sys_owner_lname = sys_owner_lastname.upper()
            replace_val = str(sys_owner_fname.upper()).strip()
            sys_owner_lname = sys_owner_lname.replace( replace_val,'')
            sys_owner_lname = sys_owner_lname.lower()
            print('sys_owner_lname' , sys_owner_lname)

            fullname = sys_owner_fname + '' + sys_owner_lname
            print(fullname)

         
        
        #### ----------###(Application Logs)---------------------------------- 
        self.text = scrolledtext.ScrolledText(self,wrap = WORD,bg = '#FFFFFF',  height=3, width=46,  font=('calibri',12),relief= 'ridge') 
        self.text.place(x=1000,y=700)
        
        self.configure(background='#FFFFFF') 
          
        
        ###------------------Select dropdown button ------------------------------------------------- 
        
        
        file_path =   os.path.join(Parent_Folder_Path, "worldcities.xlsx")
        df = pd.read_excel(file_path, engine='openpyxl')
        
        # Create the country dropdown
        self.country_names = df['country'].dropna().unique().tolist()
        self.country_combobox = ttk.Combobox(self, values=self.country_names)
        # self.country_combobox.set("Select a country")
        # self.country_combobox.pack(padx=10, pady=120)
        self.country_combobox.place(x=510,y=200)    
    
        ###-----------------------------------------------------------------------------------------
             
        # Create the city dropdown
        self.city_combobox = ttk.Combobox(self, values=[])
        # self.city_combobox.set("Select a city")
        # self.city_combobox.pack(padx=10, pady=70)
        self.city_combobox.place(x=510,y=230)    
        
        ###-----------------------------------------------------------------------------------------
             
        # Create entry fields for latitude and longitude
        self.lat_label = tk.Label(self, text="Latitude:  ", bg = '#FFFFFF', width=9,  font=('calibri',12),relief= 'ridge')
         
        self.lat_label.place(x=810,y=206)    
        
        self.lat_entry = tk.Entry(self)
         
        self.lat_entry.place(x=910,y=200)    
     
        ###-----------------------------------------------------------------------------------------
             
        self.lng_label = tk.Label(self, text="Longitude:", bg = '#FFFFFF', width=9,  font=('calibri',12),relief= 'ridge')
        
        self.lng_label.place(x=810,y=236)    
        
        self.lng_entry = tk.Entry(self)
         
        self.lng_entry.place(x=910,y=230)    
         
        # Update city dropdown when country is selected
        self.country_combobox.bind("<<ComboboxSelected>>",  lambda event: self.update_city_dropdown(event, self.country_combobox.get(),  file_path, self.city_combobox, self.lat_entry, self.lng_entry))
    
        # Update latitude and longitude when city is selected
        self.city_combobox.bind("<<ComboboxSelected>>",  lambda event: self.update_lat_lng(event, file_path, self.city_combobox.get(), self.lat_entry, self.lng_entry))
 
        ###-----------------------------------------------------------------------------------------
                 
        self.Search_label = tk.Label(self, text="Search:     ", bg = '#FFFFFF', width=8,  font=('calibri',12),relief= 'ridge')
        # lng_label.pack(padx=10, pady=6)
        self.Search_label.place(x=810,y=270)   
        
        self.v = tk.IntVar()
        self.Search_label_entry = tk.Entry(self,text=self.v) 
        self.Search_label_entry.place(x=910,y=270)    
        self.v.set(100)  
        
        ###-----------------------------------------------------------------------------------------
        
        #####RUN Automatoin  
        runWanderSphere_image = Image.open(run_Button_imgFilePath) 
        photo = ImageTk.PhotoImage(runWanderSphere_image)        
        button_Export = tk.Button(self,image=photo,command=  self.Execute_speaker_eng)  ###,bg = "white", bd = 0
        button_Export.place(x=610,y=310)        
        button_Export.image = photo  
                  
        ##### ----------###(THIS STYLE FOR THE PROGRESSBAR)----------------------------------
        self.style = ttk.Style(self)
        
        self.style.layout('text.Horizontal.TProgressbar',
        	 [('Horizontal.Progressbar.trough',
        	   {'children': [('Horizontal.Progressbar.pbar',
        					  {'side': 'left', 'sticky': 'ns'})],
        		'sticky': 'nswe'}),
        	  ('Horizontal.Progressbar.label', {'sticky': ''})])   
        self.style.configure('text.Horizontal.TProgressbar', text=' ')
        
        
        self.configure(background='#FFFFFF')     

    def Execute_speaker_eng(self) :  
        # run process in a thread to avoid blocking gui 
        t = threading.Thread(target=self.execute_main)
        t.start()
 
    
    # Function to load and display the image
    def display_image(self, image_name, image_url, google_map_link, row, col, checkbuttons):
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
    
                label_map = tk.Label(self.new_window, text="View on Google Maps", fg="blue", bg='#FFFFFF', cursor="hand2", font=("calibri", 15))
                label_map.grid(row=row*4, column=col, padx=10, pady=5)
                label_map.bind("<Button-1>", lambda e: open_map())  # Bind the click event to open the map link
                
                # Create the image label
                label_image = tk.Label(self.new_window, image=img_tk)
                label_image.image = img_tk  # Keep a reference to avoid garbage collection
                label_image.grid(row=row*4+1, column=col, padx=10, pady=10)
                
                # Create the image name label (below the image)
                label_name = tk.Label(self.new_window, text=image_name, fg="black", bg='#FFFFFF', font=("calibri", 12), wraplength=200)
                label_name.grid(row=row*4+2, column=col, padx=10, pady=10)
    
                # Create checkbox for the image (below the image name)
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(self.new_window, fg="black", bg='#FFFFFF', text=" ", variable=var)
                checkbox.grid(row=row*4+3, column=col, padx=10, pady=5)
    
                # Store the checkbox state and the place name in the list
                checkbuttons.append((var, image_name))  # Store place_name (not link)
    
                self.new_window.configure(background='#FFFFFF') 
    
            else:
                print(f"Error: Unable to fetch image {image_name}")
        except Exception as e:
            print(f"Failed to load image {image_name}: {str(e)}")
    
    # Function to generate the Google Map itinerary based on selected checkboxes
    def generate_itinerary(self, checkbuttons):
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
     
    def display_text(self,text,tag):
 

        self.text.tag_config('Error', background="white", foreground="red",font=('calibri',12))
        self.text.tag_config('Normal', background="white",foreground="#819ec4",font=('calibri',12))

        if (tag == 'Error') : 
            self.text.insert(INSERT, text,'Error')
			
        if (tag == 'Normal') : 
            self.text.insert(INSERT, text,'Normal')
			 
        self.text.see("end")  
 
    def open_new_window(self, images_info):
        
        # Create a new top-level window
        self.new_window = tk.Toplevel(root)
        self.new_window.title("Image Display with Google Map Itinerary")
        
        # Set the size of the new window
        # self.new_window.geometry("300x200")
         
        # List to store checkbox variables and their corresponding place names (not links)
        checkbuttons = []
        
        # Display all the images with their names, Google Maps links, and checkboxes
        for index, (image_name, image_url, google_map_link) in enumerate(images_info):
            row = index // 5  # Determine the row number (5 images per row)
            col = index % 5   # Determine the column number (5 images per row)
            self.display_image(image_name, image_url, google_map_link, row, col, checkbuttons)
        
        # Add a "Generate Google Map Itinerary" button to generate a single itinerary
        generate_button = tk.Button(self.new_window, text="Generate Google Map Itinerary",fg= 'Black', bg = '#FFFFFF',font=('calibri',15,'bold'), command=lambda: self.generate_itinerary(checkbuttons))
        generate_button.grid(row=(len(images_info)//5)*4+1, column=0, columnspan=5, pady=20)
        
        # Start the Tkinter event loop
        # self.new_window.mainloop()
 
        
    def execute_main(self):  
       
        self.text.config(state='normal')
        self.text.delete("1.0" , "end")
        
        import datetime
        now = datetime.datetime.now() 
        x = str(now.strftime("%Y-%m-%d %H:%M:%S"))  
        self.display_text('>>> Project execution started ' + '\n\n'  , 'Normal')
        time.sleep(1)   
        
        
        city_combobox_Selection = ''
    
        try:
            city_combobox_Selection = self.city_combobox.get()
        except: 
            city_combobox_Selection = 'Select option'
             
        print('city_combobox_Selection - ', city_combobox_Selection)
            
            
            
            
        
        country_combobox_Selection = ''
    
        try:
            country_combobox_Selection = self.country_combobox.get()
        except: 
            country_combobox_Selection = 'Select option'
             
        print('country_combobox_Selection - ', country_combobox_Selection)
            
        
        print('lng_entry - ' , self.lng_entry.get())
        print('lat_entry - ' , self.lat_entry.get()) 
        print('cnt - ', self.v.get()  )
            
          
        # ####--(Step - 1: Download the flicker dataset)----
        # Set your Flickr API key and secret
        api_key = '707492d24c42391a563cddc2bf5e619f'
        secret_api_key = '52cb54347825468a'
         
        latitude = str(self.lng_entry.get())
        longitude = str(self.lat_entry.get())
        pagecnt = int(self.v.get()) 
        
        
        
        
        
        ########################################################################################
      
        ##### Importing Custom Libraries for Excel Operations
        from ExcelUtils import ExcelOperations
        objExcelOperations = ExcelOperations() 
        
        from Flickr_data_collection import Flicker_Data_Download
        objFlicker_Data_Download = Flicker_Data_Download(self.display_text) 
         
        error_status = ''
      
        ############################################################################################################################################################################### 
        
        import os
        
        try:
            ### for Windows users
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            print(desktop)
            Parent_Folder_Path = desktop + "/AAI_551_Project_Repository"
            print(Parent_Folder_Path)
        
        except: 
            ### for Mac users
            desktop = os.path.expanduser("~/Desktop")
            desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
            Parent_Folder_Path = desktop + "/AAI_551_Project_Repository"
            print(Parent_Folder_Path)
            
        Parent_Folder_Path = Parent_Folder_Path
          
        # Join various path components
        output_filepath = os.path.join(Parent_Folder_Path, "flickr_photos_with_sentiment.xlsx") 
        top_10_images_filepath = os.path.join(Parent_Folder_Path, "top_10_images.xlsx")
        print(output_filepath)
          
        objExcelOperations = ExcelOperations() 
         
        error_status =  objFlicker_Data_Download.get_flickr_data( api_key, secret_api_key , output_filepath , latitude , longitude ,pagecnt ) 

        if (error_status == 'Error Occured'): 
            self.display_text('>>> Error occured while executing WanderSphere AI Tour Geoguide: A Real-Time Sentiment-Driven Travel Recommendation System' + '\n'  , 'Error')   
              
            self.display_text('>>> Terminating Execution' + '\n'  , 'Error')  
            self.text.config(state='disabled') 
            raise NameError('EXCEL Operation Exception')     
            stopcodehere       
         
        
        #--(Step - 2: read and perform data processing on the flicker dataset)----
        
        error_status = objExcelOperations.read_flickrdata(output_filepath ,  Parent_Folder_Path )
        print(error_status)
        

        if (error_status == 'Error Occured'):
 
            
            self.display_text('>>> Error occured while executing WanderSphere AI Tour Geoguide: A Real-Time Sentiment-Driven Travel Recommendation System' + '\n'  , 'Error')  
            
            self.display_text('>>> Terminating Execution' + '\n'  , 'Error')  
            self.text.config(state='disabled') 
            raise NameError('EXCEL Operation Exception')     
            stopcodehere       
         
            
        ######### Define the images and their URLs along with Google Maps links
        images_info = objExcelOperations.dataprocessing(top_10_images_filepath)
        
        
        ######################  Display Result GUI ##############
        print(images_info)
        self.open_new_window(images_info) 
  
        self.display_text('>>> Project execution completed successfully   '  + '\n\n'  , 'Normal')
        time.sleep(1)   
        try:
            os.remove(top_10_images_filepath)
            os.remove(output_filepath) 
        except:pass 
            
        self.text.config(state='disabled') 
     
 
time.sleep(1)     
root = tkinterApp()

############################################################################
 
#root = tk.Tk()
root.title("WanderSphere AI Tour Geoguide: A Real-Time Sentiment-Driven Travel Recommendation System (Version: 1.0.0)")
root.geometry('1393x769')

root.pack_propagate(0)
root.resizable(0,0)

def OnFocusIn(event):
    if type(event.widget).__name__ == 'WanderSphere AI Tour Geoguide: A Real-Time Sentiment-Driven Travel Recommendation System (Version: 1.0.0)':
        event.widget.attributes('-topmost', False)

root.attributes('-topmost', True)
root.focus_force()
root.bind('<FocusIn>', OnFocusIn)

root.mainloop()

     


