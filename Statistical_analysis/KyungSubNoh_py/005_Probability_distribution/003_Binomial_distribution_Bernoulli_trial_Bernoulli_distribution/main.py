# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/006_Probability_distribution/003_Binomial_distribution_Bernoulli_trial_Bernoulli_distribution && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

# ================================================================================
# Bernoulli trial
# 2 kinds of result (True or False)
# True and False are independent

# ================================================================================
# Bernoulli distribution
# Perform Bernoulli trial
# Get probability wrt events
# Plot probabilities

# Probability of True: p(x=True)
# Probability of False: 1-p(x=True)

# ================================================================================
# ./pics/2019_07_16_13:21:43.png

# Expectation value
# Variance
# from Bernoulli distribution

# expectation_val_of_X=p
# variance_of_X=p(1-p)

# ================================================================================
# Binomial distribution

# Probability distribution from "continuous" Bernoulli trials

# Expectation value of binomial distribution
# mu=np

# Variance value of binomial distribution
# sigma_square=np(1-p)

# ================================================================================
# X ~ B(n,p)

# ================================================================================
# ./pics/2019_07_16_13:25:26.png

# ================================================================================
# Probability in binomial distribution

# n number of trials
# success probability: p
# number of sucess: r

# n trials
# r success
# nCr

# probability of r number of success
# probability of n-r number of fail

# Probability function for binomial distribution
# ./pics/2019_07_16_13:51:02.png

# ================================================================================
# ./pics/2019_07_16_13:51:32.png

# 10%: probability of A getting best job to this personality

# 49 companies participate the job-conference

# Calculate probability of A getting 2 companies which A likes

# ================================================================================
# n=49
# r=2
# p=0.1

# P(x=2) = (49! / 2!(49-2)!) * 0.1^2 * (1-0.1)^(49-2)
#        = 0.08313909
#        = 8.31%

# ================================================================================
def calculate_binomial_distribution(n,r,p):
  fact_n=math.factorial(n)
  fact_r=math.factorial(r)
  fact_n_r=math.factorial(n-r)
  power_p_2=np.power(p,2)
  power_1_p_n_r=np.power(1-p,n-r)

  prob_of_A_getting_2_best_job=fact_n/(fact_r*fact_n_r) * power_p_2 * power_1_p_n_r
  # print("prob_of_A_getting_2_best_job",prob_of_A_getting_2_best_job)
  # 0.08313908976417642
  
  return prob_of_A_getting_2_best_job

# ================================================================================
n=49
r=2
p=0.1

prob_value=calculate_binomial_distribution(n=n,r=r,p=p)
# print("prob_value",prob_value)
# 0.08313908976417642

# ================================================================================
