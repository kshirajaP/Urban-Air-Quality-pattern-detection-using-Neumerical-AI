
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.stats import zscore
import pandas as pd

def reason_patterns(data):
    # --- FORCE NUMERIC CLEANING (CRITICAL FIX) ---
    for col in ["pm25", "pm10", "no2", "so2", "o3"]:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    # Drop any remaining bad rows
    data = data.dropna(subset=["pm25", "pm10", "no2", "so2", "o3"])

    # Fix datetime column for Streamlit (Arrow compatibility)
    data["datetime"] = pd.to_datetime(data["datetime"], errors='coerce')
    data = data.dropna(subset=["datetime"])

    features = data[['pm25','pm10','no2','so2','o3']]
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=3, random_state=42)
    data['Cluster'] = kmeans.fit_predict(scaled)

    data['pm25_z'] = zscore(data['pm25'])
    data['Anomaly'] = data['pm25_z'].abs() > 2

    '''# Final cleanup before returning
    data = data.copy()
    data["datetime"] = data["datetime"].astype("datetime64[ns]")'''

    # --- FINAL DATA CLEANUP FOR STREAMLIT ---

    # Force datetime to proper format
    data["datetime"] = pd.to_datetime(data["datetime"], errors='coerce')

    # Drop bad datetime rows
    data = data.dropna(subset=["datetime"])

    # Convert to string (most stable for Streamlit display)
    data["datetime"] = data["datetime"].dt.strftime("%Y-%m-%d %H:%M:%S")

    return data
