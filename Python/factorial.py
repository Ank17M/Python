def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number a positive integer : "))
print("Factorial:", factorial(number))
