import datetime
import math
import SwarmPackagePy
from SwarmPackagePy import testFunctions
from SwarmPackagePy.animation import animation

# Easy to solve
# function = testFunctions.easom_function
#function = testFunctions.ackley_function
# Easy to get confused for pso, but not for gsa
# function = testFunctions.ackley_function
# alh = SwarmPackagePy.pso(50, function, -10, 10, 2, 20)

num_iterations = 100
num_agents = 25
num_runs = 25
list_error = []
list_exec_time = []
list_functions = [(testFunctions.ackley_function, (0.0, 0.0)),
                  (testFunctions.easom_function, (math.pi, math.pi)),
                  (testFunctions.sphere_function, (0.0 , 0.0)),
                  (testFunctions.bohachevsky_function, (0.0 , 0.0)),
                  (testFunctions.sum_squares_function, (0.0 , 0.0))]
for l in range(len(list_functions)):
    # gets the function
    function = list_functions[l][0]
    #print("Function: " + ", " + str(function))
    #print("Run, Mean Error, Execution Time")
    avg_error = 0
    avg_delta = 0
    for i in range(num_runs):
        start = datetime.datetime.now()
        alh = SwarmPackagePy.fa(num_agents, function, -10, 10, 2, num_iterations)
        end = datetime.datetime.now()
        delta = end - start
        last_list_pos = alh.get_agents()[-1]
        # gets the global optima of the function
        global_optima = list_functions[l][1]
        error = 0
        for j in range(num_agents):
            last_pos = last_list_pos[j]
            ind_error = ((last_pos[0] - global_optima[0]) ** 2 + (last_pos[1] - global_optima[1]) ** 2) ** 0.5
            error += ind_error
        error /= num_agents
        list_error.append(error)
        list_exec_time.append(delta.microseconds)
        #print("average error for run " + str(i + 1) + ": " + str(error))
        #print("exec time for run " + str(i + 1) + ": " + str(delta,microseconds))
        #print(str(i + 1) + ", " + str(error) + ", " + str(delta.microseconds))
        avg_error += error
        avg_delta += delta.microseconds
        # Show animation
        # animation(alh.get_agents(), function, -10, 10, sr=True)
    avg_error /= num_runs
    avg_delta /= num_runs
    #print("Averages of runs")
    print(str(function) + ", " + str(avg_error) + ", " + str(avg_delta))