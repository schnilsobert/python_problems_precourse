# Aufgabe

# In dieser Aufgaben sollen Sie erste Erfahrungen mit dem Erstellen von Klassen machen.

# Aufgabe 1.

# Erstellen Sie eine Klasse Mensch. Ein Mensch besteht dabei aus den Attributen Name, Geburtsdatum und Geschlecht.
#  Sie können alle drei Attribute mit Strings darstellen.
class Mensch:
    def __init__(self, name: str, geburtsdatum: str, geschlecht: str):
        self.name = name
        self.geburtsdatum = geburtsdatum
        self.geschlecht = geschlecht

    def __str__(self) -> str:
        print(f"""
            Name:         {self.name}
            Geburtsdatum: {self.geburtsdatum}
            Geschlecht:   {self.geschlecht}
        """)
        


# Aufgabe 2.

# Erstellen Sie eine Methode vorstellen, mit welcher sich die Objekte formal vorstellen können.
    def vorstellen(self):
        print(f"Hallo ich bin {self.name}, {self.geschlecht}, geboren am {self.geburtsdatum}.")
# Beispiel (kein funktionierender Code, nur zum verdeutlichen der Aufgabenstellung):

# python = Mensch("Python", "20.02.1991", "Snek")
# python.vorstellen()
#nils = Mensch("Nils", "24.07.2006", "männlich")
#nils.vorstellen()
# OUTPUT:
# Hallo ich heiße Python, wurde am 20.02.1991 geboren und bin Snek.
# Bonus

# Manchmal muss es schnell gehen und es bleibt keine Zeit für Formalitäten.
#  Implementieren Sie für diesen Zweck die Methode __str__(), damit sich Menschen wie Strings verhalten können (Typecasting). 
# Dabei sollen alle wesentlichen Informationen schnell ausgedruckt werden.

# Beispiel (kein funktionierender Code, nur zum verdeutlichen der Aufgabenstellung):

chell = Mensch("Chell", "Unbekannt", "Weiblich")
# print(chell)
print(chell)
# OUTPUT:
# Name: Chell
# Geburtsdatum: Unbekannt
# Geschlecht: Weiblich