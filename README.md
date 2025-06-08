# ProgramKomnum
final project komnum

|    NRP     |      Name      |
| :--------: | :------------: |
| 5025241260 | Farras Nazhif Pratikno |
| 5025241244 | Sinurat, Federico |
| 5025241245 | Girvan Notario Sarira |
| 5025241252 | Xavier Carlo Situmorang |

# Penjelasan Kode
```
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
```

1. Fungsi Et, dikalikan 100 untuk menjadikan persen.
```
def error_true(y_real, x_n):
    return abs((y_real - x_n) / y_real) * 100
```

2. Fungsi Ea, Jika x_n = 0, return infinity (float('inf')) agar tidak terjadi pembagian nol.
```
def error_approx(x_n, x_prev):
    return abs((x_n - x_prev) / x_n) * 100 if x_n != 0 else float('inf')
```

3. Fungsi Secant
   - mendefinisikan simbol x, karena akan dipakai di fungsi secantnya kode berikut,
     ```
         x = symbols('x')
     ```

   - menggantikan x di fungsi f dengan x0 atau x1,
     ```
         for i in range(max_iter):
        f_x0 = f.subs(x, x0)
        f_x1 = f.subs(x, x1)

     ```

   - rumus metode secant.
     ```
      x_n = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
     ```

   - membulatkan hasil menjadi desimal 2 angka di belakang koma, dan print setiap iterasi
     ```
       et_value = round(error_true(y_real, x_n), 2)
        ea_value = round(error_approx(x_n, x1), 2)
        x_n = round(x_n, 2)

        print(f"Iterasi {i+1}: x_n = {x_n}, Et = {et_value} %, Ea = {ea_value} %")

        x0, x1 = x1, x_n
     ```

4. Fungsi main (untuk input dari user)
    - input berupa fungsi f(x), x0, x1, dan y_real, sebagai contoh(nomor 12),
      ```
      Enter the function f(x) in terms of x: x**3+6*x**2+19*x-84                                            
      Enter the initial guess x0: -1
      Enter the second guess x1: 8
      Enter the real value y_real: 4
      ```

   - maka output akan menghasilkan
     ```
     Iterasi 1: x_n = -0.17, Et = 104.24 %, Ea = 4820.00000000000 %
     Iterasi 2: x_n = 0.51, Et = 87.32 %, Ea = 133.50 %
     Iterasi 3: x_n = 3.9, Et = 1.37 %, Ea = 87 %
     ```


