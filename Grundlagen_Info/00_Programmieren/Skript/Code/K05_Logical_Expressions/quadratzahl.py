def ist_quadrat(x):
    # Überprüfung mit einer while-True-Schleife
    a = 1
    while True:
        if a * a == x:
            print(f"{x} ist eine Quadratzahl. a = {a}")
            break
        elif a * a > x:
            print(f"{x} ist kein Quadrat.")
            break
        a += 1


# Eingabe der natürlichen Zahl x
x = int(input("Geben Sie eine natürliche Zahl ein: "))
ist_quadrat(x)
