# 1 is neither prime nor composite
# The smallest prime number is 2 (also the only even prime)

# n ** 0.5 = Gives the Square root of n

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))

def check_prime(st, en):
    return [n for n in range(st, en + 1) if is_prime(n)]

print(check_prime(2, 11))