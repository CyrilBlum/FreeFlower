print("Kanada-perfekte Zahlen kleiner als 600:")
zahl = 2
for _ in range(600-2):
    teilersumme = 0
    teiler = 2
    for _ in range(zahl - 2):
        if zahl % teiler == 0:
            teilersumme += teiler
        teiler += 1

    # Ziffern von hinten mit % 10 abtrennen
    ziffernquadratsumme = 0
    rest = zahl
    while rest > 0:
        ziffer = rest % 10
        ziffernquadratsumme += ziffer**2
        rest //= 10

    if teilersumme == ziffernquadratsumme:
        print(
            f"{zahl}: Summe nichttrivialer Teiler = {teilersumme}, "
            f"Quersumme quadrierter Ziffern = {ziffernquadratsumme}"
        )

    zahl += 1
