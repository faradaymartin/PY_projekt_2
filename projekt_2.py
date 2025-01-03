"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martin Faraday
email: faradaymartin@gmail.com
discord: martinfaraday_19641
"""
import random
import time

def generuj_tajne_cislo():
    cisla = list("123456789")  
    prvni_cislo = random.choice(cisla)
    cisla.remove(prvni_cislo)
    novy_seznam = list("0123456789")
    for cislo in prvni_cislo:
        novy_seznam.remove(cislo)
    tajne_cislo = prvni_cislo + ''.join(random.sample(novy_seznam, 3))
    return tajne_cislo

def validuj_vstup(vstup):
    if len(vstup) != 4:
        return "Číslo musí mít přesně 4 číslice."
    if not vstup.isdigit():
        return "Číslo musí obsahovat pouze číslice."
    if vstup[0] == '0':
        return "Číslo nesmí začínat nulou."
    if len(set(vstup)) != 4:
        return "Číslo nesmí obsahovat duplicity."
    return None

def vyhodnot_tip(tajne_cislo, tip):
    bulls = 0
    cows = 0
    for i in range(4):
        if tip[i] == tajne_cislo[i]:
            bulls += 1
        elif tip[i] in tajne_cislo:
            cows += 1
    return bulls, cows

def format_vysledek(bulls, cows):
    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_text}, {cows} {cow_text}"

uvod_text = "I've generated a random 4 digit number for you.\nLet's play a bulls and cows game."
delka_linky = len(uvod_text.splitlines()[0])

print("Hi there!")
print("-" * delka_linky)
print(uvod_text)
print("-" * delka_linky)

tajne_cislo = generuj_tajne_cislo()
print("Enter a number:")
print("-" * delka_linky)

start_cas = time.time()

while True:
    hrac_vstup = input("Your guess: ")
    chyba = validuj_vstup(hrac_vstup)
    if chyba:
        print(chyba)
    else:
        bulls, cows = vyhodnot_tip(tajne_cislo, hrac_vstup)
        vysledek = format_vysledek(bulls, cows)
        print(vysledek)
        if bulls == 4:
            konec_cas = time.time()
            celkovy_cas = konec_cas - start_cas
            print(f"Correct, you've guessed the right number'\nin 4 guesses! You've guessed the secret number in {celkovy_cas:.2f} seconds.")
            break
