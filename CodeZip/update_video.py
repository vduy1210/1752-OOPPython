import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import video_library as lib
import font_manager as fonts
from video_library import update_rating, show_video_info_by_id,list_all, show_video_info_by_id
import tkinter.scrolledtext as tkst
from pg_utils import PostgresDB as pgdb


class UpdateVideos(tk.Toplevel):  
    def __init__(self, parent):  
        super().__init__(parent)  
        self.geometry("600x270")  
        self.title("Update Videos")  
        self.setup_for_UVA()  

    def setup_for_UVA(self):  # Method to set up the GUI elements
        self.video_number_label = Label(self, text="Enter Video Number:")  # Create a label for entering video number
        self.video_number_label.grid(row=1, column=0, padx=10, pady=10)  # Place the label in a grid layout

        self.video_number_entry = Entry(self, width=10)  # Create an entry widget for video number input
        self.video_number_entry.grid(row=1, column=1, padx=10, pady=10)  # Place the entry widget in a grid layout

        self.rating_label = Label(self, text="Enter New Rating:")  # Create a label for entering new rating
        self.rating_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")  # Place the label in a grid layout with sticky 'W'

        self.rating_entry = Entry(self, width=10)  # Create an entry widget for new rating input
        self.rating_entry.grid(row=2, column=1, padx=10, pady=10)  # Place the entry widget in a grid layout

        self.list_right_txt = tkst.ScrolledText(self, width=25, height=7, wrap="none")  # Create a scrolled text widget
        self.list_right_txt.grid(row=0, column=5, rowspan=3, padx=10, pady=10)  # Place the scrolled text widget in a grid layout, occupying multiple rows

        self.update_button = Button(self, text="Update Video", command=self.update_video)  # Create a button to update video
        self.update_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)  # Place the button in a grid layout, spanning multiple columns

        self.update_video_btn = Button(self, text="Check Video", command=self.check_video)  # Create a button to check video
        self.update_video_btn.grid(row=3, column=5, padx=10, pady=10)  # Place the button in a grid layout

    def update_video(self):  # Method to update video information
        video_number = self.video_number_entry.get()  # Get the entered video number
        new_rating = self.rating_entry.get()  # Get the entered new rating

        if not video_number or not new_rating:  # Check if both video number and new rating are entered
            messagebox.showerror("Error", "Please enter both Video Number and New Rating.")  # Show an error message if either field is empty
            return  

        try:  # Try to update video information
            video_info = show_video_info_by_id(video_number)  # Get video information by ID
            if video_info:  # If video information exists
                video_name = video_info[0]  # Get video name from video_info
                play_count = video_info[3]  # Get play count from video_info
                update_rating(video_number, new_rating)  # Update the rating of the video

                # Show a success message with video details
                messagebox.showinfo("Success", f"Video Name: {video_name}\nNew Rating: {new_rating}\nPlay Count: {play_count}")
            else:
                messagebox.showerror("Error", "Invalid Video Number. Video not found.")  # Show an error if the video is not found
        except Exception as e:  # Catch any exceptions
            messagebox.showerror("Error", f"An error occurred: {e}")  # Show an error message with the specific error

    def check_video(self):  # Method to check video information
        self.list_right_txt.delete('1.0', tk.END)  # Clear the existing content in list_right_txt
        video_id = self.video_number_entry.get()  # Get the entered video ID
        video_info = show_video_info_by_id(video_id)  # Get video information by ID

        if video_info:  # If video information exists
            for info in video_info:  # Loop through video information
                self.list_right_txt.insert(tk.END, f"{info}\n")  # Insert video information into list_right_txt
        else:
            messagebox.showerror("Error", "Invalid Video Number. Video not found.")  # Show an error if the video is not found

if __name__ == "__main__":  
    main = tk.Tk()  
    fonts.configure()  
    app = UpdateVideos(main)  
    main.mainloop()  