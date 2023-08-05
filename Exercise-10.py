lis = []
n = int(input("How many numbers you enter : "))
for i in range (n):
    lis.append(int(input("Enter a number : ")))
s = int (input ("Enter search value : "))
for i in range(n):
    if s == lis[i]:
        print ("Value Found {} position {}".format(lis[i],i))
        break
else:
    print ("Not Found")
