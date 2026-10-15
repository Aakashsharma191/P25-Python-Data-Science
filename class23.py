#list methods 


'''l = [10,20,30]

l.append(40)
print(l)
'''


'''l = [10,20,30,40]

b = l

b[0] = 200
print(l)'''


'''l = [10,20,30,40]

b = l.copy()   #copy se refrence jata hai maine data not change 

b[0] = 200
print(l)'''


'''a = [10,20,30,40,50]
b = []
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)''' # op [5,40,30,20,10]

'''a = [10,20,30,40,50]
a.reverse()
print(a)'''


a = [10,20,30,40,50,60,70,80,90,100]

temp = len(a)-1
for i in range(0,(len(a)-1)//2):
    a[i], a[temp] = a[temp],a[i]
    temp=temp-1

print(a)
