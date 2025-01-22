# This is Task 2 question no 13
""" 13. Sort a List
 Objective  : Sort a list of numbers in ascending order.
 Input      : A list of integers.
Output      : A sorted list.
 Hint       : Use sorting algorithms like bubble sort, selection sort, or simply sorted()."""
def bubble_sort(list1):
    n = len(list1)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
                swapped =True
        if swapped == False:
            break
    return list1
def selection_sort(arr):
    n= len(arr)
    for i in range (n):
        min_index = i
        for j in range(i+1, n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
def sorted_method(arr):
    return sorted(arr)
    
print(bubble_sort([34,43,2,1,3,667,6,64,3,3,6,89,6,4]))
print(selection_sort([34,43,2,1,3,667,6,64,3,3,6,89,6,4]))
print(sorted_method([34,43,2,1,3,667,6,64,3,3,6,89,6,4]))