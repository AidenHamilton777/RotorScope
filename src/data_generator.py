import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
from zoneinfo import ZoneInfo

start_time = datetime.now(ZoneInfo("America/Toronto"))

data = {
    "Timestamp" : pd.date_range(start = start_time, periods = 1000, freq = "1s" ),
    "Temperature" : np.random.normal(65, 3, 1000),
    "Vibration" : np.random.normal(2.2, 0.4, 1000),
    "Rotational Speed" : np.random.normal(1450, 25, 1000),
    "Power Consumption" : np.random.normal(4.8, 0.3, 1000)
}

df = pd.DataFrame(data)

df["Known Anomaly"] = False
df.loc[200:209, "Known Anomaly"] = True
df.loc[500:509, "Known Anomaly"] = True

df.loc[200:209, "Temperature"] = np.random.uniform(90, 100, 10)
df.loc[500:509, "Vibration"] = np.random.uniform(5, 7, 10)

df.to_csv("data/sensor_data.csv", index=False)
print(df)