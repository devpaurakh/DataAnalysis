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
print(var2) #printing the dataframe