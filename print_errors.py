import math

def calculate_crit_value(alpha):
	return math.sqrt(2*math.log((1-2*alpha)*math.sqrt(2*math.pi)/2))

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import laplace
import matplotlib.patches as mpatches
from scipy.stats import norm

# maximal and minimal t values
min_t = -4
max_t = 6

# H0: myu = 0.01, H1: myu != 0.01
h0 = 0.01

# sample data
sample_t = [0, 0, 0, 0, 0, 0.01, -0.2, -0.3, 0.1, 0.4]
n = len(sample_t)

# calculate sample mean
sample_mean = np.sum(sample_t)/n
print("Sample mean: {0}".format(sample_mean))

# calculate sample variance
sample_variance = np.sum(pow(sample_t-sample_mean, 2))/n
print("Sample variance: {0}".format(sample_variance))

t = np.arange(min_t, max_t, 0.01)

#calculate observed statistics value
u_statistics = (sample_mean - h0)*math.sqrt(n)/sample_variance
print('t_observed: {0}'.format(round(u_statistics,3)))

u0 = [0] * len(t)
u1 = [0] * len(t)

# calculate normal distribution for H0 and H1 statistics
for ind, h in enumerate(t):
	u0[ind] = norm.pdf(h)
	u1[ind] = norm.pdf(h, 4, 1.5)

# calculate critical values for distribution
t_crit_right = 1.645
t_crit_left = -t_crit_right

# plot statistical distributions
h0_dist, = plt.plot(t, u0, 'r', alpha=0.35, label='PrD(T|H0)')
h1_dist, = plt.plot(t, u1, 'b', alpha=0.35, label='PrD(T|H1)')

# plot critical t values
left_crit_line = plt.axvline(
	x=t_crit_left, color='red', label='T_critical_left', 
	ymin = 0.05, ymax = 0.95, alpha=0.7, linewidth=1.5
	)
right_crit_line = plt.axvline(
	x=t_crit_right, color='blue', label='T_critical_right', 
	ymin = 0.05, ymax = 0.95, alpha=0.7, linewidth=1.5
	)

# fill in error areas
plt.fill_between(t, u1, where=t <= t_crit_right, facecolor='blue', alpha=0.35)
plt.fill_between(t, u0, where=t >= t_crit_right, facecolor='red', alpha=0.35)
plt.fill_between(t, u0, where=t <= t_crit_left, facecolor='red', alpha=0.35)

red_patch = mpatches.Patch(color='red', alpha=0.35, label='type 1 (alpha) error')
blue_patch = mpatches.Patch(color='blue', alpha=0.35, label='type 2 (beta) error')

# labels and legend
plt.xlabel('T')
plt.ylabel('Probability density')
plt.legend(
	handles=[h0_dist, h1_dist, left_crit_line, right_crit_line, red_patch, blue_patch], 
	loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=3
	)
plt.grid(True)
plt.show()

print(norm.cdf(0.05)-0.5)