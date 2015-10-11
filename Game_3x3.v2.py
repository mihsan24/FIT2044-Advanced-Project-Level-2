"""
PYTHON TERNARY LIBRARY
@param: x and y are the proportion of players playing strategies 1 and 2, respectively. Hence 1 - (x + y) is the proportion of players playing strategy 3.
"""

from mpl_toolkits.mplot3d import *
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def pi0(x, y, matrix):
    return x * (matrix[0][0] - matrix[0][2]) + y * (matrix[0][1] - matrix[0][2]) + matrix[0][2]

def pi1(x, y, matrix):
    return x * (matrix[1][0] - matrix[1][2]) + y * (matrix[1][1] - matrix[1][2]) + matrix[1][2]

def pi2(x, y, matrix):
    return x * (matrix[2][0] - matrix[2][2]) + y * (matrix[2][1] - matrix[2][2]) + matrix[2][2]

def avg_pi(x, y, matrix):
    return x * pi0(x, y, matrix) + y * pi1(x, y, matrix) + (1 - (x + y)) * pi2(x, y, matrix)

def deltax_deltat(x, y, matrix):
    return x * (pi0(x, y, matrix) - avg_pi(x, y, matrix))

def deltay_deltat(x, y, matrix):
    return y * (pi1(x, y, matrix) - avg_pi(x, y, matrix))

def deltaz_deltat(x, y, matrix):
    return (1 - (x + y)) * (pi2(x, y, matrix) - avg_pi(x, y, matrix))

def find_rest_points(input_matrix):
    s = sp.symbols('s')
    t = sp.symbols('t')
    x = deltax_deltat(s, t, input_matrix)
    y = deltay_deltat(s, t, input_matrix)

    roots_list = sp.solve([x, y], s, t)
    equilibrium_points = []
    for i in roots_list:
        tmp = []
        valid_coordinate = True
        for j in i:
            if j < 0:
                valid_coordinate = False
                break
            else:
                tmp.append(float(j))
        if valid_coordinate:
            tmp.append(float(1 - (tmp[0] + tmp[1])))
            equilibrium_points.append(tmp)

    return equilibrium_points

def equilibrium_stability_check(equilibrium_points, input_matrix):
    s = sp.symbols('s')
    t = sp.symbols('t')
    x = deltax_deltat(s, t, input_matrix)
    y = deltay_deltat(s, t, input_matrix)

    dx_ds = sp.Lambda([s, t], sp.diff(x, s))
    dy_ds = sp.Lambda([s, t], sp.diff(y, s))
    dx_dt = sp.Lambda([s, t], sp.diff(x, t))
    dy_dt = sp.Lambda([s, t], sp.diff(y, t))

    stable_list = []
    for i in equilibrium_points:
        s = i[0]
        t = i[1]
        Jacobian_matrix = np.matrix([[dx_ds(s, t), dx_dt(s, t)], [dy_ds(s, t), dy_dt(s, t)]])
        Jacobian_eig = np.linalg.eig(Jacobian_matrix)
        stable = True
        for j in np.real(Jacobian_eig):
            if j > 0:
                stable = False
                break
        stable_list.append(stable)

    return stable_list

if __name__ == "__main__":
    input_matrix = [[0, 6, -4], [-3, 0, 5], [-1, 3, 0]]
    Num = 100

    equilibrium_points = find_rest_points(input_matrix)
    stable_list = equilibrium_stability_check(equilibrium_points, input_matrix)

    s = np.linspace(0, 1, num=Num)
    t = np.linspace(0, 1, num=Num)
    u = []
    for i in range(Num):
        u.append(1 - (s[i] + t[i]))

