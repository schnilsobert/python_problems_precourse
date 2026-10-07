def main():
    Liste_Cyber: list = ["C", "Y", "B", "E", "R"]
    cyber_string: str = "CyBeR"
    s : str = input("Gibt bitte ein Wort:")
#1. Schreiben Sie eine For-Schleife, welche nacheinander die Elemente der Liste ['C', 'Y', 'B', 'E', 'R'] ausgibt.
    print("---1---")
    for i in Liste_Cyber:
        print(i)
#2. Schreiben Sie eine For-Schleife, welche nacheinander die Buchstaben des Strings "CyBeR" ausgibt.
    print("---2---")
    for j in range(5):
        print(cyber_string[j])
#3.Schreiben Sie eine For-Schleife, welche nacheinander die Zahlen von 0 bis 9 ausgibt.
    print("---3---")
    for k in range(0, 9+1):
        print(k)
#4.Schreiben Sie eine For-Schleife, welche nacheinander die Zahlen von 0 bis -9 ausgibt.
    print("---4---")
    for l in range(0, 9+1):
            print(-l)
#5.Schreiben Sie eine For-Schleife, welche nacheinander die Zahlen von -1 bis -10 ausgibt.
    print("---5---")
    for m in range(1,10+1):
         print(-m)
#6.Schreiben Sie eine For-Schleife, welche für einen gegebenen String s die Zahlen von 0 bis Länge_von(s) ausgibt.
    print("---6---")
    for n in range(0, len(s)+1):
         print(n)
#7.Schreiben Sie eine For-Schleife, welche die Buchstaben des Strings "CyBeR" in umgekehrter Reihenfolge ausgibt
    print("---7---")
    reverse_cyber_string: str = cyber_string[::-1]
    print(reverse_cyber_string)




if __name__ == "__main__":
    main()