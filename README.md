# Priprema radnog okruženja

Student: Matija Raičević

Projekat sadrži funkciju za računanje prosječne cijene, testove i alate za provjeru Python koda.

## Funkcija

Funkcija `prosjecna_cijena` nalazi se u fajlu `cijene.py`.
Prima listu brojeva i vraća njihov aritmetički prosjek.
Ako je lista prazna, prijavljuje `ValueError`.

Primjer: za cijene [10, 20, 30] rezultat je 20.

## Priprema i pokretanje

Potreban je Python 3.12 ili noviji.

Kreiranje virtuelnog okruženja:

```powershell
py -m venv .venv
```

Aktiviranje okruženja u PowerShell terminalu:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalacija potrebnih paketa:

```powershell
python -m pip install -r requirements.txt
```

Pokretanje testova:

```powershell
python -m pytest
```

Provjera koda:

```powershell
python -m ruff check .
```

## Testovi i rezultati

Testirana su tri slučaja:
- Lista sa više cijena: [10, 20, 30].
- Lista sa jednom cijenom: [15].
- Prazna lista, za koju se očekuje ValueError.

Sva tri testa su prošla. Ruff provjera završena je bez prijavljenih problema.

## Upotreba AI asistenta

AI asistenta (chatgpt) koristio sam za smjernice pri pripremi okruženja, predlog funkcije `prosjecna_cijena` i odgovarajućih testova.

Sažetak zahtjeva upućenog asistentu: implementirati funkciju koja računa prosječnu vrijednost liste cijena, obrađuje slučaj prazne liste i priložiti pytest testove.

Predloženo rješenje sam pregledao i provjerio pokretanjem testova i Ruff provjere. Funkcija računa prosjek dijeljenjem zbira cijena njihovim brojem, dok provjera prazne liste sprečava dijeljenje nulom. Uočena ograničenja i mogućnosti dopune navedeni su u nastavku.

## Uočena ograničenja generisanog koda

Funkcija obrađuje praznu listu, ali ne provjerava posebno da li su svi
elementi brojevi. Unos teksta umjesto broja izazvao bi TypeError.

Negativne vrijednosti nijesu zabranjene. Ako se funkcija koristi za
cijene koje ne smiju biti negativne, potrebna je dodatna provjera.

Postojeći testovi ne pokrivaju decimalne cijene ni neispravne tipove
podataka. Prolazak ova tri testa ne potvrđuje ispravnost za sve moguće unose.
