import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import json
import os
from psycopg2 import sql

# Load PostgreSQL credentials from JSON file (relative to script location)
creds_path = os.path.join(os.path.dirname(__file__), "postgres_creds.json")
with open(creds_path) as f:
    creds = json.load(f)

def create_database_if_not_exists():
    # Open a connection and set autocommit at connection creation
    conn = psycopg2.connect(dbname="postgres", user=creds["user"], password=creds["password"], host=creds["host"], port=creds["port"])
    try:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", (creds['dbname'],))
            if not cur.fetchone():
                cur.execute(sql.SQL('CREATE DATABASE {}').format(sql.Identifier(creds["dbname"])))
    finally:
        conn.close()

create_database_if_not_exists()

# reads the data from the web as a CSV
file_url = "https://ashfaq-nsclc-dataset.s3.us-east-1.amazonaws.com/dei-bootcamp/Most+popular+1000+Youtube+videos.csv"
df = pd.read_csv(file_url)

# create a connection to postgresql
connection_string = f"postgresql://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['dbname']}"
engine = create_engine(connection_string)

df.to_sql(name="kaggle_1000_youtube_videos", con=engine, if_exists="replace", index=False)