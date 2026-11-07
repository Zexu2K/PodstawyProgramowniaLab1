
# Zad 6

droga = float(input("Podaj długość trasy w km: "))
spalanie = float(input("Podaj średnie spalanie w l/100 km: "))

cena_paliwa = 6.5

zuzycie = (droga / 100) * spalanie
koszt = zuzycie * cena_paliwa

print("Przewidywane zużycie paliwa:", round(zuzycie, 2), "l")
print("Szacowany koszt podróży:", round(koszt, 2), "zł")

