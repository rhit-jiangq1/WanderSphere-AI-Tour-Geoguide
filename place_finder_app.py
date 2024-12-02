import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
import io

class PlaceFinderApp:
    """
    Class for create the UI and manage user interactions for the Instagram Place Finder
    """
    def __init__(self, root, api):
        self.root = root
        self.api = api

        # Call setup_ui()
        self.root.title("Instagram Place Finder")
        self.setup_ui()

    def setup_ui(self):
        """
        Initialize the UI setups (search + result frame)
        """
        # Search Frame
        search_frame = ttk.Frame(self.root, padding="10")
        search_frame.pack(fill="x", padx=10, pady=10)

        city_label = ttk.Label(search_frame, text="Enter City Name:")
        city_label.pack(side="left", padx=5)

        self.city_entry = ttk.Entry(search_frame, width=30)
        self.city_entry.pack(side="left", padx=5)

        # Search Button
        search_button = ttk.Button(search_frame, text="Search", command=self.search_places)
        search_button.pack(side="left", padx=5)

        # Refresh Button
        refresh_button = ttk.Button(search_frame, text="Refresh", command=self.reset_search)
        refresh_button.pack(side="left", padx=5)

        # Results Frame
        self.results_frame = ttk.Frame(self.root, padding="10")
        self.results_frame.pack(fill="both", expand=True, padx=10, pady=10)


    def search_places(self):
        """
        Search for places based on the city entered
        """
        city_name = self.city_entry.get().strip()
        if not city_name:
            messagebox.showerror("Input Error", "Please enter a city name.")
            return

        try:
            places = self.api.search_city_places(city_name)
            self.display_results(places)
        except RuntimeError as e:
            messagebox.showerror("Error", str(e))


    def reset_search(self):
        """
        Clear the input and results.
        """
        self.city_entry.delete(0, tk.END)
        for widget in self.results_frame.winfo_children():
            widget.destroy()


    def display_results(self, places):
        """
        Display search results in the UI
        """
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        if not places:
            messagebox.showinfo("No Results", "No places found for this city.")
            return

        for place in places:
            place_name = place.get("name", "Unknown")
            place_id = place.get("id", "")

            place_label = ttk.Label(self.results_frame, text=place_name)
            place_label.pack(anchor="w", pady=2)

            view_photos_btn = ttk.Button(self.results_frame, text="View Photos",
                                         command=lambda pid=place_id: self.show_photos(pid))
            view_photos_btn.pack(anchor="w", pady=2)


    def show_photos(self, place_id):
        """
        Show photos for the selected place in a new window
        """
        try:
            photos = self.api.fetch_place_photos(place_id)
        except RuntimeError as e:
            messagebox.showerror("Error", str(e))
            return

        if not photos:
            messagebox.showinfo("No Photos", "No photos found for this place.")
            return

        # New Photo Window
        photo_window = tk.Toplevel(self.root)
        photo_window.title("Photos")

        # Save photo to local
        save_photos_button = ttk.Button(photo_window, text="Save Photos",
                                        command=lambda: self.save_photos(photos))
        save_photos_button.pack(pady=5)

        for photo in photos:
            image_url = photo.get("media_url")
            if image_url:
                try:
                    img_data = requests.get(image_url).content
                    img = Image.open(io.BytesIO(img_data))
                    img = img.resize((200, 200), Image.ANTIALIAS)
                    img_tk = ImageTk.PhotoImage(img)
                    img_label = ttk.Label(photo_window, image=img_tk)
                    img_label.image = img_tk
                    img_label.pack(pady=5)
                except Exception as e:
                    messagebox.showerror("Error", f"Image Error: {e}")


    def save_photos(self, photos):
        """
        Save photos to the local file
        """
        try:
            for i, photo in enumerate(photos):
                image_url = photo.get("media_url")
                if image_url:
                    img_data = requests.get(image_url).content
                    with open(f"place_photo_{i+1}.jpg", "wb") as f:
                        f.write(img_data)
            messagebox.showinfo("Success", "Photos saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Save Error: {e}")
