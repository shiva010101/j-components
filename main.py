import pandas as pd

data = pd.read_csv("winequality-white.csv", sep=";")

col = data.columns

x_col = [col for col in col]
x_col.remove("quality")

# Gives all rows
all_val = [data.iloc[i].to_list() for i in range(len(data.index) - 1)]
for i in range(len(all_val)):
    print(all_val[i])
