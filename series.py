import pandas as pd

a = [3,4,5,6,7,8,9]
var = pd.Series(a, index=['a','b','c','d','e','f','g'], dtype="float", name='python') #creating a series with index
# print(var) #printing the series
# print(type(var)) #printing the type of the series

# print(var[0]) #printing the first element of the series                                 


dic = {"name":['python', 'c', 'c++','java'] , "popularity":[1,2,3,4], "year":['1991','1972','1983','1995']} #creating a dictionary

var1 = pd.Series(dic)
# print(var1)
# print(type(var1)) #printing the type of the series


s= pd.Series(12,index=[1,2,3,4,5,6,7]) #creating a series with scalar value
s1= pd.Series(12,index=[1,2,3,4]) #creating a series with scalar value
# print(s)

print(s+s1) #adding two series

