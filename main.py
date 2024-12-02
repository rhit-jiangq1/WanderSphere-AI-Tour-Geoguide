import tkinter as tk
from instagram_api import InstagramAPI
from place_finder_app import PlaceFinderApp

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"  # I don't have a Facebook Meta Developer Account account for Instagram API yet. The website told me should be done by 12/3/2024

def main():
    root = tk.Tk()
    api = InstagramAPI(ACCESS_TOKEN)
    app = PlaceFinderApp(root, api)
    root.mainloop()

if __name__ == "__main__":
    main()
