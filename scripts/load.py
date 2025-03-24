import pandas as pd
from sqlalchemy import create_engine

def load_data():
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/covid_db")
    df = pd.read_csv("covid_cleaned.csv")
    df.to_sql("covid_stats", engine, if_exists="replace", index=False)
    print("Data loaded successfully!")

if __name__ == "__main__":
    load_data()
