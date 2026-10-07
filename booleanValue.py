def main():
    print(bool([]))  # eine leere Liste
    print(bool([1,2,3]))  # eine Liste mit 3 Elementen
    print(bool([1, "Hallo", 3.14]))  # eine Liste mit unterschiedlichen Elementen
    print(bool([0]))  # eine Liste mit einem Element
    print(bool(""))  # ein leerer String
    print(bool("python"))  # der String "python"   

#2.
#Wandeln Sie folgende Werte in booleans um:
#1
    print(bool(1))
#0
    print(bool(0))
#1.0
    print(bool(1.0))
#0.0
    print(bool(0.0))
#0.5
    print(bool(0.5))


#3.
 #Wandeln Sie den Integer 42 in einen Float um.
    print(type(float(42)))
 #Wandeln Sie den Float 42.42 in einen Integer um. Was passiert?
    print(type(int(42.42)))
 #Erst öffnen, wenn die Frage beantwortet wurde!
 #runden => round(42.42) = 42
 #       => round(42.72) = 43
    print(type(round(42.72)))
#4.
 #Wandeln Sie einen Integer in einen String um
    print(type(str(42)))
 #Wandeln Sie "python" in eine Liste um
    print(type(list("python")))
 #Wandeln Sie einen Boolean in einen String um
    print(type(str(True)))
#5.
 #Wandeln Sie einen Boolean in einen Integer und einen Float um.
    print(type(int(True)))
    print(type(float(True)))
#6. all valueErrors and typeErrors
# Wandeln Sie "python" in einen Integer um
    print(type(int("python")))  # This will raise a ValueError because "python" cannot be converted to an integer   
# Wandeln Sie 69 in eine Liste um
    print(type(list(69))) # This will raise a TypeError because an integer cannot be directly converted to a list
# Wandeln Sie True in eine Liste um
    print(type(list(True))) # This will raise a TypeError because a boolean cannot be directly converted to a list
if __name__ == "__main__":
    main()
