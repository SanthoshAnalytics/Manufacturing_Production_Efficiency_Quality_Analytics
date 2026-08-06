import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "root"
password = quote_plus("Aaraay%40277")   # Encodes @ correctly
host = "localhost"
port = 3306
database = "manufacturing_analytics"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)