def factorial(x):
    if x < 1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))

