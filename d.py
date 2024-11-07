import random
import csv

# Number of data points
num_points = 100

# Initialize the first time and distance values randomly
time = random.uniform(0, 0.1)  # Random time between 0 and 0.1 microseconds
distance = random.uniform(5, 10)  # Random distance between 5 and 10 feet

# Open a file to write the data
with open('random_increasing_data.csv', mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["time (microseconds)", "distance (feet)"])  # Header
    
    # Write the first data point
    writer.writerow([time, distance])
    
    # Generate and write the rest of the data points
    for _ in range(1, num_points):
        # Ensure new time and distance are larger than the previous ones
        time += random.uniform(0, 0.1)  # Increase time by a random small value
        distance += random.uniform(0, 0.5)  # Ensure distance increases by a random value

        # Write each data point to the file
        writer.writerow([time, distance])

print("CSV file created successfully.")
