def main ():
    Liste = [1, 2, 3, 4, 5]

    if len(Liste) > 20:
        print("Riesig")
    elif len(Liste) > 10 and len(Liste) < 21:
        print("Groß")
    else:
        print("Klein")

if __name__ == "__main__":
    main()
    