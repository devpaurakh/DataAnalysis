## Arithmetic Operations

import pandas as pd

var = pd.DataFrame({'a':[1,2,3,4,5], 'b':[6,7,8,9,10]}) #creating a dataframe
# print(var)

var['c'] = var['a'] + var['b'] #adding two columns
var['d'] = var['a'] - var['b'] #sub two columns
var['e'] = var['a'] * var['b'] #muli two columns
var['f'] = var['a'] / var['b'] #division two columns

#print(var) #printing the dataframe


var2 = pd.DataFrame({'a':[10,20,30,40,50], 'b':[61,71,81,91,101]}) #creating a dataframe

var2['Python'] = var2['a'] <= 20 #checking if a is less than or equal to 20
var2['Python_1'] = var2['b'] >= 100 #checking if b is greater than or equal to 100
#print(var2) #printing the dataframe



#practice
# 1. Create a dataframe with 3 columns and 5 rows and perform the following operations on it:

# a. Add the first two columns
# b. Subtract the second column from the first column
# c. Multiply the first column with the third column
# d. Divide the second column by the third column
# e. Check if the first column is less than or equal to 10
# f. Check if the second column is greater than or equal to 20

var3 = pd.DataFrame({"salary":[2000,1000,3000,5000,6000],"height":[5.5,5.6,5.7,5.8,5.9]}) #creating a dataframe

var3 = var3['Detail'] = var3['salary'] + ['height']
print(var3) #printing the dataframe