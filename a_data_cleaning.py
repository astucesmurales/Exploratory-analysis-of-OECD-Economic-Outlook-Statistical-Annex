import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
FILE_PATH = DATA_DIR / "EO118_Inflation-Wages-Costs-and-Labour-Market.xlsx"

def clean_oecd_sheet(sheet_name, drop_forecast_duplicates=True):

    df = pd.read_excel(
        FILE_PATH,
        sheet_name = sheet_name,
        header = 2
    )

    df = df.rename(columns = {df.columns[0]: "Area"})
    df = df[df["Area"].notna()]
    df = df[~df["Area"].isin(["GDP deflator", "Percentage changes"])]
    df = df.dropna(axis = 1, how = "all")
    df = df.loc[:, ~df.columns.astype(str).str.contains("Unnamed")]

    if drop_forecast_duplicates:
        df = df.loc[:, ~df.columns.astype(str).str.contains(r"\.\d+$")]

    df = df.loc[:, ~df.columns.duplicated()]
    df = df.reset_index(drop=True)

    return df


def load_all_data():

    variables = {
        "private_consumption_deflators": clean_oecd_sheet("Private_Consumption_Deflators"),
        "consumer_prices": clean_oecd_sheet("Consumer_Prices"),
        "compensation_per_employee": clean_oecd_sheet("Compensation_Per_Employee"),
        "labour_productivity": clean_oecd_sheet("Labour_Productivity"),
        "unit_labour_costs": clean_oecd_sheet("Unit_Labour_Costs"),
        "labour_force": clean_oecd_sheet("Labour_Force"),
        "employment": clean_oecd_sheet("Employment"),
        "unemployment_rate": clean_oecd_sheet("Unemployment_Rates"),
    }

    return variables
