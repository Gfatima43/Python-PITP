#%%
# Question 1: 
# Create a class DatasetStats that: 

import pandas as pd

class DatasetStats:
    def __init__(self, dataframe):
        """
        Initialize the DatasetStats class with a Pandas DataFrame.
        :param dataframe: Input Pandas DataFrame
        """
        self.dataframe = dataframe

    def display_first_five(self):
        """
        Display the first five rows of the dataset.
        """
        print("First five rows of the dataset:")
        print(self.dataframe.head())

    def calculate_mean(self, column_name):
        """
        Calculate and return the mean of a specified numeric column.
        :param column_name: Name of the numeric column
        :return: Mean of the column
        """
        if column_name in self.dataframe.select_dtypes(include='number').columns:
            return self.dataframe[column_name].mean()
        else:
            raise ValueError("Column is not numeric or does not exist.")

    def check_missing_values(self):
        """
        Check for missing values in the dataset and return the count for each column.
        :return: A Series with the count of missing values per column
        """
        return self.dataframe.isnull().sum()

if __name__ == "__main__":
    # DataFrame
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Age": [25, 30, None, 22, 29],
        "Salary": [50000, 60000, 55000, None, 72000]
    }
    df = pd.DataFrame(data)

    # Initialize the DatasetStats class
    stats = DatasetStats(df)

    # Display the first five rows
    stats.display_first_five()

    # Calculate the mean of the 'Age' column
    try:
        mean_age = stats.calculate_mean("Age")
        print(f"\nMean Age: {mean_age}")
    except ValueError as e:
        print(e)

    # Check missing values
    missing_values = stats.check_missing_values()
    print("\nMissing values per column:")
    print(missing_values)

#%%
# Question 2: 
# Write a Python function using NumPy that: 

import numpy as np

def numpy_stats():
    """
    Generate a random array of 100 integers and calculate statistics.
    :return: A dictionary containing mean, median, and standard deviation
    """
    # Generate 100 random integers between 1 and 1000
    array = np.random.randint(1, 1001, 100)
    
    # Calculate statistics
    stats = {
        "mean": np.mean(array),
        "median": np.median(array),
        "std_dev": np.std(array)
    }
    return stats

if __name__ == "__main__":
    stats = numpy_stats()
    print("Statistics for the generated array:")
    print(f"Mean: {stats['mean']}")
    print(f"Median: {stats['median']}")
    print(f"Standard Deviation: {stats['std_dev']}")

#%%
# Question 3: 
# Using Matplotlib, write a Python program that: 

import matplotlib.pyplot as plt

def create_line_plot():
    """
    Create a line plot for the function y = x^2.
    """
    # Generate x values and corresponding y values
    x = list(range(-10, 11))
    y = [i**2 for i in x]

    # Plot the function
    plt.plot(x, y, marker='o', label='y = x^2')
    plt.xlabel("x-axis")  # X-axis label
    plt.ylabel("y = x^2")  # Y-axis label
    plt.title("Line Plot of y = x^2")  # Plot title
    plt.legend()  # Add legend
    plt.grid(True)  # Show grid
    plt.show()  # Display the plot

# Call the function to generate the plot
create_line_plot()

#%%
# Question 4: 
# Using Seaborn, write a Python program that: 

import seaborn as sns

def seaborn_scatterplot():
    """
    Load a built-in dataset and create a scatter plot with a regression line.
    """
    # Load the "tips" dataset
    data = sns.load_dataset("tips")
    
    # Create scatter plot with regression line
    sns.lmplot(x="total_bill", y="tip", data=data, aspect=1.5)
    plt.title("Scatter Plot with Regression Line")
    plt.show()

# Call the function to generate the plot
seaborn_scatterplot()

#%%
# Question 5: 
# Integrate all the above components into a main program where the user can: 

