#Que1. Print each key
"""
d = {"Ravi" : 80, "Rohan": 33, "Chirag": 22, "Devraj":100}
#method 1
print(d.keys())

#method 2
for i in d:
    print(i)

#method 3
for key, value in d.items():
    print(key)
"""


#Que2. Print sum of all the marks
"""total = 0
for i in d.values():
    total += i
print(total)"""




#Que. Print Studnet who scored more than 80
"""for name , marks in d.items():
    if marks >= 80:
        print(name)
"""

#Que. Find and print the student with the highest marks using FOR LOOP ONLY.
"""d = {"Ravi" : 80, "Rohan": 33, "Devraj":100, "Chirag": 22}
top = "" 
highest = 0

for name, marks in d.items():
    if marks > highest:
        highest = marks
        top = name
print(top)
print(highest)"""





#Que. Create a dictionary of numbers and their Squares (1 to 5):
"""square = {}
for i in range(1,6):
    square[i] = i * i
print(square)"""


#Que. Add 5 bonus mark to every student
d = {"Ravi" : 80, "Rohan": 33, "Devraj":100, "Chirag": 22}
for i in d:
    d[i] = d[i] + 5
print(d)