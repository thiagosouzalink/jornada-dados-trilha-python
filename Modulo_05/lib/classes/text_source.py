import os
from pathlib import Path
import pandas as pd
from lib.classes.files_sources import FilesSources


class TxtSource(FilesSources):
    def create_path(self):
        current_directory = Path(__file__).resolve().parent.parent.parent
        self.folder_path = current_directory / 'data' / 'txt_files'
        self.folder_path.mkdir(parents=True, exist_ok=True)
            
    def check_for_new_files(self):
        current_files = [
            file.name for file in self.folder_path.iterdir() 
            if file.is_file()
        ]

        new_files = [
            file for file in current_files
            if file not in self.previous_files and file.endswith('.txt')
        ]

        if new_files:
            print("New TXT files detected:", new_files)
            # Update the list of previous files
            self.previous_files = current_files
        else:
            print("No new TXT files detected.")
            self.get_data()

    def get_data(self):
        # Implement getting data from TXT files in the specified folder
        data_frames = []
        for file_path in self.previous_files:
            try:
                path = f'{self.folder_path}/{file_path}'
                data = pd.read_csv(path, sep='\t')  # Assume que os arquivos .txt estão tabulados
                data_frames.append(data)
            except Exception as e:
                print("An error occurred while reading the TXT file:", e)
        if data_frames:
            self.combined_data = pd.concat(data_frames, ignore_index=True)
            print(self.combined_data)
            return self.combined_data
        else:
            return None