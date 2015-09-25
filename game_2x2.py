"""
@unit: FIT2044 Advanced Project Level 2.
@author: Muhammad Ihsan.
@supervisor: Dr. Julian Garcia.
@since: August 15th 2015.
@modified: September 19th 2015.
@param input: a 2x2 matrix that represents the payoff of each population playing one of two strategies.
@param output: a Cartesian graph that represents the change of populations playing the first strategy over time.
@precondition: The input must be a 2x2 matrix and each element must be a real number greater than or equal to 0.
The matrix entries can either be obtained by input-output mechanism, or directly assigned to variable input_matrix.
@post-condition: The input matrix entries does not change, as variables derived from this matrix are used to generate the output of the program.
"""

# The following are Python libraries that will be used for the program
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# This function returns the average payoff for strategy 1.
def pi0(x, matrix):
    return (matrix[0][0] - matrix[0][1]) * x + matrix[0][1]

# This function returns the average payoff for strategy 2.
def pi1(x, matrix):
    return (matrix[1][0] - matrix[1][1]) * x + matrix[1][1]

# This function returns the average payoff of the game.
def avg_pi(x, matrix):
    return (x * pi0(x, matrix)) + ((1 - x) * pi1(x, matrix))

# This function returns the difference between the average payoff of strategy 1 and the average payoff of the game.
def deltax_deltat(x, matrix):
    return x * (pi0(x, matrix) - avg_pi(x, matrix))

if __name__ == "__main__":

    # The following variables require user input.

    input_matrix = [[3, 1], [1, 4]] # This variable stores the matrix of the game. It is treated as a list of two lists.
    Num = 50 # This variable stores the number of elements of Cartesian sets x and y for plotting the coordinates.

    # The first process of the program is to find the roots of the cubic function derived from the matrix. These roots represent the equilibrium point of the game.

    t = sp.symbols('t') # t is the independent variable. At this instance, this is treated as a symbol.
    x = deltax_deltat(t, input_matrix) # x is a function of t that represents the rate of change of populations playing the first strategy.
    coeffs_list = sp.poly(x) # The variable coeffs_list stores the coefficients of the polynomial of variable x.
    coeffs_list = coeffs_list.all_coeffs() # This command is to ensure that all roots of x are included in variable coeffs_list.
    roots_list = np.roots(coeffs_list) # The variable roots_list stores the roots of polynomial of x.

    # The second step is to evaluate the stability of the equilibrium point by evaluating the first derivative of the function.

    dx_dt = sp.Lambda([t], sp.diff(x)) # This assigns dx_dt as a function of the first derivative of x with respect to t.
    stable_list = [] # This list stores the stability of the equilibrium in roots_list, in the order of the latter list.
    for i in roots_list:
        if dx_dt(i) > 0: # If the first derivative of x at i is positive
            stable_list.append(0) # The equilibrium point is unstable, hence append 0.
        elif dx_dt(i) < 0: # Else if the first derivative of x at i is negative
            stable_list.append(1) # The equilibrium is stable, hence append 1.

    # The final step is to plot the equilibrium points using pyplot library, along with the function x.

    t = np.linspace(0, 1, num=Num, endpoint=True) # This sets t as a set of values between 0 and 1.
    x = deltax_deltat(t, input_matrix) # This sets x as a set of values of function deltax_deltat(t, input_matrix) for 0 <= t, t <= 1.
    plt.grid(True) # Include the grid on the upcoming figure
    plt.axis() # Include the axes on the upcoming figure.
    plt.plot(t, x) # This plots the graph of x with respect to t.

    # This code evaluates the type of markers to highlight the equilibrium points.

    for i in range(len(roots_list)):
        if stable_list[i] == 0: # If roots_list[i] is an unstable equilibrium
            plt.plot(roots_list[i], [0], "o", markersize=12, color='white') # Mark the point with a white circle.
            if i < len(roots_list) - 1: # This condition checks whether there is a triangle to mark on the x-axis that shows the direction to a stable equilibrium.
                mid_point = (roots_list[i] + roots_list[i + 1]) / 2 # The triangle marker will be plotted on the middle of two roots.
                plt.plot(mid_point, [0], "<", markersize=12, color='black') # Plot the triangle at (mid_point, 0).
        else: # If roots_list[i] is a stable equilibrium.
            plt.plot(roots_list[i], [0], "o", markersize=12, color='black') # Mark the point with a black circle.
            if i < len(roots_list) - 1: # This condition checks whether there is a triangle to mark on the x-axis that shows the direction to a stable equilibrium.
                mid_point = (roots_list[i] + roots_list[i + 1]) / 2 # The triangle marker will be plotted on the middle of two roots.
                plt.plot(mid_point, [0], ">", markersize=12, color='black') # Plot the triangle at (mid_point, 0).

    # This code adds additional features of the output graph.

    plt.plot(np.linspace(0, 1, num=Num), np.zeros(Num)) # This plots the x-axis between 0 <= x and x <= 1.
    plt.xlim(xmin=min(t) - 0.1, xmax=max(t) + 0.1) # This rescales the x-axis appearance of the graph.
    plt.ylim(ymin=min(x) - 0.1, ymax=max(x) + 0.1) # This rescales the y-axis appearance of the graph.
    plt.xlabel("Proportion of population playing strategy 1") # Label of x-axis of the graph.
    plt.ylabel("Rate of change of populations playing strategy 1") # Label of y-axis.
    plt.title("Change of populations playing strategy 1") # Title of the graph.
    plt.show()