"""doc"""

import pandas as pd 
import requests
from src import constants as const 

def get_data():
    """get data from the website"""
    df_list = []
    # read from website
    for name, url in const.TABLE_URL_DICT.items():
        response = requests.get(url, headers=const.HEADERS)
        df = pd.read_html(response.content)[4]
        df_list.append(df)
        print(f"Read {name} table")
    # add player id
    all_player_list = pd.concat(
        [df["Player"] for df in df_list], ignore_index=True).unique()
    player_id_dict = {player: i+1 for i, player in enumerate(all_player_list)}
    for df in df_list:
        df["player_id"] = df["Player"].map(player_id_dict)
        df.insert(0, "player_id", df.pop("player_id"))  # to be the first column
    # save to csv
    for name, df in zip(const.TABLE_URL_DICT.keys(), df_list):
        df.to_csv(f"data/{name}.csv", index=False)
        print(f"Saved {name}.csv")

def create_combined_table():
    """create a combined table"""
    df_combined = pd.DataFrame()
    for name in const.TABLE_URL_DICT.keys():
        df = pd.read_csv(f"data/{name}.csv")
        if df_combined.empty:
            df_combined = df
        else:
            df_combined = df_combined.merge(
                df, on=["player_id", "Player", "Matches"], how="outer")
    df_combined.to_csv("data/combined.csv", index=False)


if __name__ == "__main__":
    print("Getting data from website...")
    get_data()
    print("Creating combined table...")
    create_combined_table()