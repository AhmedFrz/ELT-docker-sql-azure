import pandas as pd
from sqlalchemy import create_engine

# reads the data from teh web as a CSV
file_url = "https://ashfaq-nsclc-dataset.s3.us-east-1.amazonaws.com/dei-bootcamp/Most+popular+1000+Youtube+videos.csv"
df = pd.read_scv(file_url)

# create a connection to postgresql
connection_string = "postgresql://postgres:postgres@localhost:5433/kaggle"

engine = create_engine(connection_string)

# turn engine into actual connection
connection = engine.connect()

# write the data to the database
df.to_sql (name="kaggle_1000_youtube_videos", con=connection, if_exists="replace")







# https://hub.docker.com/_/postgres/tags?name=12.&page=3