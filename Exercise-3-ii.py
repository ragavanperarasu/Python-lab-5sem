st = input("Enter a string : ")
v = c = s = 0
st = st.lower()

for i in st:
    k = ord(i)
    if k >= 65 and 90 <= k:
        c += 1
        if i in "aeiou": v += 1
    else : s += 1
    
print ("Vowels : ", v)
print ("Character : ", c)
print ("Space : ", s)
