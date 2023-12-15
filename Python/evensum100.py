a = 0
b = 0
for i in range(1,101):
    if(i%2==0):
        a = a+i
    if(i%2!=0):
        b = b+i
print("Sum of even number = ",a)
print("Sum of odd number = ",b)
