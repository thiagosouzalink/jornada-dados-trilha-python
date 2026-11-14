import os
from pathlib import Path
from lib.classes.abstract_source import AbstractDataSource

class FilesSources(AbstractDataSource):
    def __init__(self):
        self.previous_files = []
        self.start()
            
    def create_path(self):
        current_directory = Path(__file__).resolve().parent.parent.parent
        self.folder_path = current_directory / 'data' / 'extension_files'
        self.folder_path.mkdir(parents=True, exist_ok=True)
            
    def check_for_new_files(self):
        current_files = [
            file.name for file in self.folder_path.iterdir() 
            if file.is_file()
        ]

        new_files = [
            file for file in current_files
            if file not in self.previous_files 
        ]

        if new_files:
            print("New files detected:", new_files)
            # Update the list of previous files
            self.previous_files = current_files
        else:
            print("No new files detected.")

    def get_data(self):
        pass
    
    def transform_data_to_df(self):
        pass

    def save_data(self):
        pass

    def show_files(self):
        print(self.previous_files)

    def start(self):
        self.create_path()