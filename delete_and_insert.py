#Delete and insert function in python pandas

#insert function in python pandas

import pandas as pd 

var = pd.DataFrame({"A":[1,2,3,4,5],"B":[6,7,8,9,10],"c":[11,12,13,14,15]}) #creating a dataframe

#var.insert (2,"C",var["A"] + var["B"])  #inserting a column at index 2
#print(var)


var.insert(1,"D",[11,12,13,14,15]) #inserting a column at index 1 second example

#print(var) #printing the dataframe

var["python12"] = var["A"][:3] #inserting a column at the end of the dataframe


#print(var) #printing the dataframe

#delete function in python pandas

var_1 = var.pop("B")

#print(var) #printing the dataframe

#print(var_1) #printing the dataframe        

del var["c"]

print(var) #printing the dataframe          