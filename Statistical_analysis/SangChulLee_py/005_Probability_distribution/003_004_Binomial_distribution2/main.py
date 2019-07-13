# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/005_Probability_distribution/003_Binomial_distribution2 && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns',None)
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from statsmodels.robust.scale import mad
from scipy.stats import binom

# ================================================================================
# Calculate a few first moments:

# c n: number of trial (Bernoulli experiment)
n=5

# c p: probability of True occuring
p=0.4

# ================================================================================
mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')

# ================================================================================
# Display the probability mass function (pmf):
x = np.arange(binom.ppf(0.01, n, p),binom.ppf(0.99, n, p))

# c fig: one canvas
# c ax: one axes
fig, ax = plt.subplots(1, 1)

ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)

plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/003_Binomial_distribution2/pics/2019_07_13_19:59:42.png

# ================================================================================
# Alternatively, the distribution object can be called (as a function) to fix the shape and location. 
# This returns a “frozen” RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen pmf:

# c rv: frozen binom RV
rv = binom(n, p)

prob_y=rv.pmf(x)
# print("prob_y",prob_y)
# [0.07776 0.2592  0.3456  0.2304  0.0768 ]

fig2,axes2=plt.subplots()

axes2.vlines(x, 0, prob_y, colors='k', linestyles='-', lw=1, label='frozen pmf')
axes2.legend(loc='best', frameon=False)

plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/003_Binomial_distribution2/pics/2019_07_13_20:03:30.png

# ================================================================================
# Check accuracy of cdf and ppf:

prob = binom.cdf(x, n, p)
plt.bar(x,prob)
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/003_Binomial_distribution2/pics/2019_07_13_20:07:46.png

# np.allclose(x, binom.ppf(prob, n, p))
# True

# Generate random numbers:
r = binom.rvs(n, p, size=1000)
# print("r",r)
# [2 1 0 4 3 1 1 3 2 1 3 1 1 2 4 2 5 2 2 1 2 3 0 5 4 2 0 3 3 3 2 1 3 2 2 2 2

