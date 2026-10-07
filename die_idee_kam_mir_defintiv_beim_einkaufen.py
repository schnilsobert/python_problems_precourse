def input_validierung(para1, para2, para3):
    if para2 in para1:
        para3 += para1[para2] 
        return para3
    else:
        print("Das gehört hier nicht rein!!!")
        return para3
def bon_updaten(para1, para2, para4):
    if para2 in para1:
        para4[para2] += 1
    return para4

def bon_erstellen(para3, para4): #Tim fragen sind function variablen lokal definiert??
    print(f"""
    -----------PFAND-BON----------- 
    Recyclete Gegenstände:
    Glas:    {para4["glas"]} a 0.10 Euro
    Plastik: {para4["plastik"]} a 0.15 Euro
    Dose:    {para4["dose"]} a 0.25 Euro
    GESAMT: {para3}
    Vielen Dank für ihre Tat für die Umwelt!!!
    """
    )

def main():
    summe : int = 0
    angebot : dict[str, float] = {
        "glas": 0.10, 
        "plastik": 0.15, 
        "dose": 0.25
        }
    bon : dict[str, int] = {
        "glas": 0,
        "plastik": 0,
        "dose": 0
    }
    while True:
        automaten_input = input("Gib mir Pfand-Flaschen und ich gebe dir GELD!!! ").lower()
        if automaten_input == "exit":
            print(bon_erstellen(summe, bon))
            break
        else:
            summe : int = input_validierung(angebot, automaten_input, summe)
            bon = bon_updaten(angebot, automaten_input, bon)
            
            print(f"Aktuelle Summe: {summe} Euro!")
if __name__ == "__main__":
    main()

# Aufgabe

# Pfand Preise:

# Glas: 10 Cent
# Plastik: 15 Cent
# Dose: 25 Cent
# Implementieren Sie Schritt für Schritt einen Pfand-Automaten:
# 1. Schreiben Sie eine unendliche While-Schleife, die einen input entgegen nimmt und abbricht, sobald “exit” eingegeben wird.
# 2.Schreiben Sie eine Funktion in der Sie den input validieren:
# Wenn die Eingabe nicht Glas, Plastik oder Dose ist, dann geben Sie irgendwas Lustiges zurück.
# Achtung: Groß- und Kleinschreibung sollte egal sein. Die Eingabe darf Glas, glas, GLAS, GlAs etc. sein.
# Wenn die Eingabe valide ist, dann geben Sie Glas, Plastik oder Dose in einer einhaltlichen Schreibweise zurück.
#  Andernfalls geben Sie None zurück.
# 3.Schreiben Sie eine Funktion, die den aktuellen Pfandbetrag und den vereinheitlichen input kriegt.
# Addieren Sie den input Pfandbetrag zum Gesamtwert und geben Sie ihn zurück.
# Bonus: Falls Sie sich selbst nicht vertrauen, dann gehen Sie in dieser Funktion abermals sicher, dass input einhaltlich ist.
# 4.Schreiben Sie eine Funktion in der Sie den Pfand-Bon Betrag ausgeben, wenn Sie mit “exit” das Program beenden.
# 5.Disclaimer: Windows Nutzer müssen die VM benutzen.
# Fügen Sie ein, dass die Zeit in der Sie einen input tätigen können auf 5 Sekunden beschränkt ist.
# Dies kann unter anderem mit folgendem Code erreicht werden:
# import signal
# def zeit_abgelaufen(sig, frame):
#     raise TimeoutError
# signal.signal(signal.SIGALRM, zeit_abgelaufen)
# signal.alarm(#Zeit in Sekunden)
# try:
#     # Warte auf eine Eingabe
# except TimeoutError:
#     # Was tun wenn die Zeit abgelaufen ist?
# Sobald die Zeit abgelaufen ist, wird Ihr Pfand-Bon gedruckt und das Program beendet.
# Bonus
# Überlegen Sie sich eine lustige Pfand-Bon Ausgabe.
# Tipp: Groß- und Kleinschreibung