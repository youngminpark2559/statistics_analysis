# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/006_Probability_distribution/004_Poisson_distribution && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

# ================================================================================
# Poisson distribution
# Probability distribution where specific event has very low probability of occurring

# Probability of professional horse rider falls off
# Probability of the bus arriving when you arrive the bus station

# Use Poisson distribution in above cases

# ================================================================================
# Number of riding horse: n

# Number of falling off: x

# /home/young/Pictures/2019_07_16_14:15:42.png

# /home/young/Pictures/2019_07_16_14:16:04.png

# ================================================================================
# /home/young/Pictures/2019_07_16_14:16:28.png

# ================================================================================
def calculate_poisson_distribution_probability(x,lambda_value):
  prob_value=(lambda_value**x)*(np.exp**(-lambda_value))/factorial(x)
  return prob_value

# ================================================================================
lambda_value=3

# ================================================================================
# P(X<=1)

result_prob=calculate_poisson_distribution_probability(x=1,lambda_value=lambda_value)
print("result_prob",result_prob)
afaf

