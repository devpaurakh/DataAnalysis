import pandas as pd 
dis = {"a": [1, 2, 3], "b": [4, 5, 6],"c":[7,8,9]}
d = pd.DataFrame(dis)

# Save the dataframe to a csv file

d.to_csv("data2.csv", index=False, header=["a","b","c"]) # index=False is used to avoid writing row numbers in the csv file

