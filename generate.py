import pandas as pd

# Define the data
data = {
    "age": [24, 68, 51],
    "bp": [100, 80, 0],
    "al": [2, 3, 0],
    "su": [0, 0, 0],
    "rbc": [1, 0, 1],
    "pc": [0, 1, 0],
    "pcc": [1, 0, 0],
    "ba": [0, 0, 0],
    "bgr": [136, 157, 121],
    "bu": [60, 162, 27],
    "sc": [1.9, 9.6, 0.8],
    "pot": [3.7, 4.9, 3.7],
    "wc": [9600, 11000, 8300],
    "htn": [1, 0, 0],
    "dm": [1, 1, 0],
    "cad": [0, 0, 0],
    "pe": [0, 0, 0],
    "ane": [1, 1, 0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file (without the index)
df.to_excel("sample_kidney.xlsx", index=False)
