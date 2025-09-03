#%%
# Install required libraries
# pip install pandas matplotlib numpy

# Week 05 Day-23
# Import pandas library for data manipulation
import pandas as pd

# Read CSV file and display first 5 rows
data = pd.read_csv('KKYLOUIS332.csv')
data.head()

# %%
# Read CSV file and display first 10 rows
data = pd.read_csv('KKYLOUIS332.csv')
data.head(10)

# %%
# Attempt to access row by index directly (will cause KeyError)
data = pd.read_csv('KKYLOUIS332.csv')
data[0] # key error

# %%
# Access first row using iloc (integer location)
data = pd.read_csv('KKYLOUIS332.csv')
data.iloc[0]

# %%
# Access first row using loc (label-based, works if index is 0)
data = pd.read_csv('KKYLOUIS332.csv')
data.loc[0]

# %%
# Display last 5 rows of the DataFrame
data = pd.read_csv('KKYLOUIS332.csv')
data.tail()

# %%
# Show column names of the DataFrame
data = pd.read_csv('KKYLOUIS332.csv')
data.columns

# %%
# Get statistical summary of numerical columns
data = pd.read_csv('KKYLOUIS332.csv')
data.describe()

# %%
# Show shape (rows, columns) of the DataFrame
data = pd.read_csv('KKYLOUIS332.csv')
data.shape

# %%
# Show data types of each column
data = pd.read_csv('KKYLOUIS332.csv')
data.dtypes

# %%
# Week 05 Day-24
# Import matplotlib and numpy for plotting
import matplotlib.pyplot as plt
import numpy as np

# Create two points and plot them as dots
xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

# %%
# Plot a line between two points
xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints, ypoints)
plt.show()

# %%
# Plot a solid line between two points
xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints, ypoints, '-')
plt.show()

# %%
# Plot a dashed line between two points
xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints, ypoints, '--')
plt.show()

# %%
# Plot a dashed line for three points
xpoints = np.array([1,8,10])
ypoints = np.array([3,10,5])

plt.plot(xpoints, ypoints, '--')
plt.show()

# %%
# Plot points connected by lines with markers
xpoints = np.array([1,8,10])
ypoints = np.array([3,10,5])

plt.plot(xpoints, ypoints, 'o-')
plt.show()

# %%
# Plot only ypoints (x is index by default)
xpoints = np.array([1,8,10])
ypoints = np.array([3,10,5])

plt.plot(ypoints)
plt.show()

# %%
# Attempt to plot ypoints and a column named 'Temperature_C' (incorrect usage)
xpoints = np.array([1,8,10])
ypoints = np.array([3,10,5])

plt.plot(xpoints, ypoints, '--')
plt.plot('Temperature_C')
plt.show()

# %%
# Attempt to plot only 'Temperature_C' column (incorrect usage)
xpoints = np.array([1,8,10])
ypoints = np.array([3,10,5])

plt.plot('Temperature_C')
plt.show()

# %%
# Plot 'Temperature_C' column from DataFrame
xpoints = np.array([1,8,10])
ypoints = np.array([3,10,5])

plt.plot(data['Temperature_C'])
plt.show()

# %%
# Add labels to x and y axes
xpoints = np.array([1,8,10])
ypoints = np.array([3,10,5])

plt.xlabel('Time')
plt.ylabel('Temperature_C')
plt.show()

# %%
# Add labels and title to the plot
xpoints = np.array([1,8,10])
ypoints = np.array([3,10,5])

plt.xlabel('Time')
plt.ylabel('Temperature_C')
plt.title('Weather Measuring')
plt.show()

# %%
# Simulate data, average every 96 values, and plot averaged data
import numpy as np
import matplotlib.pyplot as plt

# Simulated data for demonstration
xpoints = np.random.random(960) * 10  # Replace with actual "time" data
ypoints = np.random.random(960) * 100  # Replace with actual "temperature" data

# Ensure the arrays can be divided into groups of 96
xpoints = xpoints[:len(xpoints) - len(xpoints) % 96]
ypoints = ypoints[:len(ypoints) - len(ypoints) % 96]

# Calculate the average of every 96 values
x_avg = np.mean(xpoints.reshape(-1, 96), axis=1)
y_avg = np.mean(ypoints.reshape(-1, 96), axis=1)

# Plot the averaged data
plt.plot(x_avg, y_avg, marker='o', linestyle='-')
plt.xlabel('Time (Averaged)')
plt.ylabel('Temperature (C)')
plt.title('Weather Measuring (Averaged Data)')
plt.grid()
plt.show()

# %%
# Simulate data, average every 96 values, and plot averaged data in red
import numpy as np
import matplotlib.pyplot as plt

# Simulated data for demonstration
xpoints = np.random.random(960) * 10  # Replace with actual "time" data
ypoints = np.random.random(960) * 100  # Replace with actual "temperature" data

# Ensure the arrays can be divided into groups of 96
xpoints = xpoints[:len(xpoints) - len(xpoints) % 96]
ypoints = ypoints[:len(ypoints) - len(ypoints) % 96]

# Calculate the average of every 96 values
x_avg = np.mean(xpoints.reshape(-1, 96), axis=1)
y_avg = np.mean(ypoints.reshape(-1, 96), axis=1)

# Plot the averaged data in red
plt.plot(x_avg, y_avg, marker='o', linestyle='-', color='red')
plt.xlabel('Time (Averaged)')
plt.ylabel('Temperature (C)')
plt.title('Weather Measuring (Averaged Data)')
plt.grid()
plt.show()

# %%
# Week 05 Day-25
# Display 'Date' column from DataFrame
data['Date']

# %%
# Display 'Time' column from DataFrame
data['Time']

# %%
# Combine 'Date' and 'Time' columns into new 'DateTime' column
data['DateTime'] = data['Date'] + ' ' + data['Time']
data['DateTime']

# %%
# Combine 'Date' and 'Time' columns, then convert to datetime type
data['DateTime'] = data['Date'] + ' ' + data['Time']
data['DateTime']

data['DateTime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])