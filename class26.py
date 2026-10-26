#Find the missing number 
#input: [1,2,4,5,7,3]

'''l = [1,2,4,5]
n = len(l)
og = n + 1
# og_sum = ((og)*(og + 1))//2
og_sum = 0
real_sum = 0

for i in range(1,og+1):
    og_sum += i
for elem in l:
    real_sum += elem
missing = og_sum - real_sum
print(missing)'''


#check whether a list is sorted or not 

# check if the list elements are 
# arranged in ascending order 

#example : 
#input: [20,10,40,50,30]
#output: list is sorted 

'''l = [10,20,30,40,50]
n = len(l)

is_sorted = True
for i in range(0,n-1):
    if l[i] > l[i+1]:
        is_sorted = False
        break
if is_sorted:
    print("List is sorted ")
else:
    print("list is not sorted")'''


#palindromic list

#check whether the list 
#reads the same from front and check

#example
# input [2,3,15,15,3,2]
#output : pa;indromic list

'''l = [2,3,15,15,3,2]
palindrome = True
n = len(l)
for i in range(n//2):
    if l[i] != l[n-i-1]:
        palindrome = False
        break
if palindrome:
    print("palindrome number ")
else:
    print("not palindrome ")'''


'''l = [10,20,30,40,50]
nn = len(l)
s = True
for i in range(1,nn-1):
    if l[i] > l[i+1]:
        s = False
        break

if s:
    print("sorted")
else:
    print("not sorted")
'''

#Find the missing number 
#input: [1,2,4,5,7,3]
 
'''l = [1,2,4,5,6,3]
n = len(l)
og = n + 1
# og_sum = ((og)*(og + 1))//2
og_sum = 0
real_sum = 0

for i in range(1,og+1):
    og_sum += i
for elem in l:
    real_sum += elem
missing = og_sum - real_sum
print(missing)'''


'''l = [1,2,4,5,6,3]
length = len(l)
og = length + 1
sum1 = 0
real_sum = 0
for i in range(1,og+1):
    sum1 += i
for elem in l:
    real_sum += elem
missing = sum1 - real_sum 
print(missing)'''

'''l = [1,2,3,5,7,6]
lent = len(l)+1
sum = 0
real_sum = 0
for i in range(1,lent+1):
    sum += i
for elem in l:
    real_sum += elem
missing = sum - real_sum
print(missing)
'''

'''l = [1,2,3,5,6,4,8]
length = len(l)+1
sum1 = 0
real_sum = 0
for i in range(length+1):
    sum1 += i
for elem in l:
    real_sum += elem
print(f"list {sum1 - real_sum}")'''



#check whether a list is sorted or not 

# check if the list elements are 
# arranged in ascending order 

#example : 
#input: [10,20,30,40,50]
#output: list is sorted 

'''l = [10,20,30,40,50]
length = len(l)
sorteds =True
for i in range(0,length-1):
    if l[i]>l[i+1]:
        sorteds = False
        break
if sorted:
    print("list is sorted")
else:
    print("list is not sorted")'''

#palindromic list

#check whether the list 
#reads the same from front and check

#example
# input [2,3,15,15,3,2]
#output : pa;indromic list

'''l = [1,1,2,15,15,2,1,1]
length = len(l)
palindrome = True
for i in range(length//2):
    if l[i] != l[length-i-1]:
        palindrome = False
        break
if palindrome:
    print("yes palindrome number ")
else:
    print("no palindrome number ")'''


'''l = [1,2,4,5,7,3]
length = len(l)
sum = 0
real_sum = 0
for i in range(1,length+1+1):
    sum += i
for elem in l:
    real_sum += elem
missing = sum - real_sum
print(missing)
'''

'''l = [1,1,1,2,2,5,2,2,1,1,1]
length = len(l)
palindrome = True
for i in range(length//2):
    if l[i] != l[length-i-1]:
        palindrome = False
if palindrome:
    print("palindrome number ")
else:
    print("no palindrome number")'''


'''l = [10,20,30,40,50]
sortedd = True
for i in range(len(l)-1):
    if l[i] > l[i+1]:
        sortedd = False
if sortedd:
    print("sorted")
else:
    print("no sorted")'''