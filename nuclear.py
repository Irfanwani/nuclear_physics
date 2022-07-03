#Importing an external library (install by running this command in the command prompt/terminal: pip install matplotlib) for visualisation of data.
from matplotlib import pyplot as plt

# Importing math library which comes with python as i have to use square root
import math

# Running a list comprehension to generate values from 0 to 65 (excluding 65) with an interval gap of 5 and diving each result by 100 (thus the final result will be 0.05, 0.1, 0.15, ..., 0.6). This list represents the different values of kinetic energy of beta particle(electron).
k = [i/100 for i in range(0, 65, 5)] 
print('k:', k)

# same as above list except all the values are same (i.e, 0.511, representing rest mass energy of electron), repeated length of k list times.
rme = [0.511 for i in range(len(k))]
print('rme:', rme)

# 2 times the rest mass energy of electron repeated length of k times.
rme_2 = [1.02 for i in range(len(k))]
print('rme_2:', rme_2)

# Sum of kinetic energy and twice the rest mass energy (above list). 
k2me = [k[i] + rme_2[i] for i in range(len(k))]
print('k2me:', k2me)

# square root of kinetic energy multipied with the above sum. 
sk2me = [math.sqrt(k[i] * k2me[i]) for i in range(len(k))]
print('sk2me:', sk2me)

# Q-value of the electron
qb = [0.6 for i in range(len(k))]
print('qb:', qb)

# subtracting kinetic energy from Q-value
q_ke = [qb[i] - k[i] for i in range(len(k))]
print('q_ke:', q_ke)

# squaring the above result
q_ke2 = [q_ke[i]**2 for i in range(len(k))]
print('q_ke2:', q_ke2)

# Sum of kinetic energy and rest mass energy
k_mec = [k[i] + rme[i] for i in range(len(k))]
print('k_mec:', k_mec)

# Generating the varying terms of  N(k) for the graph by multiplying sk2me, q_ke2 and k_mec
res = [sk2me[i]*q_ke2[i]*k_mec[i] for i in range(len(k))]
print('res:', res)

# plotting k (kinetic energy) vs res (N(k))
plt.plot(k, res, marker='o', markerfacecolor='green')

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

plt.grid()
# Calling the show method to show the result
plt.show()



# DATA will look like this

k= [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6]
rme= [0.511, 0.511, 0.511, 0.511, 0.511, 0.511, 0.511, 0.511, 0.511, 0.511, 0.511, 0.511, 0.511]
rme_2= [1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02]
k2me= [1.02, 1.07, 1.12, 1.17, 1.22, 1.27, 1.32, 1.37, 1.42, 1.47, 1.52, 1.57, 1.62]
sk2me= [0.0, 0.23130067012440755, 0.33466401061363027, 0.4189272013130682, 0.4939635614091388, 0.5634713834792322, 0.6292853089020909, 0.6924593850905625, 0.7536577472566709, 0.8133265027035576, 0.8717797887081347, 0.9292470069900683, 0.985900603509299]
qb= [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
q_ke= [0.6, 0.5499999999999999, 0.5, 0.44999999999999996, 0.39999999999999997, 0.35, 0.3, 0.25, 0.19999999999999996, 0.14999999999999997, 0.09999999999999998, 0.04999999999999993, 0.0]
q_ke2= [0.36, 0.30249999999999994, 0.25, 0.20249999999999996, 0.15999999999999998, 0.12249999999999998, 0.09, 0.0625, 0.03999999999999998, 0.02249999999999999, 0.009999999999999995, 0.0024999999999999935, 0.0]
k_mec= [0.511, 0.561, 0.611, 0.661, 0.7110000000000001, 0.761, 0.8109999999999999, 0.861, 0.911, 0.9610000000000001, 1.0110000000000001, 1.061, 1.111]
res= [0.0, 0.03925230197178727, 0.05111992762123202, 0.05607445321375746, 0.05619329474590362, 0.052528211046392714, 0.04593153469676361, 0.03726297066018589, 0.027463288310033074, 0.017586152304707666, 0.008813693663839238, 0.0024648276860411494, 0.0]
r

