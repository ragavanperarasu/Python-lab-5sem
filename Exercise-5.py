st = input ("Enter a string : ")
s1 = st
length = len (st)
if length >= 3 :
    if st[-3:] == "ing":
        st += "ly"
    else:
        st += "ing"
print ("The given string is : ", s1)
print ("The modified string is : ", st)
