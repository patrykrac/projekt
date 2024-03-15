# Przygotuj sobie array/obiekt z wszystkimi planetami i wartością grawitacji. Dzięki temu będziesz mógł dodawaać kolejne wartości do obiektów i nie będziesz musial użwyać tyle is'ów.

waga = float(input("podaj swoją wagę: "))
planeta = input("podaj planetę gdzie chciałbyś się znaleźć: ").capitalize()
if planeta == "Merkury":
    print(f"Twoja waga tam to {waga*0.378}")
elif planeta == "Wenus":
    print(f"Tam ważysz {waga * 0.907}")
elif planeta == "Mars":
    print(f"Tam ważysz {waga * 0.377}")
elif planeta == "Jowisz":
    print(f"Tam ważysz {waga * 2.528}")
elif planeta == "Saturn":
    print(f"Tam ważysz {waga * 1.064}")
elif planeta == "Uran":
    print(f"Tam ważysz {waga * 0.889}")
elif planeta == "Neptun":
    print(f"Tam ważysz {waga * 1.125}")
elif planeta == "Księżyc":
    print(f"to nie planeta... ale jak już pytasz to tam ważysz{waga * 0.166}")
else: print("w naszym układzie planetarnym nie ma takiej planety")
