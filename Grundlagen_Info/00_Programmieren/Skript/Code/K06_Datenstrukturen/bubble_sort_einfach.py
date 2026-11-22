def bubble_sort(liste):
    # Äussere Schleife: Wiederhole den Sortiervorgang (n-1)-mal
    for _ in range(len(liste) - 1):
        # Innerer Schleifenzähler (Index des aktuellen Elements)
        j = 0
        # Innere Schleife: Vergleiche jedes Mal alle n-1 Nachbarpaare
        for _ in range(len(liste) - 1):
            # Wenn das aktuelle Element grösser als das nächste ist, tausche sie
            if liste[j] > liste[j + 1]:
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
            j += 1

    # Gib die sortierte Liste aus
    print(liste)


# Beispielverwendung
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
