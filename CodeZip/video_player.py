import tkinter as tk
import font_manager as fonts
from check_video import CheckVideo
from create_videos_list import VideoListApp
from update_video import UpdateVideos


class Videoplayerapp:  
    def __init__(self, main):  
        
        self.main = main  
        self.main.geometry("850x200")  
        self.main.title("Video Player")  

        
        fonts.configure()

        # Create labels and functional buttons
        self.lbl = tk.Label(main, font=('Arial', 16), text="Select an option by clicking one of the buttons below")  # Create a label
        self.lbl.grid(column=1, row=0)  # Place the label in the main window

        self.check_video_btn = tk.Button(main, text="Check Videos", width=13, height=2, command=self.check_videos)  # Create a button for checking videos
        self.check_video_btn.grid(row=1, column=0, padx=10, pady=10)  # Place the button in the main window

        self.create_video_list_btn = tk.Button(main, text="Create Video List", width=15, height=2, command=self.create_video_list)  # Create a button for creating a video list
        self.create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)  # Place the button in the main window

        self.update_video_btn = tk.Button(main, text="Update Videos", width=13, height=2, command=self.update_video)  # Create a button for updating videos
        self.update_video_btn.grid(row=1, column=2, padx=10, pady=10)  # Place the button in the main window

        

    def check_videos(self):  # Method to handle checking videos
        CheckVideo(self.main)  # Call the CheckVideo class with the main window as an argument

    def create_video_list(self):  # Method to handle creating a video list
        VideoListApp(self.main)  # Call the VideoListApp class with the main window as an argument

    def update_video(self):  # Method to handle updating videos
        UpdateVideos(self.main)  # Call the UpdateVideos class with the main window as an argument

         

if __name__ == "__main__":  
    main = tk.Tk() 
    fonts.configure()  
    app = Videoplayerapp(main)  
    main.mainloop()  

