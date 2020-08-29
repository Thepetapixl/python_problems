# Accept an array of n numbers and an integer k
# Print length of array after removing sub-array of elements
# such that number of elements greater than k is equal to number of elements less than k
# Only one deletion allowed
# the sub array to be removed should be continuous set of numbers in the array
# if deletion is not possible then print 0

# Ex: {4, 11, 4, 1, 6, 5}, k = 4
# Result = 4  (remove 6,5)

# Ex: {1, 2, 3, 7, 4, 5}, k = 6
# Result = 0
# Explanation- we need to remove 4 numbers to satisfy the condition
# But only 3 continuous numbers exist that are less than k
# Therefore 2 deletions will be required which is not allowed

arr = []

elements = int(input("Enter Number of elements "))
k = int(input("Enter value of k "))

print("Enter elements")
for i in range(0, elements):
    num = int(input())
    arr.append(num)


prev_gk = None
gk = 0
lk = 0
cont_gk = 0
cont_lk = 0
high_count_gk = 0
high_count_lk = 0

for i in arr:
    if i > k:
        if cont_lk > high_count_lk:
            high_count_lk = cont_lk
        if prev_gk is None or prev_gk:
            cont_gk += 1
        if not prev_gk:
            cont_gk = 1
        gk += 1
        prev_gk = True
        cont_lk = 0
    elif i < k:
        if cont_gk > high_count_gk:
            high_count_gk = cont_gk
        if prev_gk:
            cont_lk = 1
        if prev_gk is None or not prev_gk:
            cont_lk += 1
        lk += 1
        prev_gk = False
        cont_gk = 0

    elif i == k:
        if cont_gk > high_count_gk:
            high_count_gk = cont_gk
        elif cont_lk > high_count_lk:
            high_count_lk = cont_lk
        cont_gk = 0
        cont_lk = 0
        prev_gk = None

if cont_gk > high_count_gk:
    high_count_gk = cont_gk
elif cont_lk > high_count_lk:
    high_count_lk = cont_lk

diff = abs(gk-lk)

# print("CONTINUOUS GREATER THAN K: "+str(high_count_gk))
# print("CONTINUOUS LESS THAN K: "+str(high_count_lk))

if gk > lk:
    if diff <= high_count_gk:
        print(len(arr) - diff)
    else:
        print(0)

elif lk > gk:
    if diff <= high_count_lk:
        print(len(arr) - diff)
    else:
        print(0)
