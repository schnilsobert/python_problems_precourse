def main():
    n = input("gib einen string ein:")
    string = str(n)
    if len(string) > 10 and len(string) < 20:
        print("Stimmt")
    else:
        print("Stimmt nicht")

if __name__ == "__main__":
    main()
    
