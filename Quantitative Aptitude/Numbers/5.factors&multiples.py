# A factor (or divisor) of a number n is any number that divides n exactly with no remainder.
    # Example: Factors of 12 → 1, 2, 3, 4, 6, 12
    # Because: 12 % 1 = 0, 12 % 2 = 0, ...

# Multiple:
#     A multiple of n is any number that can be written as n × k, where k is an integer.
#     Example: Multiples of 4 → 4, 8, 12, 16, 20, ...

#Factor Program
def find_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

print(find_factors(36)) 

#Multiple Program
def generate_multiples(n, count):
    return [n * i for i in range(1, count + 1)]

print(generate_multiples(4, 10))  
