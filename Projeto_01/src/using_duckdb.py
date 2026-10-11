from pathlib import Path
import duckdb
import time

def create_duckdb(file_: str):
    duckdb.sql(f"""
        SELECT station,
            MIN(temperature) AS min_temperature,
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperature) AS max_temperature
        FROM read_csv(
            '{file_}', 
            AUTO_DETECT=FALSE, 
            sep=';', 
            columns={{'station':'VARCHAR', 'temperature': 'DECIMAL(3,1)'}}
        )
        GROUP BY station
        ORDER BY station
    """).show()

if __name__ == "__main__":
    import time
    start_time = time.time()
    data_folder = Path(__file__).parent.parent / "data"
    measurements_file = str(data_folder / "measurements.txt")
    create_duckdb(measurements_file)
    took = time.time() - start_time
    print(f"Duckdb Took: {took:.2f} sec")