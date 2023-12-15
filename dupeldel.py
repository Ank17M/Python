nel = int(input("Enter number of elements : "))
alist = []

for i in range(nel):
    ele = int(input(f"Enter element {i + 1} : "))
    alist.append(ele)
    
print("List : ", alist)

for i in alist:
    if(alist.count(i)>1):
        alist.remove(i)

print("Duplicate Removed List : ",alist)

