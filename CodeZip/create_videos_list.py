import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
from video_library import show_name, increment_play_count
from tkinter import messagebox
import font_manager as fonts

class VideoListApp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("940x430")
        self.title("Create Video List")
        self.setup_for_VLA()

    def setup_for_VLA(self):
        header_lbl = tk.Label(self, text="Select all videos you want to add to a new list", font=("Helvetica", 13))
        header_lbl.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        self.list_left_txt = tkst.ScrolledText(self, width=48, height=12, wrap="none")
        self.list_left_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.list_right_txt = tkst.ScrolledText(self, width=48, height=12, wrap="none")
        self.list_right_txt.grid(row=2, column=3, sticky="NW", padx=10, pady=10)


        enter_lbl = tk.Label(self, text="Enter Video Number")
        enter_lbl.grid(row=1, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(self, width=3)
        self.input_txt.grid(row=1, column=2, padx=10, pady=10)

        create_video_list_btn = tk.Button(self, text="Reset playlist", command=self.reset_playlist) 
        create_video_list_btn.grid(row=5, column=1, padx=10, pady=10)

        play_playlist_btn = tk.Button(self, text="Play playlist", command=self.play_playlist)
        play_playlist_btn.grid(row=5, column=3, padx=10, pady=10)


        self.add_to_playlist_btn = tk.Button(self, text="Add Video to Playlist", command=self.add_to_playlist)
        self.add_to_playlist_btn.grid(row=1, column=3, padx=10, pady=10)

            # Displaying all videos from the library in the left scrolled text widget
        videos_from_library = lib.list_all()  # Retrieve a list of all available videos
        for video in videos_from_library:  # Iterate through each video in the list
            self.list_left_txt.insert(tk.END, video + "\n")  # Insert each video into the left scrolled text widget


    def add_to_playlist(self):
        # Add a video to the playlist in the right scrolled text widget
        video_number = self.input_txt.get()  # Get the video number from the input field
        video_name = show_name(video_number)  # Retrieve the name of the video using the video number
        message = "Can not find your video"
        if message in self.list_right_txt.get("1.0", tk.END):  # Check if a specific message exists in the playlist
            self.list_right_txt.delete("1.0", tk.END)  # Clear the playlist if the message exists
        if video_name:  # If the video name is found
            self.list_right_txt.insert(tk.END, video_name + "\n")  # Add the video to the playlist in the right scrolled text widget
        else:
            messagebox.showerror("Error", "Your video number is not found. Please check video number again.")  # Show an error message if the video number is not found


    def reset_playlist(self):
         # Clear the content of the right scrolled text widget (playlist)
        self.list_right_txt.delete("1.0", tk.END)  # Delete all content in the right scrolled text widget


    def play_playlist(self):
        # Simulate playing the videos in the playlist and increment their play counts
        playlist_content = self.list_right_txt.get("1.0", tk.END)  # Retrieve the content of the playlist
        if playlist_content.strip() == "":  # Check if the playlist is empty
            messagebox.showinfo("Info", "There are no videos in the playlist. Please add videos to the playlist first.")  # Show an info message if the playlist is empty
            return

        playlist_lines = playlist_content.split("\n")  # Split the playlist content into individual lines
        for line in playlist_lines:
            if line.strip() != "":  # Check if the line is not empty
                increment_play_count(line)  # Simulate playing the video and increment its play count

        messagebox.showinfo("Info", "Simulated playlist. Increased play counts.")  # Show an info message after simulating the playlist


if __name__ == "__main__":
    main = tk.Tk()
    fonts.configure()
    app = VideoListApp(main)
    app.mainloop()      