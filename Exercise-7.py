li = []
n = int (input ("How many number you enter : "))
print ("Enter the elements one by one")
for i in range(n):
    x = int (input ())
    li.append (x)
print ("The original list is : ", li)
li.reverse()
print ("The reversed list is : ", li)
