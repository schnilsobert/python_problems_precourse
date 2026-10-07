def main():
    number = input("Zahl:")
    try:
        number = int(number)
        if number < 10 and number > 5:
            print("Die Zahl ist kleiner als 10 und größer als 5.")
        else:
            print("Die Zahl ist entweder größer als 10 oder kleiner als 5.")

    except ValueError:
        print("Bitte geben Sie eine ganze Zahl ein.")
        return
if __name__ == "__main__":
    main()