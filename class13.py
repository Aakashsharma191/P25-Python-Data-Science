# hcf 

a = int(input("Enter number :-"))
b = int(input("Enter number :-"))
if a > b:
    for i in range(b,0,-1):
        if b % i ==0 and a % i ==0:
            print(f"hcf- {i}")
            break
elif b > a:
    for i in range(a,0,-1):
        if a % i ==0 and b % i ==0:
            print(f"hcf- {i}")
else:
    print(f"hcf- {a}")


# seprate the digits of - 5379

'''num = int(input("Enter your number :-"))
while num > 0:
    print(num%10)
    num = num //10'''


