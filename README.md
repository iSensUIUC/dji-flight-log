# dji-flight-log
This repository details instructions on how to record and parse DJI's drone flight logs


DJI's flight logs contain information from all the sensors on the drone. By connecting the controller to an RTK base station, we are also able to get highly accurate (cm-precise) GPS coordinates for the drone. Unfortunately, DJI scrambles these flight logs and hence we cannot parse them ourselves. I have found a website https://airdata.com/ that is sponsored by DJI and parses the logs for the users. We will be using this website to analyze flight data.


## Downloading flight data
Every time the drone goes on a flight, the data from that flight is stored on the DJI Remote Controller. The process to transfer this data onto your computer is as follows:

Step 1: Download the Android File Transfer app.

Step 2: Go to https://airdata.com/ and create an account.

Step 3: Connect the Controller to your computer via USB/USB-C. (After doing this, the Android File Transfer app should open automatically)

Step 4: Find and select the flight logs (they will be of the form DJIFlightRecord_YYYY_MM_DD_[timestamp]) and drag it to whatever folder you want on your computer. Eject the Controller.

Step 5: Upload this raw data file to AirData and let it process the flight logs. It will then give you an option to download the data in csv format.

Video Tutorial: https://www.youtube.com/watch?v=gc1kCtlwx0A 

## Plotting data
When trying to recreate the drone's flight path, we need the latitude, longitude, and height from the flight logs. Unfortunately, the latitude and longitude are in degrees and on a global reference frame. 

We can convert them to a reference frame relative to the starting location by simply subtracting the initial lat/lon from the rest.

After this, we have the relative lat/lon coordinates in degrees. In order to convert them to meters, we use the following equations:

Latitude in meters = degrees * 111000 

Longitude in meters = degrees * (cos(degrees) * 111320)

This is all done and plotted in the script parse_data.py.

