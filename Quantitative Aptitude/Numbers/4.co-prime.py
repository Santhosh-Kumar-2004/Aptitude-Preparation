# GCD of two numbers is the largest number that divides both of them exactly.
# GCD and HCF are the same thing.

# What are Co-Prime Numbers?
    # Two numbers are co-prime if their GCD is 1.
    # That means they don’t share any factor other than 1.

import math

def is_co_prime(a, b):
    return math.gcd(a, b) == 1

print(is_co_prime(19, 23))