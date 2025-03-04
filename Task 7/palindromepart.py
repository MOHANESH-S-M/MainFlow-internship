# This is Task 7
"""54. Palindrome Partitioning
 Objective   : Partition a string such that every substring is a palindrome.
 Input       : A string.
 Output      : A list of lists of palindromic partitions.
 Hint        : Use backtracking to explore all possible partitions."""
def is_palindrome(s):
    return s == s[::-1]

def partition_helper(s, start, path, result):
    if start == len(s):  # If we reach the end, store the partition
        result.append(path[:])
        return
    
    for end in range(start, len(s)):
        substring = s[start:end + 1]
        if is_palindrome(substring):  # Check if the substring is a palindrome
            path.append(substring)
            partition_helper(s, end + 1, path, result)  # Recur for the next part
            path.pop()  # Backtrack

def palindrome_partition(s):
    result = []
    partition_helper(s, 0, [], result)
    return result

# Example usage:
s = "aab"
print(palindrome_partition(s))
