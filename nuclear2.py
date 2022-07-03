#Importing an external library (install by running this command in the command prompt/terminal: pip install matplotlib) for visualisation of data.
from matplotlib import pyplot as plt

# Importing math library which comes with python as i have to use square root
import math

# Running a list comprehension to generate values from 0 to 65 (excluding 65) with an interval gap of 5 and diving each result by 100 (thus the final result will be 0.05, 0.1, 0.15, ..., 0.6). This list represents the different values of kinetic energy of beta particle(electron).
k = [i/100 for i in range(0, 65, 5)] 

# same as above list except all the values are same (i.e, 0.511, representing rest mass energy of electron), repeated length of k list times.
rme = [0.511 for i in range(len(k))]

# 2 times the rest mass energy of electron repeated length of k times.
rme_2 = [1.02 for i in range(len(k))]

# Sum of kinetic energy and twice the rest mass energy (above list). 
k2me = [k[i] + rme_2[i] for i in range(len(k))]

# square root of kinetic energy multipied with the above sum. 
sk2me = [math.sqrt(k[i] * k2me[i]) for i in range(len(k))]

# Q-value of the electron
qb = [0.6 for i in range(len(k))]

# subtracting kinetic energy from Q-value
q_ke = [qb[i] - k[i] for i in range(len(k))]

# squaring the above result
q_ke2 = [q_ke[i]**2 for i in range(len(k))]

# Sum of kinetic energy and rest mass energy
k_mec = [k[i] + rme[i] for i in range(len(k))]

# Generating the varying terms of  N(k) for the graph by multiplying sk2me, q_ke2 and k_mec
res = [math.sqrt((sk2me[i]*q_ke2[i]*k_mec[i])/k[i]) for i in range(len(k))]


# plotting k (kinetic energy) vs res (N(k))
plt.plot(q_ke, res)

# setting the label of x-axis to 'Kinetic energy'
plt.xlabel('Kinetic energy')

# setting the label of y-axis to 'N(k)'
plt.ylabel("N(k)")

# setting the title of the graph to 'BETA SPECTRUM'
plt.title("BETA SPECTRUM")

# setting the x-scale to kinetic energy values
plt.xticks(k)

# setting the y-scale to 0.005, 0.01, ..., 0.08
plt.yticks([i/200 for i in range(16)])

# Draw grid lines in the graph
plt.grid()

# Calling the show method to show the result
plt.show()

