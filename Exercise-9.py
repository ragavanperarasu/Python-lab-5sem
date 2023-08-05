lis = []
n = int (input ("How many strings you enter :"))
print ("Enter the words one by one")
for i in range (n):
    x = input ()
    lis.append(x)
print ("The longest word in the list {} is {}".format(lis, max(lis)))
