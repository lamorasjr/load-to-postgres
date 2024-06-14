import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Get enviroment variables
DB_USER =
DB_PASSWORD =
DB_HOST = 
DB_PORT =
DB_NAME = 


engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")