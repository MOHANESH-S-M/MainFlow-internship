# This is Task 7
""" 47. Count Inversions
 Objective   : Count the number of inversions in an array, where an inversion is when
               a[i]>a[j]a[i] > a[j]a[i]>a[j] for i<ji < ji<j.
 Input       : A list of integers.
 Output      : The count of inversions.
 Hint        : Use a modified merge sort to count inversions during the merge step."""
def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Left subarray
    j = mid + 1 # Right subarray
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # Count inversions
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    
    return inv_count

def count_inversions(arr):
    temp_arr = arr.copy()
    return merge_sort(arr, temp_arr, 0, len(arr) - 1)

def merge_sort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort(arr, temp_arr, left, mid)
        inv_count += merge_sort(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    return inv_count

# Example
arr = [8, 4, 2, 1]
print("Number of inversions:", count_inversions(arr))
