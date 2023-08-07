# Find GCD of two
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
a1 = a # temp
b1 = b # temp
while b != 0:
    t = b
    b = a % b
    a = t
print("The GCD of {} and {} is {}".format(a1, b1, a))
