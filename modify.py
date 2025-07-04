import pandas as pd
data ={
  "name": ["ANUSH", "RAMIYA", "KAVYA", "SREEJA"],
  "age": [20, 21, 22, 23],
   "salary": [50000, 60000, 70000, 80000],
   "performance score": [3.5, 4.0, 4.5, 5.0],
}
df = pd.DataFrame(data)
print(df)
# METHOD 1
# df["bonus"]= df["salary"] * 0.1  # Adding a new column 'bonus' which is 10% of 'salary'
# print(df)

# METHOD 2
df.insert(0,"Employee ID", [1, 2, 3, 4])
print(df)# Inserting a new column 'Employee ID' at the first position

#updating values
#METHOD 1
df.loc[0, "salary"] = 55000  # Updating the salary of the first employee
print(df)

# METHOD 2
df["salary"] = df["salary"].apply(lambda x: x * 1.05)  # Increasing all salaries by 5%
print(df)

df.drop("performance score","age", inplace=True)  # Dropping the 'performance score' column
print(df)
