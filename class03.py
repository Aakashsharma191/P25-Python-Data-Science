#Type Conversion
#1)int()
#2)float()
#3)str()
#4)bool()

#When you want to convert one data type into another data type you have to use type conversion.

a=12
a=str(a)
print(type(a))

# a=12.12
# a=int(a)
# print((a))

# a=None

# a=bool(a)
# print(a)
#int float string are the basic but if we talk about the bool.
#7 false values in python are:- 0,0.0,"",None,False,[],(),{}

#Input and output statements
#for providing the output you have only one thing and that is print() function.
# a=input("Enter your name:-")
# print("Your name is:-",a)
# name="Saurabh"
# age=20
# #first way of providing output
# print("My name is:-",name,"and my age is:-",age)
# #second way of providing output
# # print("My name is:- {} and my age is:- {}".format(name,age))
# # #third way of providing output
# print(f"My name is:- {name} and my age is:- {age}")
# #f-String is a way to provide the output in a formatted way.


#inputs are simple but make sure to have the right data type while taking the inputs
# Name=input("What is your name:-")
# Age=int(input("What is your age:-"))
temp=eval(input("What is your temperature:-"))
# print(Name)
# print(Age)
print(type(temp))
#eval function is used to evaluate the expression inside the string and return the result.
