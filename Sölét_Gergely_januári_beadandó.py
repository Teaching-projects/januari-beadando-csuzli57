import random
def ctvasarlas():
    ctshop = {
        "usps": 200,
        "five-seven": 500,
        "desert eagle":700 ,
        "ssg08":1700, 
        "m4a1s": 3200,
        "AWP":4750
    }
    print(ctshop)
    vasarlas=input("Kérem irjon be egy fegyver nevét a fent láthatóak közül ")
    while vasarlas not in ctshop:
        vasarlas=input("Kérem helyesen irja be a fegyver nevét ")
    else:
        print("Sikeresen megvásároltad,",vasarlas, "ami",ctshop[vasarlas],"$-ba került")
        pénz2=pénz-int(ctshop[vasarlas])
        if pénz2<0:
            print("Nincsen elég pénze jöjjön vissza amikor már megvan az elegendő mennyiség")
        else:
            print(str(pénz2)+ "$-ja maradt")
def tvasarlas():
    tshop = {
        "glock18":200,
        "tec9": 500,
        "desert eagle":700 ,
        "ssg08":1700,
        "AK47": 2700,
        "AWP":4750
    }
    print(tshop)
    vasarlas=input("Kérem irjon be egy fegyver nevét a fent láthatóak közül ")
    while vasarlas not in tshop:
        vasarlas=input("Kérem helyesen irja be a fegyver nevét ")
    else:
        print("Sikeresen megvásároltad,",vasarlas, "ami",tshop[vasarlas],"$-ba került")
        pénz2=pénz-int(tshop[vasarlas])
        if pénz2<0:
            print("Nincsen elég pénze jöjjön vissza amikor már megvan az elegendő mennyiség")
        else:
            print(str(pénz2)+ "$-ja maradt")
ct="terrorelhárító"
t="terrorista" 
pénz=int(random.randint(200,5500))
választás=1

while választás!=ct and választás!=t:
    választás=input("Válasszon egy csapatot (terrorelhárító vagy terrorista) ")
if választás==ct:
    print("terrorelhárítót választott")
    print(str(pénz)+ "$-ja van")
    ctvasarlas()
elif választás==t:
    print("terroristát válaszott")
    print(str(pénz)+ "$-ja van")
    tvasarlas()