# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/004_Probability_and_statistics/001_Understand_probability && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

import numpy as np

# ================================================================================
# Purpose of statistics
# - Extract sample data from population
# - Inference parameters of population via sample data

# Why you inference parameters of population via sample data?
# - It's generally impossible to directly calculate parameters of population 

# ================================================================================
# Why statistics uses probability?
# - Even good statistics can't make 100% accurate result
# So, crebility of statistics is represented by probability

# - High credibility: high probability of true

# ================================================================================
# Characteristics of probability

# 1. $$$\sum\limits_{i=1}^{n}P(E_i)=1$$$
# E: event
# i: number of trials
# P: probability of event occuring

probs_of_dice=[1/6,1/6,1/6,1/6,1/6,1/6]
# print("probs_of_dice",probs_of_dice)
# [0.16666666666666666, 0.16666666666666666, 0.16666666666666666, 0.16666666666666666, 0.16666666666666666, 0.16666666666666666]

sum_of_all_probs=round(np.sum(probs_of_dice),1)
# print("sum_of_all_probs",sum_of_all_probs)
# 1.0

# ================================================================================
# ./pics/2019_07_16_09:39:57.png

# ./pics/2019_07_16_09:39:45.png

# event_A: multiples of 2
# event_B: multiples of 3
# P(A and B)

U_set=[1,2,3,4,5,6,7,8,9,10]
number_of_U_set_element=len(U_set)

A_event_set=[2,4,6,8,10]
A_len=len(A_event_set)

B_event_set=[3,6,9]
B_len=len(B_event_set)

A_and_B_event_set=[6]
A_and_B_len=len(A_and_B_event_set)

prob_A_occuring=A_len/number_of_U_set_element
prob_B_occuring=B_len/number_of_U_set_element
prob_A_and_B_ocurring=A_and_B_len/number_of_U_set_element

prob_A_or_B_occuring=round(prob_A_occuring+prob_B_occuring-prob_A_and_B_ocurring,1)
# print("prob_A_or_B_occuring",prob_A_or_B_occuring)
# 0.7

# ./pics/2019_07_16_09:44:48.png

# ================================================================================
# ./pics/2019_07_16_09:45:05.png

# A and B events are independent

# ================================================================================
# ./pics/2019_07_16_09:45:25.png









