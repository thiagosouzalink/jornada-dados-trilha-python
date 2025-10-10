from pathlib import Path


FOLDER_ROOT = Path(__file__).parent.parent

def get_measurements_file() -> Path:
    measurements_file: Path = FOLDER_ROOT / "data" / "measurements.txt"
    if not measurements_file.exists():
        raise FileNotFoundError(f"O arquivo {measurements_file} não existe.")
    return measurements_file

