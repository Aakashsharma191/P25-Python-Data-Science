#a = [34,12,89,45,67,12,78,23]

#list

#1) () Tuples
#2) [] List
#3) {} Set ,Dictionary

#list

#Hetrogenous nature - you can store multiple Data Types eg:-

'''a = ["Akash",28,True,15.5,print]'''

#indexing - same as string

#Mutsble Nature - you can change any value of your list

'''l = [10,20,30,40,50]

l[0] = 500
print(l)'''

#loops on list:

'''l = [10,20,30,40,50,99,189,7,56]

#loop on value
for i in l:
    if i % 2 ==0:
        print(i)'''


#loops on index:
l = [10,20,30,40,50,99,189,7,56]
for i in range(len(l)):
    print(f'{i} => {l[i]}')