#vstup veku uzivatele

vek = int(input("Zadej svuj vek: "))
if vek >= 18:
    if  vek >= 65:
        print("Jses v duchodu")   
    else:
        print("Jsi plnolety")
else:
    if vek >= 0:
        print("Jsi neplnolety")
    else:
        print("Delas si srandu?")