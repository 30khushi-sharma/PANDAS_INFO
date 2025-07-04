# vertically or horizontally data ko combone karna
# 0 for row wise concatenation
# 1 for column wise concatenation
ignore_index = True  # Ignore the index while concatenating
import pandas as pd
customer_data = {
    "name": ["ANUSH", "RAMIYA", "KAVYA", "SREEJA"],
    "age": [20, 21, 22, 23],
    "City": ["Kochi", "haryana", "jammu", "punjab"]
}
customer_df = pd.DataFrame(customer_data) 
employee_data = {
    "name": ["SREEJITH", "ANUJAL", "ANUJASH", "NUJA"],
    "age": [24, 25, 26, 27],
    "City": ["Kerala", "meghalaya", "mumbai", "agra"]
}
employee_df = pd.DataFrame(employee_data)

# Concatenating the two DataFrames vertically
vertical_concat = pd.concat([customer_df, employee_df], axis=0, ignore_index=ignore_index)
print("Vertical Concatenation:")
print(vertical_concat)  