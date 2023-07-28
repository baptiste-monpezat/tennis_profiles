"""doc"""

import pandas as pd 
import requests
from src import constants as const 

def get_data():
    """get data from the website"""
    for name, url in const.TABLE_URL_DICT.items():
        response = requests.get(url, headers=const.HEADERS)
        df = pd.read_html(response.content)[4]
        df.to_csv(f"data/{name}.csv", index=False)
        print(f"Saved {name}.csv")

if __name__ == "__main__":
    get_data()