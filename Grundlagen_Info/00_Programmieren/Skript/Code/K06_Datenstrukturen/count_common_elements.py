a = [1, 2, 2, 3, 5]
b = [2, 2, 4, 5]

# zähle gemeinsame elemente
count = 0
for element1 in liste1:
    for element2 in liste2:
        if element1 == element2:
            count += 1
            break  # Verhindert, dass das gleiche Element in liste2 mehrfach gezählt wird
print(count)