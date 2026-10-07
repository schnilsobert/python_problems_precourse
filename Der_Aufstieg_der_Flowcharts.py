def main():
    n = input("Input:")
    try:
        n = int(n)
        if n < 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid integer.")
        return
    fakultaet = 1
    while n > 1:
        fakultaet = fakultaet * n
        n = n - 1
    else: 
        print(fakultaet)
        
if __name__ == "__main__":
    main()