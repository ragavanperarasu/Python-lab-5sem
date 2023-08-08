# Print prime number given range
s = int(input("Enter starting value : "))
e = int(input("Enter ending value : "))
s = 2 if s == 1 else s
for i in range(s, e + 1):
    for j in range(2, i):
        if i % j == 0: break
    else: print(i, end = ", ")

