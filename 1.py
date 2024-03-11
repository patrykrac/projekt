import requests
import json

kuplubsprze = input("Chcesz kupić czy sprzedać: ")
waluta = input("jaką walutę: ")
# Rozdziel logikę pobierania kursów walut, interakcję z użytkownikiem i obliczenia na oddzielne funkcje.
response = requests.get("http://api.nbp.pl/api/exchangerates/rates/A/USD/")
rusd = response.json()["rates"]
usd = float(rusd[0]["mid"])
response = requests.get("http://api.nbp.pl/api/exchangerates/rates/A/EUR/") #Użyj stałych dla URLi i lepszych nazw zmiennych.
reur = response.json()["rates"]
eur = float(reur[0]["mid"])
response = requests.get("http://api.nbp.pl/api/exchangerates/rates/A/GBP/")
rgbp = response.json()["rates"]
gbp = float(rgbp[0]["mid"])
# Dodaj obsługę błędów dla żądań HTTP i konwersji danych.

if kuplubsprze == "kupić":
    hajs = float(input("za ile chcesz kupić: "))
    if waluta == "usd":
        print(f"kupisz za to {round(hajs/usd, 2)} dolarów")
    elif waluta == "eur":
        print(f"kupisz za to {round(hajs/eur, 2)} euro")
    elif waluta == "gbp":
        print(f"kupisz za to {round(hajs/gbp, 2)} funciaków")
    else: print("coś zepsułeś")
elif kuplubsprze == "sprzedać":
    hajs = float(input("ile chcesz sprzedać: "))
    if waluta == "usd":
        print(f"dostaniesz {round(hajs*usd, 2)} polskich złociszy")
    elif waluta == "eur":
        print(f"otrzymsz {round(hajs*eur, 2)} polskiego złotego")
    elif waluta == "gbp":
        print(f"dostaniesz {round(hajs*gbp, 2)} zł, więc na browara może wystarczy")
    else: print("coś zepsułeś")
# Zminimalizuj powtarzanie kodu przez wykorzystanie funkcji.
