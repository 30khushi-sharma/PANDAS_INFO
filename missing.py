import pandas as pd
data ={
  "name": ["ANUSH",None, "RAMIYA", "KAVYA", "SREEJA"],
  "age": [20,None, 21, 22, 23],
   "salary": [50000, None,60000, 70000, 80000],
   "performance score": [3.5,None, 4.0, 4.5, 5.0],
}
df = pd.DataFrame(data)
print(df.isnull())  # Check for missing values
print(df.isnull().sum())  # Check for count of missing values

#dropna for removing missing values
# axis=0 for rows, axis = 1 for columns
# implace = true for modifying the original DataFrame
df.dropna(axis=0, inplace=True)  # Drop rows with any missing values
print(df)

# fillna for filling missing values
df.fillna(0, inplace=True)  # Fill missing values with 0
print(df)

df["age"].fillna(df["age"].mean(), inplace=True)  # Fill missing 'age' with mean
print(df)

#interpolation for filling missing values
#estimated value fill krne ke liye jis jagh ma mising value hai
df.interpolate(method='linear',axis=0, inplace=True)  # Linear interpolation for filling missing values