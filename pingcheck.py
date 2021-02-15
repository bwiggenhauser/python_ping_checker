import os
import time
import subprocess

# Settings before starting the script
minutesToCheck = 5
timeToSleep = 5
hostname = "google.com"

# Get current time (to stop script later)
currentTime = time.time()
endTime = currentTime + (minutesToCheck * 60)

# Pinging google.com and returning response
def check_ping():
    output = subprocess.check_output("ping -n 1 " + hostname, shell=True)
    return output

# Counts the amount of pings for visuals
counter = 0

# Array of pings in ms
pings = []

# While in check timeframe, check my ping
while (time.time() < endTime):
    counter += 1
    print(f"Pinging ... ({counter})")
    response = str(check_ping())
    pingIndex = response.find("Zeit=")
    pings.append(int(response[pingIndex+5:pingIndex+7]))
    time.sleep(timeToSleep)

# Result printing to console
print("--------------------")
print("Results:")
print("-> Max. Ping: " + str(max(pings)))
print("-> Average Ping: " + str(sum(pings)/len(pings)))