# Method 1:
def main():
    """
    Main program to integrate all components and provide a menu-driven interface.
    """
    print("Welcome to the Data Analysis Program!")
    print("Select an option:")
    print("1: Dataset Statistics")
    print("2: Generate Random Array (NumPy)")
    print("3: Line Plot (Matplotlib)")
    print("4: Scatter Plot with Regression (Seaborn)")
    
    # Take user input for choice
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        # Example dataset
        df = pd.DataFrame({
            "A": [1, 2, 3, 4, 5],
            "B": [5, 4, None, 2, 1]
        })
        stats = DatasetStats(df)
        stats.display_first_five()
        
        column = input("Enter column name to calculate mean: ")
        try:
            mean_value = stats.calculate_mean(column)
            print(f"Mean of column '{column}': {mean_value}")
        except ValueError as e:
            print(e)
        
        print("Missing values per column:")
        print(stats.check_missing_values())

    elif choice == 2:
        # Generate random array and show statistics
        stats = numpy_stats()
        print("Statistics for the random array:")
        print(stats)

    elif choice == 3:
        # Create a line plot
        create_line_plot()

    elif choice == 4:
        # Create a scatter plot with regression
        seaborn_scatterplot()

    else:
        print("Invalid choice. Please select a valid option.")

# Run the main program
if __name__ == "__main__":
    main()

# %%
# Method 2:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DatasetStats:
    def __init__(self, df):
        self.df = df
    
    def display_first_five(self):
        print("First five rows of the dataset:")
        print(self.df.head())
    
    def calculate_mean(self, column):
        if column not in self.df:
            raise ValueError(f"Column '{column}' not found in dataset.")
        return self.df[column].mean()
    
    def check_missing_values(self):
        return self.df.isnull().sum()

def numpy_stats():
    # Generate a random array and calculate statistics
    arr = np.random.rand(10)
    return {
        "Mean": np.mean(arr),
        "Standard Deviation": np.std(arr),
        "Max": np.max(arr),
        "Min": np.min(arr)
    }

def create_line_plot():
    # Generate x values and corresponding y values
    x = list(range(-10, 11))
    y = [i**2 for i in x]
    
    # Plot the function
    plt.plot(x, y, marker='o', label='y = x^2')
    plt.xlabel("x-axis")
    plt.ylabel("y = x^2")
    plt.title("Line Plot of y = x^2")
    plt.legend()
    plt.grid(True)
    plt.show()

def seaborn_scatterplot():
    # Load the "tips" dataset
    data = sns.load_dataset("tips")
    
    # Create scatter plot with regression line
    sns.lmplot(x="total_bill", y="tip", data=data, aspect=1.5)
    plt.title("Scatter Plot with Regression Line")
    plt.show()

def main():
    print("Welcome to the Data Analysis Program!")
    print("Select an option:")
    print("1: Dataset Statistics")
    print("2: Generate Random Array (NumPy)")
    print("3: Line Plot (Matplotlib)")
    print("4: Scatter Plot with Regression (Seaborn)")

    # Take user input for choice
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        # Example dataset
        df = pd.DataFrame({
            "A": [1, 2, 3, 4, 5],
            "B": [5, 4, None, 2, 1]
        })
        stats = DatasetStats(df)
        stats.display_first_five()
        
        column = input("Enter column name to calculate mean: ")
        try:
            mean_value = stats.calculate_mean(column)
            print(f"Mean of column '{column}': {mean_value}")
        except ValueError as e:
            print(e)
        
        print("Missing values per column:")
        print(stats.check_missing_values())

    elif choice == 2:
        # Generate random array and show statistics
        stats = numpy_stats()
        print("Statistics for the random array:")
        print(stats)

    elif choice == 3:
        # Create a line plot
        create_line_plot()

    elif choice == 4:
        # Create a scatter plot with regression
        seaborn_scatterplot()

    else:
        print("Invalid choice. Please select a valid option.")

# Run the main program
if __name__ == "__main__":
    main()
