import pandas as pd
data = {
  "time": ["1", "2", "3", "4", "5", "6", "7", "8"],
  "value": [10, 20, 30, 40, 50, None, 70, 80],
}
df=pd.DataFrame(data)
print(df)
print("after interpolation")
df["value"].interpolate(method='linear', inplace=True)  # Linear interpolation for filling missing values
print(df)

#time series, numeric data
df.sort_values(by="value",  inplace=True)  # Sorting the DataFrame by a specific column
# true for accending order
# False for descending order 

#summary statistics 

mean = df["value"].mean()  # Calculate the mean of a specific column
print(mean)
df["value"].median()  # Calculate the median of a specific column   
df["value"].std()  # Calculate the standard deviation of a specific column
df["value"].min()  # Calculate the minimum value of a specific column 
df["value"].max()  # Calculate the maximum value of a specific column
df["value"].describe()  # Get a summary of statistics for a specific column

