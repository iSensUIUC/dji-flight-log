import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# constants for converting lat/lon to meters
LAT_TO_M = 111000
LON_TO_M = 111320
DEG_TO_RAD = np.pi/180.0
FT_TO_M = 0.3048

# file with csv flight data
filename = "FlightRecord1012/csvFiles/Oct-12th-2023-05-24PM-Flight-Airdata.csv"

df = pd.read_csv(filename)
data = df.to_numpy()

# Plotting Altitude
height = data[:,4]
ms = data[:,0]
plt.plot(ms, height)
plt.title("Altitude Plot")
plt.xlabel("Time (millisecond)")
plt.ylabel("Height (feet)")


# Extracting lat/lon from flight logs
# we need the lat/lon coordinates relative to the starting point
# this gives us the displacement of the drone
latitudes = data[:,2]
lat0 = latitudes[0]
latitudes = latitudes - lat0
longitudes = data[:,3]
lon0 = longitudes[0]
longitudes = longitudes - lon0

# converting lat/lon/height to x/y/z in meters
latitudes = latitudes.astype(float)
y = latitudes * LAT_TO_M
x = longitudes * np.cos(latitudes) * LON_TO_M
z = height * FT_TO_M

# Plotting 3D flight path
fig = plt.figure(figsize = (7, 7))
ax = plt.axes(projection ="3d")
ax.scatter3D(x, y, z, color = "green", s=10)
ax.set_title("FLight Path")
ax.set_xlabel("x-displacement (m)")
ax.set_ylabel("y-displacement (m)")
ax.set_zlabel("z-displacement (m)")

plt.show()
