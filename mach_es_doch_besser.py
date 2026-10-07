class Stein:
    """Ich bin 1-Stein"""
    def __init__(self, groeße : int):
        self.groeße : int = groeße

    def __str__(self) -> str:
        """ Damit die Scheiben schoen aufeinander liegen können, also
              **
             ****
            ******
            soll man pro Größe 2 * drucken
        """

        return '**' * self.groeße

    def __int__(self) -> int:
        return self.groeße

class Spielbrett:
    def __init__(self, anzahl_der_steine : int):
        self.anzahl_der_steine : int = anzahl_der_steine
        # Das ist eine von vielen Designentscheidungen, die wir in unserer sehr guten Dokumentation ganz genau erklären
        self.tuerme = [ Turm(), Turm(), Turm() ] #neu

        for index in range(0, anzahl_der_steine):
            # Linke Liste ist self.türme[0]
            self.tuerme[0].add(Stein(anzahl_der_steine - index))


    def spielzug(self, von : int, nach : int) -> bool:
        if self.ist_spielzug_legal(von, nach):
                letztes_element_vom_von_turm = self.tuerme[von].remove()
                # Lege Element ab
                self.tuerme[nach].add(letztes_element_vom_von_turm)
                return True

        return False
    def ist_spielzug_legal(self, von: int, nach: int) -> bool:
        if 0 <= von <= 2 and 0 <= nach <= 2:
            if len(self.tuerme[von]) > 0:
                oberster_stein = self.tuerme[von].steine[-1]
                if self.tuerme[nach].ist_add_stein_korrekt(oberster_stein):
                    return True
        return False
    def ist_gewonnen(self) -> bool:
        if len(self.tuerme[2]) == self.anzahl_der_steine:
            print("Gewonnen! ")
            return True
        return False
        
    def __str__(self) -> str:
        """Todo: Schön machen"""
        ausgabe = ""

        for zeilenindex in range(1, self.anzahl_der_steine+1):
            # Ist an dieser Höhenposition ein Stein?
            for turm in self.tuerme:
                position_in_der_liste = self.anzahl_der_steine - zeilenindex
                if len(turm) > position_in_der_liste:
                    ausgabe = ausgabe + "."*(self.anzahl_der_steine - int(turm.steine[position_in_der_liste])) + f"{turm.steine[position_in_der_liste]}" + "."*(self.anzahl_der_steine - int(turm.steine[position_in_der_liste]))
                else:
                    ausgabe = ausgabe + "."*(2*self.anzahl_der_steine)
                ausgabe = ausgabe + "|"
            ausgabe = ausgabe + '\n'


        return ausgabe
class Turm:
    def __init__(self):
        self.steine = [] 
    def __len__(self) -> int:
        return len(self.steine)
    def __int__(self) -> int:
        return int(self.steine[-1])
    def remove(self):
        if not self.steine:
            return None
        else:
            return self.steine.pop()
    def ist_add_stein_korrekt(self, stein: Stein) -> bool:
        if not self.steine:
            return True
        elif int(stein) < int(self):
            return True
        else:
            return False
    def add(self, stein: Stein) -> bool:
        if self.ist_add_stein_korrekt(stein):
            self.steine.append(stein)
            return True
        else:
            return False
        
    


def hanoi():
    
    while not mygame.ist_gewonnen():
        try:
                eingabe = input("Gib einen Spielzug! (bspw. 0 2)").split()
                von = int(eingabe[0])
                nach = int(eingabe[1])
                return von, nach 
        except ValueError:
            eingabe = input("Gib einen gültigen Spielzug! (bspw. 0 2)").split()
    print(f"Test")
    mygame = Spielbrett(5)
    print(f"{mygame}")
    mygame.spielzug(0, 1)
    mygame.spielzug(0, 1)
    mygame.spielzug(0, 1)
    mygame.spielzug(0, 1)
    mygame.spielzug(0, 1)
    mygame.spielzug(0, 1)
    mygame.spielzug(0, 2)
    mygame.spielzug(1, 2)

    print(f"{mygame}")



def main():
    """Hier startet die Funktion ihre Arbeit"""
    hanoi()


if __name__ == '__main__':
    main()