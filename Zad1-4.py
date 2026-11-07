from tkinter.constants import ROUND

# Zad 1A
print("=== ZADANIE 1 A) ===")
x = 1 + 2
print("1 + 2", "Daje:", type(x), "Typ int (ang. integer) reprezentuje liczby całkowite dodatnie lub ujemne bez kropki dziesiętnej.")

x = 1 + 4.5
print("1 + 4.5", "Daje:", type(x), "Typ float (zmiennoprzecinkowy) reprezentuje liczby rzeczywiste. Składają się one z części całkowitej i ułamkowej.")

x = 3 / 2
print("3 / 2", "Daje:", type(x), "Typ float (zmiennoprzecinkowy) reprezentuje liczby rzeczywiste. Separatorem części całkowitej i ułamkowej jest kropka.")

x = 4 / 2
print("4 / 2", "Daje:", type(x), "Typ float (zmiennoprzecinkowy) reprezentuje liczby rzeczywiste. Nawet jeśli wynik dzielenia jest całkowity, operator / zwraca typ float.")

x = 3 // 2
print("3 // 2", "Daje:", type(x), "Typ int (ang. integer) reprezentuje liczby całkowite dodatnie lub ujemne bez kropki dziesiętnej.")

x = -3 // 2
print("-3 // 2", "Daje:", type(x), "Typ int (ang. integer) reprezentuje liczby całkowite. Wynik dzielenia całkowitego jest zaokrąglany w dół, czyli tutaj do -2.")

x = 11 % 2
print("11 % 2", "Daje:", type(x), "Typ int (ang. integer) reprezentuje liczby całkowite dodatnie lub ujemne bez kropki dziesiętnej.")

x = 2 ** 10
print("2 ** 10", "Daje:", type(x), "Typ int (ang. integer) reprezentuje liczby całkowite dodatnie lub ujemne bez kropki dziesiętnej.")

x = 8 ** (1/3)
print("8 ** (1/3)", "Daje:", type(x), "Typ float (zmiennoprzecinkowy) reprezentuje liczby rzeczywiste. Wynik potęgowania z wykładnikiem ułamkowym jest typu float.")
# Operatory arytmetyczne
print("\nOperatory arytmetyczne:")

print("+  - Dodawanie, np. 1 + 2 = 3")
print("-  - Odejmowanie, np. 6 - 2 = 4")
print("*  - Mnożenie, np. 3 * 4 = 12")
print("/  - Dzielenie zmiennoprzecinkowe, np. 3 / 2 = 1.5")
print("// - Dzielenie całkowite, np. 3 // 2 = 1")
print("%  - Dzielenie modulo, czyli reszta z dzielenia, np. 11 % 2 = 1")
print("** - Potęgowanie, np. 2 ** 10 = 1024")


# Zad 1B
print("\n=== ZADANIE 1 B) ===")
x = int(3.0)
print("int(3.0)", "Daje:", x, type(x), "Funkcja int() zamienia liczbę zmiennoprzecinkową na liczbę całkowitą. Typ int reprezentuje liczby całkowite dodatnie lub ujemne bez kropki dziesiętnej.")

x = float(3)
print("float(3)", "Daje:", x, type(x), "Funkcja float() zamienia liczbę całkowitą na liczbę zmiennoprzecinkową. Typ float reprezentuje liczby rzeczywiste składające się z części całkowitej i ułamkowej.")

x = float("3")
print('float("3")', "Daje:", x, type(x), "Funkcja float() zamienia tekst zawierający liczbę na liczbę zmiennoprzecinkową. Separatorem części całkowitej i ułamkowej jest kropka.")

x = str(12.4)
print("str(12.4)", "Daje:", x, type(x), "Funkcja str() zamienia liczbę zmiennoprzecinkową na tekst. Typ tekstowy str reprezentuje sekwencje danych znakowych, nazywane również napisami lub łańcuchami znaków.")

x = bool(0)
print("bool(0)", "Daje:", x, type(x), "Funkcja bool() zamienia wartość na typ logiczny. Typ bool umożliwia uzyskanie odpowiedzi Prawda lub Fałsz. Liczba 0 oznacza False, czyli Fałsz.")


# Zad 2
print("\n=== ZADANIE 2) ===")
uczelnia = "Studiuję na WSIiZ"
print(uczelnia)


# Zad 3
print("\n=== ZADANIE 3) ===")
imie = "Jan"
wiek = 20
wzrost = 178

print("Nazywam się", imie, "i mam", wiek, "lat.")
print("Mój wzrost to", wzrost, "cm.")


# Zad 4
print("\n=== ZADANIE 4) ===")
Cena = 39.99
Rabat = 0.2
Cena_po_rabacie = Cena - (Cena * Rabat)

print("Cena produktu:", Cena, "PLN")
print("Rabat:", Rabat * 100, "%")
print("Cena po rabacie: ", round(Cena_po_rabacie,2), "PLN")


