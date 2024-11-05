def isBalanced(num):
    even = True
    even_num = 0
    odd_num = 0
    for digit in num:
        if even:
            even_num += int(digit)
        else:
            odd_num += int(digit)
        even = not even
    if even_num == odd_num:
        return True
    else:
        return False