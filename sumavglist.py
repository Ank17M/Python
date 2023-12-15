n = int(input("Enter the number of elements: "))
a = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    a.append(element)

print("List:", a)

print("Sum = ",sum(a))
print("Average = ",sum(a)/n)
