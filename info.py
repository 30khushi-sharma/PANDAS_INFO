import pandas as pd
data={
  "name":["ANUSH","RAMIYA","KAVYA","SREEJA","SREEJITH","ANUJAL","ANUJASH","NUJA"],
  "age":[20,21,22,23,24,25,26,27],
  "City":["Kochi","haryana","jammu","punjab","Kerala","meghalaya","mumbai","agra"]
}
df= pd.DataFrame(data)
print(df.info())