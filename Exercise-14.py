d = {1001:"Ramu", 1002:"Babu", 1003:"Kumar"}
print("Original dictionary : ", d)
print("Length : ", len(d))
print("Copied : ", d.copy())
print("removed 1002 : ", d.pop(1002))
print("After removed : ", d)
print("Value of 1001 : ", d.get(1001))
print("Key & Value : ", d.items())
print("Value : ", d.values())
print("Remove last element : ", d.popitem())
d.clear()
print("After clear dictionary : ", d)
