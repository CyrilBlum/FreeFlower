def f(x):
    return x**2 - 2

def df(x):
    return 2 * x

def newton(f, df, x0, steps):
    x_old = x0

    for _ in range(steps):
        x_new = x_old - f(x_old) / df(x_old)
        x_old = x_new
    
    return x_new


print(newton(f, df, 1.8, 8))