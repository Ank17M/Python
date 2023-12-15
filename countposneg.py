nu = int(input("Enter number of elements : "))
a = []
p = 0
n = 0
for i in range(nu):
    el = int(input(f"Enter element {i + 1} : "))
    a.append(el)

print("List : ", a)

for i in a:
    if i>=0:
        p+=1
    else:
        n+=1
        
print("Positive Elements = ",p)
print("Negative Elements = ",n)
