import pandas as pd
data={
  "name":["ANUSH","RAMIYA","KAVYA","SREEJA","SREEJITH","ANUJAL","ANUJASH","NUJA"],
  "age":[20,21,22,23,24,25,26,27],
  "City":["Kochi","haryana","jammu","punjab","Kerala","meghalaya","mumbai","agra"]
}
df= pd.DataFrame(data)
print(df)
# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)
