#DataFrame

import pandas as pd
z = [1,2,3,4,5,6,7,8,9] #creating a list
a = pd.DataFrame(z)#creating a dataframe
# print(a)
# print(type(a)) #printing the type of the dataframe

b = {"name":['python', 'c', 'c++','java'] , "popularity":[1,2,3,4], "year":['1991','1972','1983','1995']} #creating a dictionary
#var = pd.DataFrame(b) #creating a dataframe
# var = pd.DataFrame(b, columns=['name',"year"], index=['a','b','c','d']) #creating a dataframe with columns and index
# print(var)
# print(var['name']) #printing the column with name 'name'
var = pd.DataFrame(b)

#print(var["name"][3]) #printing the value of the 3rd row of the column with name 'name'


list_1 = [[1,2,3,4,5],[22,4,55,4,3]] #creating a list of lists 2d list 

var_2 = pd.DataFrame(list_1)
#print(type(var_2))
#print(var_2)


##Creating a DataFrame from a dictionary of series

sr = {'s':pd.Series([1,2,3,4]), 's1':pd.Series([4,3,2,1])} #creating a dictionary of series

var_3= pd.DataFrame(sr) #creating a dataframe

#print(var_3) #printing the dataframe
#print(type(var_3)) #printing the type of the dataframe

