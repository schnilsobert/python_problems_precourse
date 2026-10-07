
def main():
    """
    Die Lange Version:
    n = input("Gib eine Zahl ein:")
    länge : int = int(n)
    for index in range (1, länge + 1):
        print("*"*index)
    for index in range (1, länge):
            print("*"*(länge - index))
    """

    #Die Kurze Version:
    Liste = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    for i in Liste:
        print("*"*i)


if __name__ == "__main__":
    main()