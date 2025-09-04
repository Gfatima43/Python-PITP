# Week 06 Day-26,27
#%% Import necessary modules
import pandas as pd

# %%
data = pd.read_csv('KKYLOUIS332.csv')
data.head()
# %%
data['DateTime'] = data['Date'] + ' ' + data['Time']
data['DateTime']
#%%
data['DateTime'] = pd.to_datetime(data['DateTime'])

data['DateTime']
#%%
data.set_index(data['DateTime'], inplace=True)

# %%
import pandas as pd # type: ignore

# Load the uploaded CSV file to preview its content
file_path = 'KKYLOUIS332.csv'
data = pd.read_csv(file_path)

# Display the first few rows to understand its structure
data.head()

# %%
# Descriptive statistics for Temperature_C and Speed_kmh
temperature_stats = data['Temperature_C'].describe()
speed_stats = data['Speed_kmh'].describe()

print("Temperature_C Statistics:")
print(temperature_stats)

print("\nSpeed_kmh Statistics:")
print(speed_stats)

# %%
import matplotlib.pyplot as plt

# Convert 'Date' column to datetime for better handling of time-series data
data['Date'] = pd.to_datetime(data['Date'])

# Group by date to compute daily mean temperature
daily_temperature = data.groupby('Date')['Temperature_C'].mean()

# Plot: Temperature Trend Over Time
plt.figure(figsize=(12, 6))
plt.plot(daily_temperature, color='blue', alpha=0.7, label='Daily Mean Temperature')
plt.title('Daily Temperature Trend Over Time', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Compute rolling averages (7-day and 30-day)
rolling_7 = daily_temperature.rolling(window=7).mean()
rolling_30 = daily_temperature.rolling(window=30).mean()

# Plot: Rolling Averages
plt.figure(figsize=(12, 6))
plt.plot(daily_temperature, color='blue', alpha=0.4, label='Daily Mean Temperature')
plt.plot(rolling_7, color='orange', label='7-Day Rolling Average')
plt.plot(rolling_30, color='red', label='30-Day Rolling Average')
plt.title('Temperature Trend with Rolling Averages', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# %%
# Extract month from the 'Date' column and compute monthly average temperatures
data['Month'] = data['Date'].dt.month
monthly_avg_temperature = data.groupby('Month')['Temperature_C'].mean()

# Plot: Monthly Average Temperatures
plt.figure(figsize=(10, 6))
plt.plot(monthly_avg_temperature.index, monthly_avg_temperature, marker='o', color='green', label='Monthly Average Temperature')
plt.title('Seasonality in Temperature: Monthly Averages', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(alpha=0.3)
plt.legend()
plt.show()

# %%
import seaborn as sns

# Define seasons based on rough date ranges
# Winter: December (12), January (1), February (2)
# Spring: March (3), April (4), May (5)
# Summer: June (6), July (7), August (8)
# Fall: September (9), October (10), November (11)
def assign_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Fall'

# Add a 'Season' column to the dataset
data['Season'] = data['Month'].apply(assign_season)

# Boxplot: Temperature by Season
plt.figure(figsize=(10, 6))
sns.boxplot(x='Season', y='Temperature_C', data=data, order=['Winter', 'Spring', 'Summer', 'Fall'], palette='coolwarm')
plt.title('Temperature Distribution Across Seasons', fontsize=14)
plt.xlabel('Season', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(alpha=0.3, linestyle='--', axis='y')
plt.show()

# %%
# Boxplot: Temperature by Season with different colors for each season
season_colors = {
    'Winter': 'skyblue',
    'Spring': 'lightgreen',
    'Summer': 'orange',
    'Fall': 'gold'
}

plt.figure(figsize=(10, 6))
sns.boxplot(
    x='Season',
    y='Temperature_C',
    data=data,
    order=['Winter', 'Spring', 'Summer', 'Fall'],
    palette=season_colors
)
plt.title('Temperature Distribution Across Seasons', fontsize=14)
plt.xlabel('Season', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(alpha=0.3, linestyle='--', axis='y')
plt.show()