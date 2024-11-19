import psycopg2 as pg  # Import the psycopg2 library to interact with PostgreSQL
import config  # Import the config module
import sys

class PostgresDB:
    def __init__(self, conn_string=config.DB_CONN) -> None:
        self.conn_string = conn_string  # Set the connection string, defaulting to DB_CONN from config
        self.conn = None  # Initialize connection object as None
        self.cursor = None  # Initialize cursor object as None
        return

    def connect(self):
        try:
            # Establish a connection to the database
            self.conn = pg.connect(self.conn_string)  # Connect using the provided connection string
            # Create a cursor to perform database operations
            self.cursor = self.conn.cursor()  # Create a cursor object
        except Exception as e:
            # Print an error message if an exception occurs during connection
            print(f"Got exception on DB connection: {e}")
            # Raise the exception to handle it further
            raise e

    def close(self):
        # Close the cursor and connection to the database
        self.cursor.close()  # Close the cursor
        self.conn.close()  # Close the database connection
        return

    def select_all_videos(self):
        # Retrieve all video records from the 'videos' table
        self.connect()  # Connect to the database
        query_string = "SELECT * FROM videos"  # Define the SQL query
        self.cursor.execute(query_string)  # Execute the query
        results = self.cursor.fetchall()  # Fetch all results
        self.close()  # Close the connection
        return results  # Return fetched results

    def select_video(self, id):
        # Retrieve a specific video record by ID from the 'videos' table
        self.connect()  # Connect to the database
        query_string = "SELECT * FROM videos WHERE id=%s;"  # Define the SQL query with a parameter placeholder
        self.cursor.execute(query_string, (id,))  # Execute the query with the provided ID
        results = self.cursor.fetchall()  # Fetch all results
        self.close()  # Close the connection
        return results[0] if results else None  # Return the first result if available, otherwise None

    def select_video_by_name(self, name):
        # Retrieve a specific video record by name from the 'videos' table
        self.connect()  # Connect to the database
        query_string = "SELECT * FROM videos WHERE video_name=%s;"  # Define the SQL query with a parameter placeholder
        self.cursor.execute(query_string, (name,))  # Execute the query with the provided name
        results = self.cursor.fetchall()  # Fetch all results
        self.close()  # Close the connection
        return results[0] if results else None  # Return the first result if available, otherwise None

    def update_row(self, row_tuple):
        # Update a specific row in the 'videos' table with new data
        self.connect()  # Connect to the database
        query_string = f"UPDATE videos \
                        SET video_name = '{row_tuple[1]}', \
                            director = '{row_tuple[2]}', \
                            rate = {row_tuple[3]}, \
                            play_count = {row_tuple[4]}, \
                            file_path = '{row_tuple[5]}' \
                        WHERE id = {row_tuple[0]};"  # Define the SQL update query with values from the tuple
        self.cursor.execute(query_string)  # Execute the update query
        self.conn.commit()  # Commit the changes to the database
        self.close()  # Close the connection
        return  # Return from the method
