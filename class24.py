# n = int(input("Enter your number :- "))
# nn = n
# sum = 0
# while n != 0:
#     ex = n % 10
#     fact = 1
#     for i in range(1,ex+1):
#         fact *= i
#     sum += fact
#     n //=10
# if nn == sum:
#     print(f"strong number {nn} = {sum}")
# else:
#     print(f" not strong number {nn} = {sum}")


# n = int(input("Enter your number "))
# nn = n
# rev = 0
# while n != 0:
#     rev = rev * 10 + n %10
#     n //=10
# if nn == rev:
#     print(f"palindrome number {nn} = {rev}")
# else:
#     print(f" not palindrome number {nn} = {rev}")

# n = int(input("Enter your number "))
# nn = n
# sum = 0
# ex = len(str(n))
# while n != 0:
#     ex =  n % 10
#     sum = sum + ex ** ex
#     n //= 10
# if nn == sum:
#     print(f"amstrong number {sum} = {nn}")
# else:
#     print(f"not amstrong number {sum} = {nn} ")

# n = int(input("Enter your number : - "))

# for j in range(2,n+1):

#     for i in range(2,(j//2) +1):
#         if j % i == 0:
#             break
#     else:
#         print(j)


'''n = int(input("Enter your number :- "))
for  i in range(2,n+1):
    for j in range(2,(i//2)+1):
        if i % j == 0:
            break
    else:
        print(i)
'''

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
if sum == nn:
    print(f"Strong number :- {nn} = {sum}")
else:
    print(f"Not Strong number :- {nn} = {sum}")'''


'''n = int(input("Enter your number "))
nn = n
sum = 0

while n != 0:
    sum = sum * 10 + n % 10
    n //= 10
if nn == sum:
    print(f"palindrome number :- {nn} = {sum}")
else:
    print(f"not palindrome number :- {nn} = {sum}")'''

'''n = int(input("Enter your  number :- "))
nn = n
ex = 0

while n != 0:
    ex = ex *10 + n % 10
    n //= 10

if nn == ex:
    print("palindrome number ")
else:
    print("not palindrome number ")'''


'''n = int(input("enter your number "))
for i in range(2,n+1):
    for j in range(2,(i//2)+1):
        if i % j == 0:
            break
    else:
        print(i)'''

n = int(input("Enter your number :- "))
sum = 0
nn = n
while n != 0:
    fact = 1
    ex = n % 10
    for i in range(1,ex+1):
        fact *= i
    sum += fact
    n //= 10
if nn == sum:
    print("strong number")
else:
    print("not strong number ")