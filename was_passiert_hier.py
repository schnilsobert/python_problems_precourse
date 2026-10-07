#1.
#multipliziert eine Zahl mit sich selbst, und gibt das produkt als neue_zahl zurück
def eine_funktion(zahl):
    neue_zahl = zahl*zahl
    return neue_zahl
#2. 
#addiert erst 1 und dann multiplizert mit 2, gibt das ergibnis als neue_zahl zurück

def eine_weitere_funktion(zahl):
    zahl += 1
    neue_zahl = zahl*2
    return neue_zahl
#3.
#erzeugt die summe der multiplikationen mit sich selber von 1-3.
def eine_weiterere_funktion(zahl):
    i = 3
    neue_zahl = 1
    while i > 0:
        neue_zahl = neue_zahl*zahl
        i = i-1
    return neue_zahl
#4.
#Die funktion macht aus einer natürlichen Zahl die Fakultät dieser Zahl
def noch_eine_funktion(natuerliche_zahl):
    neue_zahl = 1
    i = natuerliche_zahl
    while i > 0:
        neue_zahl = neue_zahl*i
        i = i-1
    return neue_zahl
#5.
#die Funktion geht sicher das 'zahl' immer positiv ist.
def noch_eine_weitere_funktion(zahl):
    if zahl < 0:
        neue_zahl = zahl*(-1)
    else:
        neue_zahl = zahl
    return neue_zahl