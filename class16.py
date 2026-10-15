# fact torial nikala 145   sum nikala 145 

'''n = int(input("Enter your range :- "))
sum = 0
temp = n

while n != 0:
    ex = n % 10
    fact = 1
    for i in range(1,ex+1):
        fact *= i
    
    sum += fact

    n //= 10

print(sum)

if sum == temp:
    print("strong number ")
else:
    print("not a storng number ")  '''  


# Number guessing game (1-100)

'''import random

num = random.randint(1,100)

tries = 0

while True:
    tries += 1
    guess = int(input("guess your number 1 - 100 :- "))

    if guess == num:
        print(f"Congratulation you are win  and aapne kitne tries liye {tries}")
        break
    elif guess > num:
        print("Go  bit lower ")
    else:
        print("Go a bit Higher")'''

'''import random

num = random.randint(1,100)
tries = 0

while True:
    tries += 1
    guess =int(input("Guess your number 1 - 100  :- "))
    if guess == num:
        print(f"Congratulation you are win and your tries {tries} ")
        break
    elif guess > num:
        print("Go bit Lower ")
    else:
        print("Go bit Higher")'''


# fact torial nikala 145   sum nikala 145  check karna strong number / not strong number 

'''n = int(input("Enter your numbe :- "))
nn = n
sum = 0

while n != 0:
    ex = n %10
    fact = 1

    for i in range (1,ex+1):
        fact *= i
    sum += fact 
    n //= 10

print(f"Factorial sum = :- {sum}")

if sum == nn:
    print(f"Strong number {sum} = {nn}")

else:
    print(F"Not strong number {sum} = {nn}")'''


# Number guessing game (1-100)

'''import random
num = random.randint(1,200)
tries = 0
while True:
    guess = int(input("Enter your number 1-200 :- "))
    tries += 1
    if guess == num:
        print(f"You are win guessing game :- congratulation :  and your tries {tries}")
        break
    elif guess > num:
        print("Go bit Lower :")
    else:
        print("Go bit Higher")'''

# fact torial nikala 145   sum nikala 145  check karna strong number / not strong number 

'''n = int(input("Enter your number :- "))
nn = n
sum = 0

while n != 0:
    ex = n % 10
    fact = 1
    for i in range(1,ex+1):
        fact *= i
    sum += fact
    n //= 10
print(f"Sum of facts = {sum}")

if sum == nn:
    print(f"Strong Number {sum} = {nn}")
else:
    print(f"Not strong Number {sum} = {nn}")'''

# Number guessing game (1-1000)

'''import random
n = random.randint(1,1000)
tries = 0
while True:
    tries += 1
    guess =int(input("Enter your guessing number 1 - 1000 :-  "))
    if n == guess:
        print(f"You are win the guessing game congratulation :- your tries {tries}")
        break
    elif guess > n :
        print("Go bit a lower : ")
    else:
        print("Go bit a higher : ")'''

# fact torial nikala 145   sum nikala 145  check karna strong number / not strong number

'''n = int(input("Enter your number :- "))
nn = n
sum = 0
while n != 0:
    ex = n % 10
    fact = 1
    for i in range(1,ex+1):
        fact *= i
    sum += fact
    n //= 10
print(f"sum of factes {sum}")

if sum == nn:
    print(f"Stron number = {sum} = {nn}")
else:
    print(f"not strong number = {sum} = {nn}")'''


'''n = int(input("Enter your number :- "))
nn = n
sum = 0
while n != 0:
    ex = n % 10
    fact = 1
    for i in range(1,ex+1):
        fact*=i
    sum += fact
    n //= 10
print(f"Sum of facters :-  {sum}")

if sum == nn:
    print(f"Strpng number :-  {nn} = {sum}")
else:
    (f"Not strong number :-  {nn} = {sum}")'''


'''import random
num = random.randint(1,100)
tries = 0
while True:
    tries += 1
    guess = int(input("Enter your Guessing number 1 - 100 :- "))
    if num == guess:
        print(f"congratulation you are win and your count {tries}")
        break
    elif guess > num :
        print(f"Go bit a Lower :- ")
    else:
        print(f"Go bit a Higher")'''