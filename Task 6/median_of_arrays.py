# This is task 6
""" 43. Find the Median of Two Sorted Arrays
 Objective    : Find the median of two sorted arrays.
 Input        : Two sorted lists.
Output        : The median value of the two lists.
 Hint         : Use binary search or merge the two arrays and find the median."""

def find_median(a,b):
    merged_array = sorted(a+b)
    n = len(merged_array)

    if n % 2 == 1:
        return merged_array[n//2]
    else :
        return (merged_array[n//2 -1]+merged_array[n//2])
nums1 = [1, 3]
nums2 = [2]
print(find_median(nums1, nums2))