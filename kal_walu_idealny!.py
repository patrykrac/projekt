import requests
import json

decyzja = input("Chcesz kupić czy sprzedać walutę?: ")
waluta = input("jaką walutę?: ").upper()

response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/")
if response.status_code == 200:
    rates = response.json()["rates"]
    kurs = float(rates[0]["mid"])
elif response.status_code == 404:
    response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/B/{waluta}/")
    rates = response.json()["rates"]
    kurs = float(rates[0]["mid"])

if decyzja == "kupić" or decyzja == "kupic":
    hajs = float(input("za ile chcesz kupić: "))
    print(f"kupisz za to {round(hajs/kurs, 2)} {waluta}")
elif decyzja == "sprzedać" or decyzja == "sprzedac":
    hajs = float(input("ile chcesz sprzedać: "))
    print(f"dostaniesz {round(hajs*kurs, 2)} polskich złociszy")