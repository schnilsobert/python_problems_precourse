def main():
    n = input("Gib eine Zahl ein:")
    zahl = int(n)
    if zahl % 3 == 0:
        print("Fizz")
    elif zahl % 5 == 0:
        print("Buzz")
    elif zahl % 3 == 0 and zahl % 5 == 0:
        print("FizzBuzz")
    else:
        print(zahl)

if __name__ == "__main__":
    main()