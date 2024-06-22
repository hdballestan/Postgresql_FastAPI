import os
from fastapi import FastAPI, HTTPException
import psycopg2
import pandas as pd
from pydantic import BaseModel
from typing import Dict
from constants import DATABASE_CONFIG, QUERY



app = FastAPI()
app.title = "Primer Punto"
app.version = "1.0.0"

def get_record_count_psycopg2() -> int:
    """
    Connect to the PostgreSQL database using psycopg2 and fetch the record count.

    Returns:
        int: The total number of records in the specified table.
    """
    connection = None
    try:
        connection = psycopg2.connect(**DATABASE_CONFIG)
        cursor = connection.cursor()
        cursor.execute(QUERY)
        record_count = cursor.fetchone()[0]
        return record_count
    except psycopg2.Error as e:
        error_message = f"PSycopg2 error: {e}"
        raise HTTPException(status_code=500, detail=error_message)
    except Exception as e:
        error_message = f"Error: {e}"
        raise HTTPException(status_code=500, detail=error_message)
    finally:
        if connection:
            connection.close()

def get_record_count_pandas() -> int:
    """
    Connect to the PostgreSQL database using pandas and fetch the record count.

    Returns:
        int: The total number of records in the specified table.
    """
    connection = None
    try:
        connection_string = (
            f"postgresql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}"
            f"@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['dbname']}"
        )
        df = pd.read_sql_query(QUERY, connection_string)
        record_count = df.iloc[0, 0]
        return record_count
    except pd.errors.EmptyDataError as e:
        # Handle empty query result
        error_message = "Empty result from query."
        raise HTTPException(status_code=404, detail=error_message)
    except pd.errors.ParserError as e:
        # Handle pandas parser error
        error_message = f"Pandas parser error: {e}"
        raise HTTPException(status_code=500, detail=error_message)
    except Exception as e:
        # Handle other exceptions
        error_message = f"Error: {e}"
        raise HTTPException(status_code=500, detail=error_message)
    finally:
        if connection:
            connection.close()
            
@app.get('/')
def health():
    """Healthy path"""
    return {'status': 'Healthy'}

@app.get("/record_count_psycopg2", response_model=Dict[str, int])
def read_record_count_psycopg2():
    """
    Get the total number of records in the specified table using psycopg2.

    Returns:
        dict: A dictionary containing the total number of records.
    """
    count = get_record_count_psycopg2()
    return {"total_records": count}

@app.get("/record_count_pandas", response_model=Dict[str, int])
def read_record_count_pandas():
    """
    Get the total number of records in the specified table using pandas.

    Returns:
        dict: A dictionary containing the total number of records.
    """
    count = get_record_count_pandas()
    return {"total_records": count}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
