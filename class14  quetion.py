'''n = int(input("enetr your number "))
if n % 3 ==0 and n % 5 ==0:
    print("disble by 3 and 5")
else:
    ("not disble by 3 and 5")'''


'''n = int(input("enter your number "))
for i in range(2,n//2+1):
    if n%i==0:
        print("  not prime")
        break
else:
    print(" prime")'''

'''n = int(input("Enter number :-"))
num = int(input("Enter number :-"))
if n > num:
    for i in range(num,0,-1):
        if num % i ==0 and n % i ==0:
            print(f"hcf- {i}")
            break
elif num > n:
    for i in range(n,0,-1):
        if n % i ==0 and num % i ==0:
            print(f"hcf- {i}")
else:
    print(f"hcf- {n}")'''

'''num = int(input("Enter your number :-"))
count =0
while num > 0:
    print(num%10)
    count +=1
    num //=10
print(f"count of digit {count}")'''


# n = int(input("enetr your number :-"))
# n1 = int(input("enetr your number :-"))
# if n1 > n:
#     for i in range(n1,0,-1):
#         if n1 % i ==0 and n % i ==0:
#             print(f"hcf  :- {i}")
#             break
# elif n > n1:
#     for i in range(n,0,-1):
#         if n % i ==0 and n1 % i ==0:
#             print(f"hcf  :- {i}")
# else:
#     print(f"hcf  {n}")
