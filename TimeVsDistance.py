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

# Now, 'time' and 'distance' contain the values from the CSV file

# Combine with zip and sort by time
sorted_data = sorted(zip(time, distance))
time_sorted, distance_sorted = zip(*sorted_data)

min_time = min(time_sorted)
max_time = max(time_sorted)



# Add a sorting bar (slider) to control the range of visible data
ax_bar = plt.axes([0.1, 0.02, 0.8, 0.03], facecolor='lightgoldenrodyellow')  # Slider position and color
slider = Slider(ax_bar, 'Range', min_time, max_time, valinit=min_time, valstep=(max_time - min_time) / 100)


# Update the plot when the slider value changes
def update(val):
    # Get the current slider value
    slider_value = slider.val
    
    # Update the range of the visible data on the plot
   
    
    # Filter data based on the slider's value (only show data within the range)
    visible_time = [t for t in time_sorted if t <= slider_value]
    visible_distance = [distance_sorted[i] for i in range(len(time_sorted)) if time_sorted[i] <= slider_value]
    
    # Plot the visible data
    ax_main.plot(visible_time, visible_distance, marker='o')
    ax_main.set_title('Data with Sorting Bar')
    ax_main.set_xlabel('Time (microseconds)')
    ax_main.set_ylabel('Distance (feet)')
    ax_main.grid(True)
    ax_main.set_xlim(min_time, max_time)
    
    # Redraw the figure
    fig.canvas.draw_idle()

slider.on_changed(update)


fig, ax_main = plt.subplots()

plt.show()