# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/005_Probability_distribution/006_Poisson_distribution2 && \
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
from scipy.stats import poisson

# ================================================================================
mu = 0.6

mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')

# ================================================================================
# Display the probability mass function (pmf):

x = np.arange(poisson.ppf(0.01, mu),
              poisson.ppf(0.99, mu))

fig, ax = plt.subplots(1, 1)

ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
ax.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)
plt.show()

# ================================================================================
# Alternatively, the distribution object can be called (as a function) to fix the shape and location. This returns a “frozen” RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen pmf:

# rv = poisson(mu)
# ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
# ...         label='frozen pmf')
# ax.legend(loc='best', frameon=False)
# plt.show()
# ../_images/scipy-stats-poisson-1_00_00.png
# Check accuracy of cdf and ppf:


# prob = poisson.cdf(x, mu)
# np.allclose(x, poisson.ppf(prob, mu))
# True
# Generate random numbers:


# r = poisson.rvs(mu, size=1000)
