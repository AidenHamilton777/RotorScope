# ============================================================
# 1. DATA LOADING AND PREPARATION
# ============================================================

#Imports Libraries
import pandas as pd
import matplotlib.pyplot as plt

#Data Loading and Prep

#Turns sensor_data csv file into a table in pandas format
df = pd.read_csv("data/sensor_data.csv")

#Converts the timestamps in df to datetime objects to make comparison easier
df["Timestamp"] = pd.to_datetime(df["Timestamp"])


# ============================================================
# 2. ANOMALY FILTERING
# ============================================================


#Creates a variable that is true where ever there is an anomaly for its respective category
temperature_anomalies = df.loc[df["Temperature Anomaly"]]
vibration_anomalies = df.loc[df["Vibration Anomaly"]]
rotational_speed_anomaly = df.loc[df["Rotational Speed Anomaly"]]
power_consumption_anomaly = df.loc[df["Power Consumption Anomaly"]]


# ============================================================
# 3. DATA VISUALIZATION
# ============================================================


# ================ Temperature Visualization =================

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


# ================ Vibration Visualization =================

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


# ================ Rotational Speed Visualization =================

#Creates a figure for vibration data to be displayed of size 12in by 5in in width and height respectively
plt.figure(figsize = (12,5))

#Sets the data for the main axis
plt.plot(
    df["Timestamp"],
    df["Rotational Speed"],
    label = "Rotational Speed"
)

#Sets the data for the scatterplot on the figure
plt.scatter(
    rotational_speed_anomaly["Timestamp"],
    rotational_speed_anomaly["Rotational Speed"],
    color = "red",
    label = "Rotational Speed Anomalies"
)

#Setting up key information to make a graph readable
plt.title("Industrial Equipment Rotational Speed Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Rotational Speed")
plt.legend()
plt.grid(True)

#Adjusts the figure to make sure all data fits properly within dimensions
plt.tight_layout()
#Displays the figure
plt.show()


# ================ Power Consumption Visualization =================

#Creates a figure for vibration data to be displayed of size 12in by 5in in width and height respectively
plt.figure(figsize = (12,5))

#Sets the data for the main axis
plt.plot(
    df["Timestamp"],
    df["Power Consumption"],
    label = "Power Consumption"
)

#Sets the data for the scatterplot on the figure
plt.scatter(
    power_consumption_anomaly["Timestamp"],
    power_consumption_anomaly["Power Consumption"],
    color = "red",
    label = "Power Consumption Anomalies"
)

#Setting up key information to make a graph readable
plt.title("Industrial Equipment Power Consumption Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Power Consumption")
plt.legend()
plt.grid(True)

#Adjusts the figure to make sure all data fits properly within dimensions
plt.tight_layout()
#Displays the figure
plt.show()


# ============================================================
# 4. CORRELATION ANALYSIS
# ============================================================


sensor_data = df[["Temperature", "Vibration", "Rotational Speed", "Power Consumption"]]

correlation_matrix = (sensor_data.corr(method = "pearson"))

plt.imshow(correlation_matrix, cmap = "coolwarm", vmin = -1, vmax = 1)

plt.colorbar()
plt.xticks(ticks = [0,1,2,3], labels = sensor_data.columns)
plt.yticks(ticks = [0,1,2,3], labels = sensor_data.columns)
plt.title("Motor Data Correlation Heatmap")

for row in range(len(correlation_matrix.index)):
    for col in range(len(correlation_matrix.columns)):
        plt.text(x = col, y = row, s = round(correlation_matrix.iloc[row, col], 3))


plt.tight_layout()
plt.show()
