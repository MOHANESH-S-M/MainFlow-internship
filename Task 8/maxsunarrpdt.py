# This is Task 8
""" 59. Maximum Subarray Product
 Objective   : Find the maximum product of a contiguous subarray in an array of integers.
 Input       : A list of integers.
 Output      : The maximum product of the subarray.
 Hint        : Use dynamic programming, considering both the maximum and minimum product
               up to each element."""
def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = min_product = result = nums[0]

    for num in nums[1:]:
        temp_max = max(num, max_product * num, min_product * num)
        min_product = min(num, max_product * num, min_product * num)
        max_product = temp_max
        result = max(result, max_product)

    return result
print(max_product_subarray([-2, 3, -4]))