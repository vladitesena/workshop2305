#vytvoreni seznamu 
seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #seynam cisel
seznam_str = ["ahoj", "svete", "jak", "se", "mas"] #seynam string

print(seznam)

print(seznam[2]) #3 prvek ze seznamu
print(seznam_str[2])

print(seznam[9])
print(seznam[-1])

print(seznam[8])
print(seznam[-2])

delka = len(seznam_str)
print("Delka seznamu je: ", str(delka))

seznam_str.append("dnes")
seznam.append(0)

print(seznam)
print(seznam_str)

seznam.sort()
print(seznam)

seznam_str.sort()
print(seznam_str)

seznam[-1] = 100
print(seznam)

seznam_str[0] = "Nazdar"
print(seznam_str)

del seznam_str[1]
print(seznam_str)

seznam_str.insert(1, "jabadabadu")
print(seznam_str)
