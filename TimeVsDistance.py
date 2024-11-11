import csv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

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

# Sort data by time
sorted_data = sorted(zip(time, distance))
time_sorted, distance_sorted = zip(*sorted_data)

min_time = min(time_sorted)
max_time = max(time_sorted)
min_distance = min(distance_sorted)
max_distance = max(distance_sorted)

# Create a figure and axis for the plot
fig, ax_main = plt.subplots()
plt.subplots_adjust(bottom=0.35)  # Adjust space for both sliders

# Initial plot
line, = ax_main.plot(time_sorted, distance_sorted, marker='o')
ax_main.set_xlim(min_time, max_time)
ax_main.set_ylim(min_distance, max_distance)
ax_main.set_title('Lidar Distance Data ')
ax_main.set_xlabel('Time (microseconds)')
ax_main.set_ylabel('Distance (feet)')
ax_main.grid(True)

# Add sliders for selecting the range
ax_slider_min = plt.axes([0.1, 0.1, 0.8, 0.03], facecolor='lightgoldenrodyellow')
ax_slider_max = plt.axes([0.1, 0.05, 0.8, 0.03], facecolor='lightgoldenrodyellow')
slider_min = Slider(ax_slider_min, 'Start Time', min_time, max_time, valinit=min_time, valstep=(max_time - min_time) / 100)
slider_max = Slider(ax_slider_max, 'End Time', min_time, max_time, valinit=max_time, valstep=(max_time - min_time) / 100)

# Update function for the sliders
def update(val):
    # Get current values from both sliders
    
    min_val = slider_min.val
    max_val = slider_max.val

    # Filter data based on the selected range
    visible_time = [t for t in time_sorted if min_val <= t <= max_val]
    visible_distance = [distance_sorted[i] for i in range(len(time_sorted)) if min_val <= time_sorted[i] <= max_val]

    # Update the line data with the filtered data
    line.set_data(visible_time, visible_distance)
    ax_main.set_xlim(min_val, max_val)
    ax_main.set_ylim(min_distance, max_distance)

    # Redraw the figure
    fig.canvas.draw_idle()

# Link the sliders to the update function
slider_min.on_changed(update)
slider_max.on_changed(update)

plt.show()
