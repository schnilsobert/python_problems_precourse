pokemon : dict = {"name": "Gengar", "typ": "Geist"}

def welchen_typ_hat_mein_pokemon(pokemon : dict, multiple : bool = False):
    if multiple:
        return(pokemon["name"],", ".join(pokemon["typ"]))
    else: 
        return((pokemon["name"], pokemon["typ"]) if "typ" in pokemon else None)    
        
def main():
#1.Schreiben Sie eine Funktion welchen_typ_hat_mein_pokemon. Die Funktion soll "Feuer" zurück geben (return).
    pokemon : dict = {"name": "Gengar", "typ": ["Geist", "Gift"]}
     
    print(welchen_typ_hat_mein_pokemon(pokemon, multiple = True))
#2.Fügen Sie den Parameter pokemon: dict hinzu. Geben Sie den typ zurück, der im Dict unter dem key typ steht.
# Beispiel pokemon: gengar = {"name": "Gengar", "typ": "Geist"}
#3.Überprüfen Sie in Ihrer Funktion of typ ein key von pokemon ist. Falls das nicht der Fall ist, dann geben Sie None zurück.
    # if "typ" in pokemon:
    #     print(f"Jup{pokemon["typ"]}")
    # else: 
    #     print("None")
#4.Manche Pokemon haben mehr als einen Typ: gengar = {"name": "Gengar", "typ": ["Geist", "Gift"]}.
# Fügen Sie den optionalen Parameter multiple hinzu und bearbeiten Sie Ihr Program, sodass es bei einer Liste von Typen (multiple = True) die Rückgabe wie folgt aussieht: Geist, Gift (Beispiel)

#5.Oh nein, ich hab während der Funktion doch ganz vergessen um welches Pokemon es geht.
#Geben Sie zwei Rückgabewerte an. Der erste ist der Name vom Pokemon, der zweite der/die Typ(en).

#6.Schreiben Sie einen Docstring für die Funktion, damit Sie Ihren Code auch noch in 2 Monaten verstehen.

if __name__ == "__main__":
    main()