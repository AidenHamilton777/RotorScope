#Imports Relevant Libraries.
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
from zoneinfo import ZoneInfo

#Sets timezone.
start_time = datetime.now(ZoneInfo("America/Toronto"))

#Creates dictionary with generated values for simulating using the numpy library and datetime library.
data = {
    "Timestamp" : pd.date_range(start = start_time, periods = 1000, freq = "1s" ),
    "Temperature" : np.random.normal(65, 3, 1000),
    "Vibration" : np.random.normal(2.2, 0.4, 1000),
    "Rotational Speed" : np.random.normal(1450, 25, 1000),
    "Power Consumption" : np.random.normal(4.8, 0.3, 1000)
}

#Puts the dictionary "data" into a table using the pandas library (df = Data Frame).
df = pd.DataFrame(data)

#Creates a Boolean column identifying the rows containing simulated temperature anomalies.
df["Temperature Anomaly"] = False
df.loc[200:209, "Temperature Anomaly"] = True

# Creates a Boolean column identifying the rows containing simulated vibration anomalies.
df["Vibration Anomaly"] = False
df.loc[500:509, "Vibration Anomaly"] = True

#Creates column for any known anomaly. Is a boolean column that evaluates to true if any other column has an anomaly.
df["Known Anomaly"] = (
    df["Temperature Anomaly"] | df["Vibration Anomaly"]
)

#Plants random values higher than the average in specific rows of the data to simulate anomalies
df.loc[200:209, "Temperature"] = np.random.uniform(90, 100, 10)
df.loc[500:509, "Vibration"] = np.random.uniform(5, 7, 10)

#Saves the data frame as a csv file called sensor_data.csv in a folder called data 
df.to_csv("data/sensor_data.csv", index=False)

#Prints the data frame
print(df)