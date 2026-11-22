zahl = 0
for _ in range(100):
    if zahl % 7 == 0 and zahl % 3 != 0:
        print(zahl)
    zahl += 1
