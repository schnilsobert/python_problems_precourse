def main():
#1.Schreiben Sie diese while-Schleife in eine for-Schleife um:
#.     index = 0
#      while index < 5:
#           print(index)
#           index = index+1
    print("---1---")
    for i in range(0,5):
        print(i)
#2.Schreiben Sie diese while-Schleife in eine for-Schleife um:
    print("---2---")
    liste = ["Hallo", "ich", "bin", "im", " Programm ", " gefangen "]
    # index = 0
    # while index < len(liste):
    #     print(liste[index])
    #     index = index + 1
    for j in range(0,len(liste)):
        print(liste[j])

#3.Schreiben Sie eine while-Schleife, die einen Wert so lange mit 2 multipliziert, bis der Wert 2048 ist. Starten Sie mit dem Wert 1.
    print("---3---")
    eins : int = 1
    while eins <= 2048:
        print(eins)
        eins = eins * 2
        
#4.Schreiben Sie eine while-Schleife, die immer wieder nach einem input() fragt. Bei dem Input “exit” soll die Schleife abbrechen.
    print("---4---")
    frage = ""
    while frage != "exit":
        frage = input("Was willst du? ")
#5.Schreiben Sie eine while-Schleife, die immer wieder nach einem input() fragt. Die Schleife soll abbrechen, wenn der Input kleiner als 10 ist.
    print("---5---")
    zahlen_abfrage : int = 11
    while zahlen_abfrage >= 10:
        zahlen_abfrage = int(input("Gib nh zahl: "))    
#6.Schreiben Sie eine while-Schleife, die eine Wert a in jedem Schleifendurchlauf mit 2 addiert und einen Wert b mit 6 multipliziert. Die Schleife soll abbrechen, wenn a größer als 10 und b größer als 40 ist.
    print("---6---")
    a : int = 0
    b : int = 1
    while a <= 10 or b <= 40:
        a = a + 2
        b = b * 6
        print(f"a: {a}|b: {b}")

if __name__ == "__main__":
    main()