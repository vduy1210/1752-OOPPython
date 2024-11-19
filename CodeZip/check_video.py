import tkinter as tk
from tkinter import Listbox
from video_library import list_all, show_video_info_by_id 
from pg_utils import PostgresDB as pgdb
from tkinter import messagebox


class CheckVideo(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("900x500")
        self.title("Check Video")
        self.setup_ui_for_CVW()

    def setup_ui_for_CVW(self): # Define a method to set up the UI elements for Check Video window
        list_video_btn = tk.Button(self, text="List All Video", width=15, height=2, command=self.list_all_and_clicked)
        list_video_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_number_label = tk.Label(self, text="Enter Video Number", width=18, height=2)
        enter_number_label.grid(row=0, column=1, padx=10, pady=10)

        self.enter_number_entry = tk.Entry(self, width=3)
        self.enter_number_entry.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(self, text="Check Video", width=15, height=2, command=self.check_video)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.listbox_left = Listbox(self, width=48, height=12)
        self.listbox_left.grid(row=2, column=0, columnspan=2, rowspan=20, pady=8)

        self.listbox_right = Listbox(self, width=24, height=8)
        self.listbox_right.grid(row=2, column=3, columnspan=2)

    def list_all_and_clicked(self):  # Define a method to list all videos and perform a click action
        self.list_all_videos()  # Call the method to list all videos
        self.clicked()  # Call the clicked method

    def list_all_videos(self):  # Define a method to list all available videos
        self.listbox_left.delete(0, tk.END)  # Clear the left listbox
        videos = list_all()  # Get a list of all videos
        for video in videos:  # Loop through each video
            self.listbox_left.insert(tk.END, video)  # Insert each video into the left listbox

    def check_video(self):  # Define a method to check video details based on entered video ID
        self.listbox_right.delete(0, tk.END)  # Clear the right listbox
        video_id = self.enter_number_entry.get()  # Get the entered video ID

        valid_video = self.is_valid_video_id(video_id)  # Check if the video ID is valid

        if valid_video:  # If video ID is valid
            video_info = show_video_info_by_id(video_id)  # Get video info by ID
            for info in video_info:  # Loop through each info and insert into right listbox
                self.listbox_right.insert(tk.END, info)
        else:
            messagebox.showerror("Error", "Invalid video number!")  # Show error if the video ID is invalid

        return

    def is_valid_video_id(self, video_id):  # Define a method to check if the video ID exists in the database
        db = pgdb()  # Create an instance of PostgresDB
        video = db.select_video(video_id)  # Get the video based on the ID from the database
        return video is not None  # Return True if video exists in database, otherwise False

    def clicked(self):  # Define a method to display a label when the list video button is clicked
        lbl = tk.Label(self, text="List Video Button was clicked!")
        lbl.grid(row=22, column=0, columnspan=2)