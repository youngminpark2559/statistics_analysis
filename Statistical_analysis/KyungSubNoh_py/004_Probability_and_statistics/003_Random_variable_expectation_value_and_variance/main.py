# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/004_Probability_and_statistics/003_Random_variable_expectation_value_and_variance && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np
from itertools import product

# ================================================================================
# ./pics/2019_07_16_10:23:54.png

all_possible_events=[1,2,3,4,5,6]
mean_value=np.mean(all_possible_events)
probability_of_each_event=[1/6,1/6,1/6,1/6,1/6,1/6]

# ================================================================================
# @ Characteristics of probability

summed_probs=np.sum(probability_of_each_event)
summed_probs=round(summed_probs,2)
# print("summed_probs",summed_probs)
# 1.0

# ================================================================================
# @ Expectation value

multiplied=np.array(all_possible_events)*np.array(probability_of_each_event)
# print("multiplied",multiplied)
# [0.16666667 0.33333333 0.5        0.66666667 0.83333333 1.        ]

summed=np.sum(multiplied)
summed=round(summed,2)
# print("summed",summed)
# 3.5

# ================================================================================
# ./pics/2019_07_16_10:27:35.png

# ================================================================================
# ./pics/2019_07_16_10:29:09.png

subtracted=np.array(all_possible_events)-np.array(mean_value)
# print("subtracted",subtracted)
# [-2.5 -1.5 -0.5  0.5  1.5  2.5]

powered_by_2=np.power(subtracted,2)
# print("powered_by_2",powered_by_2)
# [6.25 2.25 0.25 0.25 2.25 6.25]

multipled=powered_by_2*np.array(probability_of_each_event)
# print("multipled",multipled)
# [1.04166667 0.375      0.04166667 0.04166667 0.375      1.04166667]

summed=multipled.sum()
summed=round(summed,2)
# print("summed",summed)
# 2.92

# ================================================================================
# ./pics/2019_07_16_10:32:36.png

# ================================================================================
# ./pics/2019_07_16_10:33:26.png

# ================================================================================
std_of_RV=np.sqrt(summed)
# print("std_of_RV",std_of_RV)
# 1.7088007490635062

# ================================================================================
# ./pics/2019_07_16_10:34:34.png

incentives=[300,150,0,-100]
prob_of_each_incentive_A=[0.58,0.87,0.55,0.05]
prob_of_each_incentive_B=[0.65,0.51,0.45,0.05]

# ================================================================================
multiplied=np.array(incentives)*np.array(prob_of_each_incentive_A)
# print("multiplied",multiplied)
# [174.  130.5   0.   -5. ]
expectation_value_from_A=np.sum(multiplied)
# print("expectation_value_from_A",expectation_value_from_A)
# 299.5

multiplied=np.array(incentives)*np.array(prob_of_each_incentive_B)
# print("multiplied",multiplied)
# [174.  130.5   0.   -5. ]
expectation_value_from_B=np.sum(multiplied)
# print("expectation_value_from_B",expectation_value_from_B)
# 266.5

# print("Expectation value from A is larger than B?")
# print(expectation_value_from_A>expectation_value_from_B)
# True

# ================================================================================
subtracted_A=incentives-expectation_value_from_A
# print("subtracted_A",subtracted_A)
# [   0.5 -149.5 -299.5 -399.5]

variance_A=np.power(subtracted_A,2)*prob_of_each_incentive_A
# print("variance_A",variance_A)
# [1.45000000e-01 1.94447175e+04 4.93351375e+04 7.98001250e+03]
variance_A=round(np.sum(variance_A),2)
# print("variance_A",variance_A)
# 76760.01

# ================================================================================
subtracted_B=incentives-expectation_value_from_B
# print("subtracted_B",subtracted_B)
# [   0.5 -149.5 -299.5 -399.5]

variance_B=np.power(subtracted_B,2)*prob_of_each_incentive_B
# print("variance_B",variance_B)
# [1.45000000e-01 1.94447175e+04 4.93351375e+04 7.98001250e+03]
variance_B=round(np.sum(variance_B),2)
# print("variance_B",variance_B)
# 46327.44

# ================================================================================
