
# Zad 6A

import random

droga = random.randint(1, 1000)
spalanie = float(input("Podaj średnie spalanie w l/100 km: "))
cena_paliwa = float(input("Podaj aktualną cenę paliwa za litr: "))

zuzycie = (droga / 100) * spalanie
koszt = zuzycie * cena_paliwa

print("Wylosowana długość trasy:", droga, "km")
print("Przewidywane zużycie paliwa:", round(zuzycie, 2), "l")
print("Szacowany koszt podróży:", round(koszt, 2), "zł")
