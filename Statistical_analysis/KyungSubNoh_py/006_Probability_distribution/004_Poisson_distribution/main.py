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
from scipy.stats import poisson
import matplotlib.pyplot as plt

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
  
  
  prob_value=(lambda_value**x)*(np.e**(-lambda_value))/math.factorial(x)
  return round(prob_value,2)

# ================================================================================
lambda_value=3

# ================================================================================
# P(X<=1)

result_prob_x_1=calculate_poisson_distribution_probability(x=1,lambda_value=lambda_value)
# print("result_prob_x_1",result_prob_x_1)
# 0.15

# ================================================================================
result_prob_x_0=calculate_poisson_distribution_probability(x=0,lambda_value=lambda_value)
# print("result_prob_x_0",result_prob_x_0)
# 0.05

# ================================================================================
result_prob_x_less_than_1=result_prob_x_1+result_prob_x_0
# print("result_prob_x_less_than_1",result_prob_x_less_than_1)
# 0.2

print(str(result_prob_x_less_than_1*100)+"%")
# 20.0%

# ================================================================================
# Calculate following probability 
# P(4<=x<=5)

result_prob_x_4=calculate_poisson_distribution_probability(x=4,lambda_value=lambda_value)
# print("result_prob_x_4",result_prob_x_4)
# 0.17

result_prob_x_5=calculate_poisson_distribution_probability(x=5,lambda_value=lambda_value)
# print("result_prob_x_5",result_prob_x_5)
# 0.1

result_prob_x_4_5=result_prob_x_4+result_prob_x_5
# print("result_prob_x_4_5",result_prob_x_4_5)
# 0.27

# ================================================================================
lambda_vals=list(range(1,8))
# print("lambda_vals",lambda_vals)
# [1, 2, 3, 4, 5, 6, 7]

x_vals=list(range(1,11))
# print("x_vals",x_vals)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dict_for_poisson_dist={}
list_for_poisson_dist=[]
for one_lambda in lambda_vals:
  for one_x in x_vals:
    y_proba_val=calculate_poisson_distribution_probability(one_x,one_lambda)
    # print("y_proba_val",y_proba_val)
    list_for_poisson_dist.append(y_proba_val)
  dict_for_poisson_dist[one_lambda]=list_for_poisson_dist

# print("dict_for_poisson_dist",dict_for_poisson_dist)

# ================================================================================
plt.plot([dict_for_poisson_dist[1],dict_for_poisson_dist[2]])
# plt.plot()
# plt.plot(dict_for_poisson_dist[3])
# plt.plot(dict_for_poisson_dist[4])
# plt.plot(dict_for_poisson_dist[5])
# plt.plot(dict_for_poisson_dist[6])
# plt.plot(dict_for_poisson_dist[7])
plt.show()
