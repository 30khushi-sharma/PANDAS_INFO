#GROUPING IN PANDAS
import pandas as pd
# data ={
#   "age": [20, 21, 20, 23, 24, 24, 26, 21],
#   "salary": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000]
# }
# df=pd.DataFrame(data)
# group = df.groupby('age')["salary"].sum()  # Group by a specific column
# print(group)

#merging dataframes
data1 = {
    "name": ["ANUSH", "RAMIYA", "KAVYA", "SREEJA"],
    "age": [20, 21, 22, 23],
    "salary": [50000, 60000, 70000, 80000]
}   
data2 = {
    "name": ["ANUSH", "RAMIYA", "KAVYA", "SREEJA"],
    "performance score": [3.5, 4.0, 4.5, 5.0],
    "department": ["HR", "Finance", "IT", "Marketing"]    
    
}
df1 = pd.DataFrame(data1) 
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df1, df2, on="name" , how="inner")  # Merging two DataFrames on a common column
# merged_df = pd.merge(df1, df2, on="name" , how="outer")  
# merged_df = pd.merge(df1, df2, on="name" , how="left")  
# merged_df = pd.merge(df1, df2, on="name" , how="right") 
# merged_df = pd.merge(df1, df2, on="name" , how="cross")  
print(merged_df)


