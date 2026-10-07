#1.
begrüßung = "Hi, schön, dass du da bist!"
print(begrüßung)
verabschiedung = "Bis später!"
print(verabschiedung)
#2.
Anfang = 0
Ende = 10

# das ist eine while schleife, die für immer läuft
for i in range(Anfang, Ende):
    print(i)
#3.

def addiere(Summand1,Summand2 ):
    # Funktion, die sdlhvbdöfyknv
    return Summand1 + Summand2

Summe = addiere(8, 9)
print("Das Ergebnis der Addition ist:")
print(Summe)
#4.

# Hinweis: input wartet auf eine Eingabe im Terminal
# Sie tippen einfach etwas im Terminal und bestätigen die Eingabe mit [Enter]
# Danach läuft das Programm weiter
Eingabe = input("gib eine zahl ein: ")

ergebnis_als_string = int(Eingabe)  # k.a. was hier passiert

Ergebnis = ergebnis_als_string * 4  # eh. rechnen?

print("Vier mal die Eingabe ist ")
print(Ergebnis)
#5.

# Hinweis: Mit der random Bibliothek können Zufallszahlen generiert werden 
import random

# Hinweis: random.randint(a, b) erzeugt eine Ganzzahl zwischen a und b
random_zahl = random.randint(1, 10)

if random_zahl % 2 == 0:
    gerade_zahl = True
else:
    gerade_zahl = False
    
if gerade_zahl:
    print("Die Zahl ist gerade:")
else:
    print("Die Zahl ist ungerade:")

print("Die Zahl:")
print(random_zahl)