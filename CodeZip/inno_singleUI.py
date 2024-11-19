import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox
from video_library import list_all, show_video_info_by_id, show_name, increment_play_count, update_rating
from pg_utils import PostgresDB as pgdb
import font_manager as fonts


class SingleUI(tk.Tk):
    def __init__(self):  
        super().__init__()  
        self.geometry("1200x500")  
        self.title("SingleUI")  
        fonts.configure()  

        # Create GUI elements
        header_lbl = tk.Label(self, text="Select an option:", font=("Helvetica", 13))  # Create a label for header
        header_lbl.grid(row=0, column=1, columnspan=3, padx=10, pady=10)  # Place the header label in a grid layout

        # Create scrolled text widgets for displaying video information
        self.list_left_txt = tkst.ScrolledText(self, width=48, height=12, wrap="none")  # Left scrolled text widget
        self.list_left_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.list_right_txt = tkst.ScrolledText(self, width=48, height=12, wrap="none")  # Right scrolled text widget
        self.list_right_txt.grid(row=2, column=3, columnspan=3, sticky="NW", padx=10, pady=10)

        # Create entry and buttons for user input and actions
        self.input_lbl = tk.Label(self, text="Enter Video Number")  # Label for entering video number
        self.input_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(self, width=3)  # Entry widget for video number input
        self.input_txt.grid(row=1, column=1, padx=10, pady=10)

        self.check_video_btn = tk.Button(self, text="Check Video", command=self.check_video)  # Button to check video
        self.check_video_btn.grid(row=5, column=0, padx=10, pady=10)

        # More buttons for various actions related to videos and playlist
        self.create_video_list_btn = tk.Button(self, text="Create Video List", command=self.create_video_list)
        self.create_video_list_btn.grid(row=5, column=1, padx=10, pady=10)

        self.add_to_playlist_btn = tk.Button(self, text="Add Video to Playlist", command=self.add_to_playlist)
        self.add_to_playlist_btn.grid(row=5, column=2, padx=10, pady=10)

        self.play_playlist_btn = tk.Button(self, text="Play Playlist", command=self.play_playlist)
        self.play_playlist_btn.grid(row=5, column=3, padx=10, pady=10)

        self.reset_playlist_btn = tk.Button(self, text="Reset ", command=self.reset_playlist)
        self.reset_playlist_btn.grid(row=5, column=4, padx=10, pady=10)

        self.update_video_btn = tk.Button(self, text="Update Video", command=self.update_video)
        self.update_video_btn.grid(row=5, column=5, padx=10, pady=10)

        # New Rating Entry and Label
        self.new_rating_lbl = tk.Label(self, text="Enter New Rating")
        self.new_rating_lbl.grid(row=1, column=3, padx=10, pady=10)

        self.new_rating_entry = tk.Entry(self, width=3)
        self.new_rating_entry.grid(row=1, column=4, padx=10, pady=10)

        self.setup_for_VPA()  # Call the setup_for_VPA method to populate the left scrolled text widget

    def setup_for_VPA(self):  # Method to populate the left scrolled text widget
        # Retrieve all videos from the library
        videos_from_library = list_all()
        # Insert each video's information into the left scrolled text widget
        for video in videos_from_library:
            self.list_left_txt.insert(tk.END, video + "\n")

    def check_video(self):
        # Clear the content of the right scrolled text widget
        self.list_right_txt.delete('1.0', tk.END)
        # Get the video ID from the input text
        video_id = self.input_txt.get()
        # Retrieve video information based on the ID
        video_info = show_video_info_by_id(video_id)
        # If video information exists, display it in the right scrolled text widget; otherwise, show an error message
        if video_info:
            for info in video_info:
                self.list_right_txt.insert(tk.END, f"{info}\n")
        else:
            messagebox.showerror("Error", "Invalid Video Number. Video not found.")

    def create_video_list(self):
        # Get the video number from the input text
        video_number = self.input_txt.get()
        # Get the video name based on the video number
        video_name = show_name(video_number)
        message = "Can not find your video"
        # Check if the video name exists in the right scrolled text widget; if so, remove it
        if message in self.list_right_txt.get("1.0", tk.END):
            self.list_right_txt.delete("1.0", tk.END)
        # If video name exists, display it in the right scrolled text widget; otherwise, show an error message
        if video_name:
            self.list_right_txt.insert(tk.END, video_name + "\n")
        else:
            messagebox.showerror("Error", "Your video number is not found. Please check video number again.")

    def update_video(self):
        # Get the video number and new rating from the respective entry fields
        video_number = self.input_txt.get()
        new_rating = self.new_rating_entry.get()
        # Check if both video number and new rating are provided; if not, show an error message
        if not video_number or not new_rating:
            messagebox.showerror("Error", "Please enter both Video Number and New Rating.")
            return
        try:
            # Retrieve video information based on the video number
            video_info = show_video_info_by_id(video_number)
            # If video information exists, update the rating; if not, show an error message
            if video_info:
                video_name = video_info[0]
                play_count = video_info[3]
                update_rating(video_number, new_rating)
                # Show success message with updated video details
                messagebox.showinfo("Success", f"Video Name: {video_name}\nNew Rating: {new_rating}\nPlay Count: {play_count}")
            else:
                messagebox.showerror("Error", "Invalid Video Number. Video not found.")
        except Exception as e:
            # Show error message if an exception occurs during the update process
            messagebox.showerror("Error", f"An error occurred: {e}")

    def add_to_playlist(self):
        # Get the video number from the input text
        video_number = self.input_txt.get()
        # Get the video name based on the video number
        video_name = show_name(video_number)
        message = "Can not find your video"
        # Check if the video name exists in the right scrolled text widget; if so, remove it
        if message in self.list_right_txt.get("1.0", tk.END):
            self.list_right_txt.delete("1.0", tk.END)
        # If video name exists, display it in the right scrolled text widget; otherwise, show an error message
        if video_name:
            self.list_right_txt.insert(tk.END, video_name + "\n")
        else:
            messagebox.showerror("Error", "Your video number is not found. Please check video number again.")

    def reset_playlist(self):
        # Clear the content of the right scrolled text widget (playlist)
        self.list_right_txt.delete("1.0", tk.END)

    def play_playlist(self):
        # Get the content of the playlist from the right scrolled text widget
        playlist_content = self.list_right_txt.get("1.0", tk.END)
        # Check if the playlist is empty; if so, display an info message
        if playlist_content.strip() == "This list doesn't contain any videos":
            messagebox.showinfo("Info", "There are no videos in the playlist. Please add videos to the playlist first.")
            return
        # Split the playlist into lines and simulate playing videos (increment play counts)
        playlist_lines = playlist_content.split("\n")
        for line in playlist_lines:
            # Check for valid video entries and increment play count for each video
            if line.strip() != "This list doesn't contain any videos" and line.strip() != "":
                increment_play_count(line)
        # Show info message indicating the simulation of increased play counts
        messagebox.showinfo("Info", "Simulated playlist. Increased play counts.")


if __name__ == "__main__":
    app = SingleUI()
    app.mainloop()
