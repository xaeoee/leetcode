def isValid(s):
    stack = []
    opening_brackets = ["{", "(", "["]
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        else:
            if not stack:
                return False
            if stack[-1] == bracket_pairs[char]:
                stack.pop()
            else:
                return False
        
    return len(stack) == 0
    

        



