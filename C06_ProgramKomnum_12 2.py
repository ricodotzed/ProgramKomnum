from sympy import symbols, sympify

def error_true(y_real, x_n):
    return abs((y_real - x_n) / y_real) * 100

def error_approx(x_n, x_prev):
    return abs((x_n - x_prev) / x_n) * 100 if x_n != 0 else float('inf')

def secant(f, x0, x1, y_real, max_iter=3):
    x = symbols('x')

    for i in range(max_iter):
        f_x0 = f.subs(x, x0)
        f_x1 = f.subs(x, x1)

        if f_x1 - f_x0 == 0:
            raise ValueError("Divide by zero causes error")

        x_n = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        et_value = round(error_true(y_real, x_n), 2)
        ea_value = round(error_approx(x_n, x1), 2)
        x_n = round(x_n, 2)

        print(f"Iterasi {i+1}: x_n = {x_n}, Et = {et_value} %, Ea = {ea_value} %")

        x0, x1 = x1, x_n

if __name__ == "__main__":
    f = input("Enter the function f(x) in terms of x: ")
    f = sympify(f)

    x0 = float(input("Enter the initial guess x0: "))
    x1 = float(input("Enter the second guess x1: "))
    y_real = float(input("Enter the real value y_real: "))

    secant(f, x0, x1, y_real)
