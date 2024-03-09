import requests
import json

kuplubsprze = input("Chcesz kupić czy sprzedać: ")
waluta = input("jaką walutę: ")

response = requests.get("http://api.nbp.pl/api/exchangerates/rates/A/USD/")
rusd = response.json()["rates"]
usd = float(rusd[0]["mid"])
response = requests.get("http://api.nbp.pl/api/exchangerates/rates/A/EUR/")
reur = response.json()["rates"]
eur = float(reur[0]["mid"])
response = requests.get("http://api.nbp.pl/api/exchangerates/rates/A/GBP/")
rgbp = response.json()["rates"]
gbp = float(rgbp[0]["mid"])

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