def f(x):
    return x**2 - 2

def df(x):
    """Die erste Ableitung von f(x) = x^2 - 2"""
    return 2 * x


def newton(f, df, x0, tol=1e-5, max_iter=100):
    """
    Findet eine Nullstelle von f mittels Newton-Verfahren.
    
    df: Die Ableitungsfunktion von f
    x0: Der Startwert
    """
    x = x0
    
    print(f"{'Iteration':<10}{'x_n':<15}{'f(x_n)':<15}{'f\'(x_n)':<15}")
    print("-" * 55)
    
    for i in range(1, max_iter + 1):
        y = f(x)
        slope = df(x)
        
        print(f"{i:<10}{x:<15.8f}{y:<15.8f}{slope:<15.8f}")
        
        # Kritischer Fall: Waagrechte Tangente (Division durch 0)
        if slope == 0:
            print("Fehler: Ableitung ist Null. Keine eindeutige Tangente.")
            return None
            
        # Der Newton-Schritt
        x_neu = x - y / slope
        
        # Abbruchbedingung: Wenn der Schritt winzig klein wird
        if abs(x_neu - x) < tol:
            return x_neu
            
        x = x_neu
        
    print("Maximale Iterationen erreicht.")
    return x

# Startwert x0 = 2.0
nullstelle_newton = newton(f, df, x0=2.0, tol=0.001)
print("-" * 55)
print(f"Gefundene Nullstelle: {nullstelle_newton:.8f}")