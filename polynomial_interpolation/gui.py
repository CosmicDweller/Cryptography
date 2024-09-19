import tkinter as tk
import math
import numpy as np
import galois


root = tk.Tk()
root.geometry('700x500')

root.title("Polynomial Interpolation")
k_label = tk.Label(root, text="k:")
k_label.grid(sticky=tk.W, pady=2, padx=10)

k_text = tk.Entry(root)
k_text.grid(column=1, row=0, pady=2, sticky=tk.W)
k_text.focus()

k = 0

instruction_text = tk.Label(root, text="Enter in points in form: x, y")
instruction_text.grid(column=1, row=1)

points = [tk.Entry(root, width=8) for _ in range(40)]

def load_points():
    calculate_btn.grid(column=1, row=4, sticky=tk.W)
    sol_label.grid(column=2, row=100, sticky=tk.W)
    for entry in points:
        entry.grid_remove()

    row = 3
    global k
    k = int(k_text.get())
    for i in range(k):
        points[i].grid(column=((i%4) + 3), row=row)
        if (i + 1) % 4 == 0:
            row += 1

p = 35951863
GF = galois.GF(p)

def poly_interpolate():
    coord = []
    sol = ""
    for i in range(k):
        text = points[i].get().replace(' ', '')
        text = text.split(',')
        x = float(text[0])
        y = float(text[1])
        coord.append((x, y))

    a = []

    for i in range(k):
        # b.append(points[i][1])
        eqn = []
        for j in range(k):
            eqn.append(pow(coord[i][0], j))
            # peval([], j)
        eqn.append(coord[i][1])
        a.append(eqn)
    augmented_matrix = GF(np.array(a))
    # sols = GF(np.array(b))
    rref_matrix = augmented_matrix.row_reduce()
    coefficients = []
    for i in range(len(rref_matrix)):
        coefficients.append(rref_matrix[i][-1])

    sol += 'y ='
    for i in range(k):
        if i == 0:
            num = coefficients[k - i - 1]
            sol += ' ' + str(round(float(num), 3)) + f"x^{k - i - 1}"
        else:
            if coefficients[k - i - 1] < 0:
                num = abs(coefficients[k - i - 1])
                sol += " - " + str(round(float(num), 3)) + f"x^{k - i - 1}"
            else:
                num = abs(coefficients[k - i - 1])
                sol += " + " + str(round(float(num), 3)) + f"x^{k - i - 1}"

    sol_label.config(text=sol)


k_btn = tk.Button(root, text="Go", command=load_points)
k_btn.grid(column=2, row=0, sticky=tk.W)

calculate_btn = tk.Button(root, text="Calculate", command=poly_interpolate)

sol_label = tk.Label(root, text="")

root.mainloop()