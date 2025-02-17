# This is Task 4
""" 26. Check Balanced Parentheses
 Objective      : Check if a string of parentheses ((), {}, []) is balanced.
 Input          : A string of parentheses.
 Output         : True if balanced, otherwise False.
 Hint           : Use a stack to match opening and closing parentheses."""
def is_balanced(s):
    stack = []
    bracket_map = {
        ')':'(' , ']':'[' , '}':'{'
    }
    for i in s:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack or stack.pop() != bracket_map[i]:
                return False
    return len(stack) == 0
print(is_balanced('{()}'))