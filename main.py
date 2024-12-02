import tkinter as tk
from instagram_api import InstagramAPI
from place_finder_app import PlaceFinderApp

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"  # I don't have a Instagram account for Instagram API yet

def main():
    root = tk.Tk()
    api = InstagramAPI(ACCESS_TOKEN)
    app = PlaceFinderApp(root, api)
    root.mainloop()

if __name__ == "__main__":
    main()
