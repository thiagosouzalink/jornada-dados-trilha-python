
import json
from pathlib import Path
from lib.classes.files_sources import FilesSources


class JsonSource(FilesSources):
    def create_path(self):
        current_directory = Path(__file__).resolve().parent.parent.parent
        self.folder_path = current_directory / 'data' / 'json_files'
        self.folder_path.mkdir(parents=True, exist_ok=True)

    def check_for_new_files(self):
        current_files = [
            file.name for file in self.folder_path.iterdir()
            if file.is_file()
        ]

        new_files = [
            file for file in current_files
            if file not in self.previous_files
            and Path(file).suffix == '.json'
        ]

        if new_files:
            print("New files detected:", new_files)
            self.previous_files = current_files
        else:
            print("No new JSON files detected.")
            self.get_data()

    def read_json_file(self, file_path: Path):
        try:
            with file_path.open('r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Erro ao acessar o JSON: {e}")
            return None

    def get_data(self):
        data = []

        for file_name in self.previous_files:
            file_path = self.folder_path / file_name

            if file_path.suffix == '.json' and file_path.is_file():
                json_data = self.read_json_file(file_path)

                if json_data is not None:
                    data.append(json_data)

        print(data)
        return data
