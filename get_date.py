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
    # clean and save to csv
    for name, df in zip(const.TABLE_URL_DICT.keys(), df_list):
        df_clean = clean_data(df)
        df_clean.to_csv(f"data/{name}.csv", index=False)
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


def clean_data(df):
    """clean the data.
    
    For now, it only deletes the percentage sign in the data and convert it to float.
    """
    df_clean = df.copy()
    for col in df_clean.columns:
        if df_clean[col].dtype == "O":
            has_percent = df_clean[col].str.contains("%").any()
            if has_percent:
                df_clean[col] = df_clean[col].astype(str)
                df_clean[col] = df_clean[col].str.replace("%", "")
                df_clean[col] = df_clean[col].astype(float)
                df_clean[col] = df_clean[col].div(100)

    return df_clean

if __name__ == "__main__":
    print("Getting data from website...")
    get_data()
    print("Creating combined table...")
    create_combined_table()