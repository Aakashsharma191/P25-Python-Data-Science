
# Print List Elements in Reverse Order
#
# Reverse the list using the two-pointer approach.
#
# Example:
# Input: [10, 20, 30, 40, 50]
# Output: [50, 40, 30, 20, 10]

'''arr = [10, 20, 30, 40, 50]
n = len(arr)
mid = n//2
for i in range(mid):
    arr[i] , arr[n-i-1] = arr[n-i-1] ,arr[i]'''







# Print Positive and Negative Elements of a List
#
# Print positive and negative elements separately.
# Ignore zero.
#
# Example:
# Input: [10, -5, 20, -3, 0, 8][10, -5, 20, -3, 0, 8]
# Output:
# Positive: 10 20 8
# Negative: -5 -3

'''arr = [10, -5, 20, -3, 0, 8]

print("positive:")
for elem in arr:
    if elem>0:
        print(elem)
        
print("negative: ")
for elem in arr:
    if elem<0:
        print(elem)'''
        


# Mean of List Elements
#
# Calculate the average of all elements in a list.
#
# Example:
# Input: [10, 20, 30, 40]
# Output: Mean = 25.0


'''list = [10, 20, 30, 40]
n = len(list)
sum =0
for elem in list:
    sum+=elem
print(f"mean is {sum/n}")'''
    

# Find the Greatest Element and Its Index
#
# Find the greatest element and 
# print its index.
#
# Example:
# Input: [2, 96, 69, 77, 145, 20]
# Output: Max element = 145 
# found at 4 index

arr =[2, 96, 69, 77, 145, 20]
max = arr[0]
index =0
for i in range(1,len(arr)):
    elem = arr[i]
    if elem > max:
        max = elem
        index = i
    
print(f"max is {max} at index {index}")