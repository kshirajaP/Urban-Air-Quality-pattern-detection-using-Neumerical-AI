
'''import pandas as pd

def perceive_data(path):
    return pd.read_csv(path)'''

import pandas as pd

def perceive_data(path="data/AirQualityUCI.xlsx"):

    # Load Excel file
    data = pd.read_excel(path)

    # Drop empty columns if any
    data = data.dropna(axis=1, how='all')

    # Combine Date + Time into datetime
    '''data["datetime"] = pd.to_datetime(
        data["Date"] + " " + data["Time"]
    )'''
    data["datetime"] = pd.to_datetime(data["Date"].astype(str) + " " + data["Time"].astype(str))

    # Select relevant columns
    df = pd.DataFrame({
        "datetime": data["datetime"],
        "pm25": data["PT08.S1(CO)"],
        "pm10": data["NMHC(GT)"],
        "no2": data["NO2(GT)"],
        "so2": data["NOx(GT)"],
        "o3": data["C6H6(GT)"]
    })

    # Convert to numeric
    for col in ["pm25", "pm10", "no2", "so2", "o3"]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Replace invalid values (-200)
    df = df.replace(-200, pd.NA)

    # Drop missing values
    df = df.dropna()

    return df
