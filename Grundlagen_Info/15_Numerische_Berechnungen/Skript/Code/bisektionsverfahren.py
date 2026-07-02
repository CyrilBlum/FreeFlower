def f(x):
    """Die Funktion, deren Nullstelle wir suchen."""
    return x**2 - 2


def bisektion(f, a, b, tol=1e-5, max_iter=100):
    """
    Findet eine Nullstelle der Funktion f im Intervall [a, b].
    
    tol: Die Toleranz (wie nah wollen wir an der Nullstelle sein?)
    max_iter: Maximale Anzahl Schritte, um Endlosschleifen zu verhindern.
    """
    # Überprüfen, ob überhaupt ein Vorzeichenwechsel vorliegt
    if f(a) * f(b) >= 0:
        print("Fehler: Kein Vorzeichenwechsel im Startintervall [a, b].")
        return None
    
    print(f"{'Iteration':<10}{'a':<10}{'b':<10}{'m (Schätzung)':<15}{'f(m)':<12}")
    print("-" * 60)
    
    for i in range(1, max_iter + 1):
        # Berechne die Mitte
        m = (a + b) / 2
        y_m = f(m)
        
        # Ausgabe des aktuellen Schritts
        print(f"{i:<10}{a:<10.5f}{b:<10.5f}{m:<15.5f}{y_m:<12.5f}")
        
        # Abbruchbedingung: Wenn das Intervall klein genug ist oder wir die Nullstelle exakt treffen
        if (b - a) / 2 < tol or y_m == 0:
            return m
        
        # Intervall anpassen basierend auf dem Vorzeichen
        if f(a) * y_m < 0:
            b = m  # Nullstelle liegt links
        else:
            a = m  # Nullstelle liegt rechts
            
    print("Maximale Iterationen erreicht.")
    return (a + b) / 2

# Definition des Startintervalls [1, 2], da 1^2 - 2 = -1 und 2^2 - 2 = +2
start_a = 1.0
start_b = 2.0

nullstelle = bisektion(f, start_a, start_b, tol=0.001)
print("-" * 60)
print(f"Gefundene Nullstelle: {nullstelle:.5f}")