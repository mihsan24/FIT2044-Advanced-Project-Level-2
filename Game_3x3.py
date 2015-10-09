"""

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
            tmp.append(1 - (tmp[0] + tmp[1]))
            equilibrium_points.append(tmp)
    return equilibrium_points

def is_stable(point, input_matrix):
    # TODO: Add here method based on notebook
    return True




if __name__ == "__main__":

    Num = 100

    input_matrix = [[0, 6, -4], [-3, 0, 5], [-1, 3, 0]]
    for point in find_rest_points(input_matrix):
        print("Rest point: {}".format(point))


    # dx_ds = sp.diff(x, s)
    # dy_ds = sp.diff(y, s)
    # dx_dt = sp.diff(x, t)
    # dy_dt = sp.diff(y, t)
    # d2x_ds2 = sp.Lambda([s, t], sp.diff(dx_ds, s))
    # d2x_dsdt = sp.Lambda([s, t], sp.diff(dx_dt, s))
    # d2x_dtds = sp.Lambda([s, t], sp.diff(dx_ds, t))
    # d2x_dt2 = sp.Lambda([s, t], sp.diff(dx_dt, t))
    #
    # for i in equilibrium_points:
    #     a = i[0]
    #     b = i[1]
    #     hessian_x = np.matrix([d2x_ds2(a, b), d2x_dsdt(a, b)], [d2x_dtds(a, b), d2x_dt2(a, b)])
    #     hessian_x_eig = np.linalg.eig(hessian_x)
    #     print(hessian_x_eig)
    #
    # stable_list = []
    # for i in equilibrium_points:
    #     if jacobian_det(i[0], i[1]) > 0:
    #         stable_list.append(0)
    #     elif jacobian_det(i[0], i[1]) < 0:
    #         stable_list.append(1)

    # Num = 100
    #
    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # plt.hold(True)
    #
    # s = np.linspace(0, 1, num=Num)
    # t = np.linspace(0, 1, num=Num)
    # u = []
    # for i in range(Num):
    #     u.append(1 - (s[i] + t[i]))
    # Axes3D.plot_surface(s, t, u)
    #
    # ax.set_xlabel('s')
    # ax.set_ylabel('t')
    # ax.set_zlabel('u')
    #
    # Axes3D.imshow()