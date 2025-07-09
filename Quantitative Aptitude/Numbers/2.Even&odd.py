def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(10))
print(even_odd(15))

#Using Loop
for i in range(1, 21):
    print(f"{i} is {even_odd(i)}")