import pandas as pd
import tkinter as tk
from tkinter import ttk

# Step 1: Read the Excel file using pandas
# Step 2: Filter the cities by the selected country


def get_cities_by_country(df, country_name, file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path, engine='openpyxl')
      
    # Filter the DataFrame based on the country name
    filtered_df = df[df['country'] == country_name]
    return filtered_df[['city', 'lat', 'lng']]

# Step 3: Update the cities dropdown when a country is selected
def update_city_dropdown(event, country_name, df, city_combobox, lat_entry, lng_entry):
    # Get the cities for the selected country
    cities_df = get_cities_by_country(df, country_name)
    
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
def update_lat_lng(event, df, city_name, lat_entry, lng_entry):
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

# Step 5: Create the Tkinter GUI
def create_gui(df):
    # Initialize the main window
    root = tk.Tk()
    root.title("Select Country and City")

    # Create the country dropdown
    country_names = df['country'].dropna().unique().tolist()
    country_combobox = ttk.Combobox(root, values=country_names)
    country_combobox.set("Select a country")
    country_combobox.pack(padx=10, pady=10)

    # Create the city dropdown
    city_combobox = ttk.Combobox(root, values=[])
    city_combobox.set("Select a city")
    city_combobox.pack(padx=10, pady=10)

    # Create entry fields for latitude and longitude
    lat_label = tk.Label(root, text="Latitude:")
    lat_label.pack(padx=10, pady=5)
    lat_entry = tk.Entry(root)
    lat_entry.pack(padx=10, pady=5)

    lng_label = tk.Label(root, text="Longitude:")
    lng_label.pack(padx=10, pady=5)
    lng_entry = tk.Entry(root)
    lng_entry.pack(padx=10, pady=5)

    # Update city dropdown when country is selected
    country_combobox.bind("<<ComboboxSelected>>", 
                          lambda event: update_city_dropdown(event, country_combobox.get(), df, city_combobox, lat_entry, lng_entry))

    # Update latitude and longitude when city is selected
    city_combobox.bind("<<ComboboxSelected>>", 
                       lambda event: update_lat_lng(event, df, city_combobox.get(), lat_entry, lng_entry))

    # Run the Tkinter event loop
    root.mainloop()

# Main script
if __name__ == "__main__":
    # Replace with the path to your Excel file
    file_path = "worldcities.xlsx"  # Specify your Excel file path here


    # Step 1: Read the Excel file
    df = read_excel(file_path)

    # Step 2: Create the Tkinter GUI with the country names and city selection functionality
    create_gui(df)
 