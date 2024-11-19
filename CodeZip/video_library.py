from pg_utils import PostgresDB as pgdb

class Video:
    def __init__(self, id) -> None:
        self.id = id
        self.name = None
        self.director = None
        self.rate = 0
        self.play_count = 0
        self.file_path = None
        self.get_video_info_by_id()

    def get_video_info_by_id(self):
        db = pgdb()
        row = db.select_video(self.id)
        if row:
            self.name = row[1]
            self.director = row[2]
            self.rate = row[3]
            self.play_count = row[4]
            self.file_path = row[5]
            
            # Format the video information into a string
            video_info = f"Name: {self.name}, Director: {self.director}, Rate: {self.rate}, Plays: {self.play_count}"
            return video_info
        
        return "No information found" 

    def get_name(self):
        return self.name

    def get_director(self):
        return self.director

    def get_rating(self):
        return self.rate

    def set_rating(self, rate_value):
        self.rate = rate_value
        self.update_video_to_db()

    def get_play_count(self):
        return self.play_count

    def increment_play_count(self, increase_num=1):
        self.play_count += increase_num
        self.update_video_to_db()

    def update_video_to_db(self):
        db = pgdb()
        row_tuple = (self.id, self.name, self.director, self.rate, self.play_count, self.file_path)
        db.update_row(row_tuple)

def list_all():
    db = pgdb()
    all_videos = db.select_all_videos()
    video_names = [
        f"{row[0]} {row[1]} - {row[2]} {'*' * int(row[3])}" for row in all_videos
    ]
    return video_names

def show_video_info_by_id(id):
    db = pgdb()
    picked_video = db.select_video(id)
    return picked_video[1:5] if picked_video else None

def show_name(id):
    db = pgdb()
    picked_video = db.select_video(id)
    return picked_video[1] if picked_video else None

def increment_play_count(video_name):
    db = pgdb()
    video = db.select_video_by_name(video_name)

    if video:
        play_count = video[4] + 1
        db.update_row((video[0], video[1], video[2], video[3], play_count, video[5]))
    else:
        print(f"Video with name '{video_name}' not found.")

def update_rating(video_id, new_rating):
    db = pgdb()
    video = db.select_video(video_id)

    if video:
        db.update_row((video_id, video[1], video[2], new_rating, video[4], video[5]))
    else:
        print(f"Video with ID '{video_id}' not found.")
