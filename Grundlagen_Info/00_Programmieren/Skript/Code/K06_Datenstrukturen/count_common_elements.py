liste_a = [1, 2, 2, 3, 5]
liste_b = [2, 2, 4, 5]

# zähle gemeinsame Elemente
count = 0
index_a = 0
for _ in range(len(liste_a)):
    index_b = 0
    for _ in range(len(liste_b)):
        if liste_a[index_a] == liste_b[index_b]:
            count += 1
            break  # Verhindert, dass das gleiche Element in liste_b mehrfach gezählt wird
        index_b += 1
    index_a += 1
print(count)    