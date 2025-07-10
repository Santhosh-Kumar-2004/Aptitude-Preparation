# HCF (Highest Common Factor) or GCD (Greatest Common Divisor) of two numbers is the largest number that divides both numbers exactly.
# | Numbers | HCF (GCD) | Explanation                                   |
# | ------- | --------- | --------------------------------------------- |
# | 12, 18  | 6         | Common factors: 1, 2, 3, 6                    |
# | 8, 14   | 2         | Common factors: 1, 2                          |
# | 7, 13   | 1         | No common factor except 1 (they are co-prime) |

import math

def hcf(a, b):
    return math.gcd(a, b)

print(hcf(12, 18)) 
print(hcf(39, 45))
