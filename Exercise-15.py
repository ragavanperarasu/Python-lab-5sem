with open ("file1.txt","w+") as f:
    print("Enter your content (Double enter for exit)")
    while True:
        g = input()
        if g == "": break
        else : f.write(g+"\n")
        
with open ("file1.txt","r") as f:
    s = f.read()
    print("File1 content :\n", s)
    with open ("copy.txt", "w") as c:
        c.write(s)
        
with open ("copy.txt", "r") as c:
    print("Copy file content :\n", c.read())
