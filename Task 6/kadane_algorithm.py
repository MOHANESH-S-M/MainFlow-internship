# This is Task 6
""" 45. Largest Sum Contiguous Subarray (Kadane's Algorithm)
 Objective    : Find the largest sum of a contiguous subarray in an array of integers.
 Input        : A list of integers.
 Output       : The maximum sum of the subarray.
 Hint         : Use Kadane’s Algorithm which runs in linear time."""
def largest_sum(list1):
    max_sum = float('-inf')
    cur_sum = 0

    for i in range(len(list1)):
        cur_sum += list1[i]
        max_sum = max(cur_sum,max_sum)

        if cur_sum < 0 :
            cur_sum = 0
    return max_sum
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(largest_sum(arr))