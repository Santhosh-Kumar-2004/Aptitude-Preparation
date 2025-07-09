# An Armstrong Number (also called a Narcissistic Number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    total = sum([d ** power for d in digits])
    return total == n

print(is_armstrong(153))   
print(is_armstrong(123))   
