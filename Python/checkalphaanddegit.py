st = '1234, to-play-games'
a = 0
d = 0
for val in st:
    if val.isalpha():
        a = a+1
    if val.isdigit():
        d = d+1
print(f"Alphabet = {a}")
print(f"Digit = {d}")
