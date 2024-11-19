import tkinter as tk
from tkinter import scrolledtext, messagebox
from video_library import list_all  
import font_manager as fonts

class Search(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x460")
        self.title("Director & Video Finder")
        self.setup_for_SW()  

    def setup_for_SW(self):
        # Creating and placing UI elements
        list_video_btn = tk.Button(self, text="List All Video", width=15, height=2, command=self.list_all_and_clicked)
        list_video_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_number_label = tk.Label(self, text="Enter name of Director or Video name", width=30, height=2)
        enter_number_label.grid(row=0, column=2, padx=10, pady=10)

        self.enter_number_entry = tk.Entry(self, width=30)
        self.enter_number_entry.grid(row=0, column=3)

        search_btn = tk.Button(self, text="Search", width=15, height=2, command=self.search_video)
        search_btn.grid(row=0, column=4, padx=10, pady=10)

        # Creating scrolled text widgets to display videos
        self.list_left_txt = scrolledtext.ScrolledText(self, width=48, height=12, wrap="none")
        self.list_left_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.list_right_txt = scrolledtext.ScrolledText(self, width=48, height=12, wrap="none")
        self.list_right_txt.grid(row=2, column=3, columnspan=2, sticky="NW", padx=10, pady=10)

    def list_all_and_clicked(self):
        self.list_all_videos()  # Call method to list all videos
        self.clicked()  # Call method to indicate button click

    def list_all_videos(self):
        self.list_left_txt.delete(1.0, tk.END)  # Clear existing content in the left scrolled text widget
        videos = list_all()  # Get all video information
        # Display each video in the left scrolled text widget
        for video in videos:
            self.list_left_txt.insert(tk.END, video + "\n")

    def search_video(self):
        search_term = self.enter_number_entry.get().lower()
        if not search_term:
            messagebox.showinfo("Search Error", "Please enter a search term.")
            return

        search_results = self.search_by_name(search_term)  # Perform search based on the entered term
        if not search_results:
            messagebox.showinfo("Search Results", "No matching videos/directors found.")
            return

        self.display_search_results(search_results)  # Display search results in the right scrolled text widget

    def search_by_name(self, search_term):
        all_videos = list_all()  # Get the list of all videos
        search_results = []
        # Check each video for a match with the search term (case insensitive)
        for video in all_videos:
            if search_term in video.lower():
                search_results.append(video)  # Append matching videos to search_results
        return search_results

    def display_search_results(self, search_results):
        self.list_right_txt.delete(1.0, tk.END)  # Clear existing content in the right scrolled text widget
        # Display each search result in the right scrolled text widget
        for result in search_results:
            self.list_right_txt.insert(tk.END, result + "\n")

    def clicked(self):
        lbl = tk.Label(self, text="List Video Button was clicked!")  # Indicate that the button was clicked
        lbl.grid(row=22, column=0, columnspan=2)

if __name__ == "__main__":
    app = Search()
    fonts.configure()  
    app.mainloop()  
