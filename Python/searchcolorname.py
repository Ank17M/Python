color_name = ['Red','Green','Blue']
name = input("Enter the color name to search : ")
for c in color_name:
    if name == c:
        printf(f"color name {c} found in list")
        break
else:
    printf("Color name not found in list")
