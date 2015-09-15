"""
@author: Muhammad Ihsan
"""

import sympy as sp
import numpy as np
import turtle

def pi0(x, matrix):
    return (matrix[0][0] - matrix[0][1]) * x + matrix[0][1]

def pi1(x, matrix):
    return (matrix[1][0] - matrix[1][1]) * x + matrix[1][1]

def avg_pi(x, matrix):
    return (x * pi0(x, matrix)) + ((1 - x) * pi1(x, matrix))

def deltax_deltat(x, matrix):
    return x * (pi0(x, matrix) - avg_pi(x, matrix))

if __name__ == "__main__":
    Num = 50
    input_matrix = [[3, 1], [1, 4]]
    t = sp.symbols('t')
    x = deltax_deltat(t, input_matrix)
    coeffs_list = sp.poly(x)
    coeffs_list = coeffs_list.all_coeffs()
    roots_list = np.roots(coeffs_list)

    dx_dt = sp.Lambda([t], sp.diff(x))
    stable_list = []
    for i in coeffs_list:
        if i >= 0:
            stable_list.append(0)
        else:
            stable_list.append(1)

    turtle.home()
    if stable_list[0] == 0:
        turtle.dot(20, "black")
        turtle.dot(10, "white")
        turtle.shape("arrow")
        turtle.backward(roots_list[1] * 100)
        turtle.stamp()
        turtle.setpos(-100, 0)
        turtle.shape("arrow")
        turtle.forward((1 - roots_list[1] * 100))
        turtle.stamp()
    else:
        turtle.dot(20, "black")
        turtle.backward(roots_list[1] * 100)
        turtle.dot(20, "black")
        turtle.dot(10, "white")
        turtle.shape("arrow")
        turtle.forward(roots_list[1] * 100)
        turtle.stamp()
        turtle.backward(100)
        turtle.dot(20, "black")
        turtle.setpos(roots_list[1] * 100, 0)
        turtle.shape("arrow")
        turtle.backward((1 - roots_list[1]) * 100)
        turtle.stamp()

    turtle.getscreen()._root.mainloop()



    """
    t = np.linspace(0, 1, num=Num, endpoint=True)
    dx_dt = deltax_deltat(t, input_matrix)
    d2x_dt2 = np.gradient(dx_dt)
    plt.grid(True)
    plt.axis()
    plt.plot(t, dx_dt)
    plt.plot(t, d2x_dt2)
    plt.xlabel("Proportion of population playing strategy 1")
    plt.ylabel("Change of populations playing strategy 1")
    plt.title("Change of populations playing strategy 1")
    plt.show()
    """