#Imports Libraries
import pandas as pd
import matplotlib.pyplot as plt

#Turns sensor_data csv file into a table in pandas format
df = pd.read_csv("data/sensor_data.csv")

#Converts the timestamps in df to datetime objects to make comparison easier
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

#Displays that the information in df to check that it is correct.
#print(df.head())
#df.info() # Prints itself and returns none
#print(df.describe())

#Computes the number of anomalies both as a sum and a percentage of the total.
anomaly_count = df["Known Anomaly"].sum()
anomaly_percentage = (anomaly_count / len(df)) * 100

#Prints the previously calculated values
#print("Number of anomalies: ",  anomaly_count)
#print("Percentage of anomalous readings:", anomaly_percentage, "%")

#Creates a variable that is true where ever there is an anomaly for its respective category
temperature_anomalies = df.loc[df["Temperature Anomaly"]]
vibration_anomalies = df.loc[df["Vibration Anomaly"]]

#Creates a figure for temperature data to be displayed of size 12in by 5in in width and height respectively
plt.figure(figsize=(12, 5))

#Sets the data for the main axis
plt.plot(
    df["Timestamp"],
    df["Temperature"],
    label = "Temperature"
)

#Sets the data for the scatterplot on the figure
plt.scatter(
    temperature_anomalies["Timestamp"],
    temperature_anomalies["Temperature"],
    color = "red",
    label = "Temperature Anomalies"
)

#Setting up key information to make a graph readable
plt.title("Industrial Equipment Temperature Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Temperature")
plt.legend()
plt.grid(True)

#Adjusts the figure to make sure all data fits properly within dimensions
plt.tight_layout()
#Displays the figure
plt.show()


#Creates a figure for vibration data to be displayed of size 12in by 5in in width and height respectively
plt.figure(figsize = (12,5))

#Sets the data for the main axis
plt.plot(
    df["Timestamp"],
    df["Vibration"],
    label = "Vibration"
)

#Sets the data for the scatterplot on the figure
plt.scatter(
    vibration_anomalies["Timestamp"],
    vibration_anomalies["Vibration"],
    color = "red",
    label = "Vibration Anomalies"
)

#Setting up key information to make a graph readable
plt.title("Industrial Equipment Vibration Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Vibration")
plt.legend()
plt.grid(True)

#Adjusts the figure to make sure all data fits properly within dimensions
plt.tight_layout()
#Displays the figure
plt.show()


#More value testing
#print(df.columns)
#More value testing (Again)
#print("Temperature anomalies:", df["Temperature Anomaly"].sum())
#print("Vibration anomalies:", df["Vibration Anomaly"].sum())
#print("Total anomalies:", df["Known Anomaly"].sum())

