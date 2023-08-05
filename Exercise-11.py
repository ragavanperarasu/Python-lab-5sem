def bs(a):
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j + 1]
                a[j + 1] = t 
d = []
n = int(input("How many number you enter : "))
for i in range(n):
    d.append(int(input("Enter a number : ")))
print("Original list : ", d)
bs(d)
print("Sorted list : ", d)
