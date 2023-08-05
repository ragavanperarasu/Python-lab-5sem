def  fib (n):
    if n <= 1 : return n
    else : return (fib (n - 1) + fib (n - 2))

n = int (input ("Enter any number : "))

if n <= 0:
    print ("Please enter a Positive number")
else:
    print ("Fibonacci sequence")
    for i in range (n): print (fib (i))
