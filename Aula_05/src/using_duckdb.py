import duckdb
import time

from get_file import get_measurements_file

def create_duckdb():
    measurements_file = get_measurements_file()
    duckdb.sql(f"""
        SELECT station,
            MIN(temperature) AS min_temperature,
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperature) AS max_temperature
        FROM read_csv(
            "{measurements_file}", 
            AUTO_DETECT=FALSE, sep=';', 
            columns={{'station':VARCHAR, 'temperature': 'DECIMAL(3,1)'}}
        )
        GROUP BY station
        ORDER BY station
    """).show()

if __name__ == "__main__":
    import time
    start_time = time.time()
    create_duckdb()
    took = time.time() - start_time
    print(f"Duckdb Took: {took:.2f} sec")