'''def hello():
    print("Aakash sharma")
hello()'''  # calling


#parameters and arguments


#whenever we want to accept a value in a fuction you have 
#to use parameters

'''def addition(a,b): # parameters
    print(a+b)

#and whenever you want to provide values to those
#parameters you have to use arguments

addition(12,12) #positional arguments
addition(10,20)'''

'''#return 

def hello():
    return "Aakash sharma"

print(hello())
#print(a)'''


'''def strongnumber(a):
    num  = a
    sum = 0
    while a != 0:
        fact = 1
        for i in range(1,a%10+1):
            fact = fact * 1
        sum = sum + fact
        a //= 10
    if num == sum:
        print(num)

for i in range(1,100000):
    strongnumber(i)'''


#type of parameters and arguments

#default
#we have to provide a fefault value to  our parameters
#but it cannot be created before a normal parameter 

'''def addition(b = 10, c = 10):
    print(b+c)

addition(10)'''

#positional vs default argument
'''def xyz(a,b,c):
    print(a,b,c)
xyz(12,c = 20,b = 52)'''