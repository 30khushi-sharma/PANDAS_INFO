import pandas as pd
data ={
  "name": ["ANUSH", "RAMIYA", "KAVYA", "SREEJA"],
  "age": [20, 21, 22, 23],
   "salary": [50000, 60000, 70000, 80000],
   "performance score": [3.5, 4.0, 4.5, 5.0],
}
df = pd.DataFrame(data)
# print(df)
# name = df["name"]  # selecting a single column
# print(name)
# columns = df[["name", "age"]]  # selecting multiple columns
# print(columns)
# specific_column = df[df["salary"]>60000 & (df["age"] >23)]  # selecting a specific column
# print(specific_column)
specific_column = df[(df["salary"]>60000 )| (df["age"] >22)]  # selecting a specific column
print(specific_column)