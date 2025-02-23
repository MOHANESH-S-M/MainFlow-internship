# This is Task 4
""" 37. Find K Largest Elements
 Objective       : Find the kkk largest elements in a list.
 Input           : A list of integers and an integer kkk.
 Output          : A list of the kkk largest integers.
 Hint            : Use a heap or sort the array and select the last kkk elements"""
def get_k_largest_numbers(list1,k):
    n = len(list1)
    for i in range(n):
        for j in range(n-i-1):
            if list1[j] < list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return list1[:k]
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(get_k_largest_numbers(nums, k)) 