# A Perfect Number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
# A proper divisor is a number that divides it exactly but is not equal to the number itself.

# Ex: 
#     6
#     Divisors: 1, 2, 3
#     Sum = 1 + 2 + 3 = 6 

def is_perfect(n):
    sum_of_divisors = sum([i for i in range(1, n) if n % i == 0])
    return sum_of_divisors == n

print(is_perfect(6))   
print(is_perfect(28))   
print(is_perfect(12))   


