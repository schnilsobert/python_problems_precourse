##Korrigieren Sie den folgenden Code, sodass er das tut, was im Diagramm steht.

def main():
    n = input("Gib einen Integer ein. ")
    n = int(n)
    s = input("Gib einen String ein. ")
    if n == 2:
        print(f"Juhu")
    elif n < 2 and s == "Cyber":
        print(f"Yeah")
    elif n > 2 or s == "Felix":
        print(f"Jippi")
    elif s== (f"Marc"):
        print(f"Heureka")
    else: 
        print(f"Jay")

if __name__ == "__main__":
    main()