import math
import pandas as pd
import numpy as np
from scipy.stats import norm
from print_errors import print_distr
import os

# maximal and minimal t values
min_t = -4
max_t = 6

# H0: myu = 0.01, H1: myu != 0.01
h0 = 0.01

fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)
filename = parentDir + "/data/data.csv"
# sample data
sample_t = pd.read_csv(filename)
n = len(sample_t)

# calculate sample mean
sample_mean = sample_t.mean()
print("Sample mean: {0}".format(round(sample_mean[0],3)))

# calculate sample variance
sample_variance = sample_t.var()
print("Sample variance: {0}".format(round(sample_variance[0],3)))

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

print_distr(t_crit_right=t_crit_right, t_crit_left=t_crit_left, t=t, u0=u0, u1=u1)