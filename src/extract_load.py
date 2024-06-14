import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# Get enviroment variables
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_SCHEMA = os.getenv('DB_SCHEMA')

database_url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(database_url)

def convert_csv_to_df(csv_name:str):
    df = pd.read_csv(csv_name, encoding="ISO-8859-1")
    df.rename(columns={"artist(s)_name" : "artist_name"}, inplace=True)
    return df

def load_to_postgres(df, db_schema="public"):
    df.to_sql("kaggle_popular_spotify_songs", engine, if_exists="replace", index=False, schema=db_schema)
    print(f"The dataset has been loaded into the '{db_schema}' / Supabase-PostgreSQL database.")

if __name__ == "__main__":
    df = convert_csv_to_df("data\popular_spotify_songs.csv")
    load_to_postgres(df, db_schema=DB_SCHEMA)