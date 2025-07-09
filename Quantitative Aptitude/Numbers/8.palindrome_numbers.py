# A Palindrome Number is a number that reads the same forward and backward.

def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome(121))  
print(is_palindrome(123))  
