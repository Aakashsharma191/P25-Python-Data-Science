'''
DICTIONARY
1.Annoted By {curly brackets}
2.Dictionary is combination multiple keys : values
3.Dictionary are Mutable.
4.Dictionary are Hetrogenous 
5.Dictionary are ordered
6.In Dictionary keys will always be UNIQUE but value can be duplicate 
'''
# d = {} #Empty Dictionary

'''d = {1:10,2:20,3:30}
d [3] = 100
print(d[3])
'''
'''d ={1:10,2:20,3:30,4:40,2:500}
print(d)'''

'''d ={1:10,2:20,3:30,4:40}#5:50
d[5] = 50#Creating new key and assigning value.
print(d)'''

#Agar hum direct loop run krte hai 
# Dictionar pe tho we will get Keys.

'''d = {1:10,2:20,3:30,4:40}
for i in d:
    print(i,d[i])'''

#Methods in Dictionary
#1. Kyes
#To print or give only and only keys from the dict.
'''d = {1:10,2:20,3:30,4:40}
print(d.keys())'''
#2. values()
#Will give all the values from the Dictionary.
'''d = {1:10,2:20,3:30,4:40}
print(d.values())'''

#3. Items()
#it will give both kyes and values from the Dictionary
'''d = {1:10,2:20,3:30,4:40}
print(d.items())'''

'''d = {1:10,2:20,3:30,4:40}
for key,vlaue in d.items():
    print(key,vlaue)'''

#4. pop (key) -> remove the key and value from the dict.
d = {1:10,2:20,3:30,4:40}
d.pop(3)
print(d)