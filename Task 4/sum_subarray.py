# This is Task 4
""" 32. Find Subarray with Given Sum
 Objective   : Find a contiguous subarray whose sum equals a given value SSS.
 Input       : A list of integers and an integer SSS.
 Output      : The indices of the subarray or-1 if no such subarray exists.
 Hint        : Use the sliding window technique or prefix sums."""
def sum_of_subarray(a,target):
    left = 0
    cur_sum = 0
    for right in range(len(a)):
        cur_sum += a[right]
        while cur_sum > target and left <= right :
            cur_sum -= nums[left]
            left += 1
        if cur_sum == target:
            return [left,right]
    return -1
nums = [1, 2, 3, 7, 5]
target_sum = 12
result = sum_of_subarray(nums, target_sum)
print("Indices of subarray with sum", target_sum, ":", result)

