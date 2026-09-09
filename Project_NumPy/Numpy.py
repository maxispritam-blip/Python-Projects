import numpy as np
import pandas as pd

# Load a CSV file into a NumPy array and display its shape

df = pd.read_csv('temperature_data.csv')
arr = df.shape
print("Shape of the array:", arr)

# Mean, median, and standard deviation of the each City

mean_value = np.mean(df)
print("Mean:", mean_value)

med_value = np.median(df)
print("Median:", med_value)

std_dev = np.std(df)
print("Standard Deviation:", std_dev)

# temperature data using min & max normalization

min_temp = np.min(df)
max_temp = np.max(df)

normalize_data = (df - min_temp) / (max_temp - min_temp)

print("Original: ", df)
print("Normalized Data: ", normalize_data)


# The City with the highest average temperature

max_temp_index = np.argmax(df.values, axis=0)

hottest_city = df.values[max_temp_index]
max_temp = df.values[max_temp_index].max()

print(f"The hottest city is {hottest_city} with {max_temp}°C.")

# thresold with the city wise

thresold = 30
above_thresold = df[df > thresold]
print("Cities with temperature above thresold:\n", above_thresold)

