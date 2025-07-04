import pandas as pd
data ={
  "name": ["ANUSH", "RAMIYA", "KAVYA", "SREEJA"],
  "age": [20, 21, 22, 23],
   "salary": [50000, 60000, 70000, 80000],
   "performance score": [3.5, 4.0, 4.5, 5.0],
}
df = pd.DataFrame(data)
print("DESCRIPTIVE STATISTICS")
print(df.describe())
print(f'SHAPE: {df.shape}')
print(f'COLUMNS: {df.columns}')
column = df("column1")   #selecting of column
rows= df[df["column name like salary"]>1000]  #selecting of rows and condition 
filter_rows = df[(df["column name like salary"]>50000)& (df["column name " ]<8000)]  #filtering rows based on a multiple values condition