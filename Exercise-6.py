li = []
n = int (input ("How many number you enter : "))
print ("Enter the numbers one by one ")
for i in range(n):
    x = int (input ())
    li.append (x)
print ("The minimum number : ", min(li))
print ("minimum number position : ", li.index(min(li))+1)
print ("The maximum number : ", max(li))
print ("maximum number position : ", li.index(max(li))+1)
