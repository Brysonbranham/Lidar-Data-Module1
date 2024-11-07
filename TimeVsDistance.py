import csv
import matplotlib.pyplot as plt

# Replace with the path to your CSV file
file_path = "random_increasing_data.csv"

# Initialize lists to store the data
time = []
distance = []


# Read the CSV file
with open(file_path, mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        time.append(float(row[0]))      # Time in microseconds
        distance.append(float(row[1]))  # Distance in feet

# Now, 'time' and 'distance' contain the values from the CSV file

# Combine with zip and sort by time
sorted_data = sorted(zip(time, distance))
time_sorted, distance_sorted = zip(*sorted_data)

fig, ax = plt.subplots()
ax.plot(time_sorted, distance_sorted)
plt.show()