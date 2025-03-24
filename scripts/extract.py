import requests
import pandas as pd

def extract_data():
    url = "https://api.covid19api.com/summary"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data["Countries"])
        df.to_csv("covid_data.csv", index=False)
        print("Data extracted successfully!")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    extract_data()
