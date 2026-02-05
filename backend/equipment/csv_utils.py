import pandas as pd

def load_csv(file_path):
    return pd.read_csv(file_path)

def calculate_summary(file_path):
    data = load_csv(file_path)

    return {
        "total_count": len(data),
        "avg_flowrate": data["Flowrate"].mean(),
        "avg_pressure": data["Pressure"].mean(),
        "avg_temperature": data["Temperature"].mean(),
        "type_distribution": data["Type"].value_counts().to_dict()
    }
