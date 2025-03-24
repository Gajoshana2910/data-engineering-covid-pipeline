import pandas as pd

def transform_data():
    df = pd.read_csv("covid_data.csv")
    df = df[["Country", "TotalConfirmed", "TotalDeaths", "TotalRecovered"]]
    df.dropna(inplace=True)
    df.to_csv("covid_cleaned.csv", index=False)
    print("Data transformed successfully!")

if __name__ == "__main__":
    transform_data()
