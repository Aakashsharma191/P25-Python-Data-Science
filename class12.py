#print the number from 1 - 20
'''for i in range(1,21):
    if i%2==0:
        continue
    print(i)'''

#prime number and composite number

'''n = int(input("enetr your number :-"))

for i in range(2,n//2+1):
    if n % i ==0:
        print("composite number")
        break
else:
    print("prime number")'''


n = int(input("enetr your range :-"))

for j in range(2,n+1):

    for i in range(2,(j//2) +1 ):
        if j % i == 0:
            break
    else:
        print(j)







