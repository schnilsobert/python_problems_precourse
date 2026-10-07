def main():
    list : list = ["marcell d'avis", 'mar', 'marc', "marcell d'avis", "marcell d'avis", 'mar', "marcell d'avis", "marcell d'avis", 'avis', "marcell d'avis", "marcell d'avis", 'avis', "marcell d'avis", 'avis', 'marc', 'avis', 'marc', 'marc', 'avis', 'marc', 'avis', "marcell d'avis", "marcell d'avis", "marcell d'avis", "marcell d'avis", 'avis', 'avis', "marcell d'avis", 'mar', "marcell d'avis", "marcell d'avis", 'avis', 'mar', 'mar', 'marc', 'mar', 'mar', 'avis', 'avis', "marcell d'avis", "marcell d'avis", 'mar', "marcell d'avis", 'marc', 'marc', "marcell d'avis", 'mar', "marcell d'avis", 'mar', 'mar', 'marc', "marcell d'avis", 'mar', 'mar', 'mar', "marcell d'avis", 'marc', 'marc', "marcell d'avis", "marcell d'avis", "marcell d'avis", "marcell d'avis", 'avis', 'mar', "marcell d'avis", "marcell d'avis", 'mar', 'avis', 'avis', 'mar', 'marc', "marcell d'avis", 'avis', "marcell d'avis", 'marc', 'marc', 'avis', 'mar', 'mar', 'marc', 'avis', 'mar', "marcell d'avis", "marcell d'avis", 'mar', "marcell d'avis", "marcell d'avis", 'marc', "marcell d'avis", 'avis', 'mar', "marcell d'avis", "marcell d'avis", 'mar', 'marc', 'avis', 'avis', "marcell d'avis", "marcell d'avis", 'avis', "marcell d'avis", 'avis', 'marc', 'marc', 'mar', 'marc', "marcell d'avis", 'mar', 'mar', "marcell d'avis", 'mar', "marcell d'avis", "marcell d'avis", 'marc', "marcell d'avis", 'marc', 'marc', 'marc', "marcell d'avis", "marcell d'avis", 'marc', 'marc', "marcell d'avis", "marcell d'avis", "marcell d'avis", "marcell d'avis", 'marc', "marcell d'avis", 'marc', 'mar', 'marc', 'marc', 'avis', 'marc', "marcell d'avis", 'mar', 'marc', 'mar', 'mar', 'marc', 'avis', 'marc', "marcell d'avis", 'mar', "marcell d'avis", "marcell d'avis", 'avis', 'mar', "marcell d'avis", 'avis', 'mar', 'marc', 'mar', "marcell d'avis", 'mar', 'mar', 'marc', 'mar', "marcell d'avis", 'mar', 'marc', 'marc', "marcell d'avis", 'marc', "marcell d'avis", 'avis', 'marc', 'avis', "marcell d'avis", "marcell d'avis", "marcell d'avis", "marcell d'avis", 'avis', 'marc', 'avis', 'marc', 'mar', "marcell d'avis", "marcell d'avis", "marcell d'avis", "marcell d'avis"]
#1.Finden Sie heraus wie oft marcell d'avis in der Liste steckt.

    print(list.count("marcell d'avis")) 
#2.Finden Sie heraus wie oft marc in der Liste steckt.

    print(list.count("marc"))

#3.Finden Sie heraus welche einzigartigen Einträge in der Liste sind.
    print(set(list))
#4.Finden Sie heraus wie oft marc in der Liste steckt, diesmal kann marc auch in anderen Strings stecken.
    marc_count = list.count("marc") + list.count("marcell d'avis")
    print(marc_count)

# Bonus
# Lösen Sie die Aufgaben ohne for-Schleifen
# Tipp: Schauen Sie sich Counter und set an
if __name__ == "__main__":
    main()