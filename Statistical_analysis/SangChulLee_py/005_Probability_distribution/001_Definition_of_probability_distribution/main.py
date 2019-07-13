# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/005_Probability_distribution/001_Definition_of_probability_distribution && \
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

# ================================================================================
sample_space=[1,2,3,4,5,6]

occured_event=[5]

# c prob_of_5_occuring: probability of 5 occuring
prob_of_5_occuring=len(occured_event)/len(sample_space)
# print("prob_of_5_occuring",prob_of_5_occuring)
# 0.16666666666666666

# ================================================================================
# Random variable tutorial

def discrete_random_variable():
  one_random_number=np.random.randint(1,6,size=1)
  # print("one_random_number",one_random_number)
  # [5]
  return one_random_number

discrete_value=discrete_random_variable()
# print("discrete_value",discrete_value)
# [2]

number_of_rolling_dice=1000000

numbers_from_rolling_dice=[]

for _ in range(number_of_rolling_dice):
  discrete_value=discrete_random_variable()
  numbers_from_rolling_dice.append(discrete_value[0])

# print("numbers_from_rolling_dice",numbers_from_rolling_dice)
# [2, 4, 2, 5, 4, 2, 3, 1, 3, 5, 5, 3, 5,

fig,axes_for_hist=plt.subplots()

axes_for_hist.hist(numbers_from_rolling_dice,bins=20)

plt.title("Number distribution from rolling dice")
plt.xlabel("Number")
plt.ylabel("Number of occuring")
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/001_Definition_of_probability_distribution/pics/2019_07_13_19:03:50.png

# ================================================================================
def continuous_random_variable():
  forty=[40.1]*8
  forty2=[44.6]*10
  fifty=[50.2]*44
  fifty2=[50.6]*50
  sixty=[60.5]*150
  sixty2=[61.5]*170
  seventy=[70.1]*61
  seventy2=[75.1]*44
  eighty=[80.8]*12
  eighty=[82.8]*11

  entire_weights=forty+forty2+fifty+fifty2+sixty+sixty2+seventy+seventy2+eighty+eighty
  # print("entire_weights",entire_weights)
  # [40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 44.6, 44.6, 44.6, 44.6, 44.6, 44.6, 44.6, 44.6, 44.6, 44.6, 50.2, 50.2, 50.2, 50.2, 50.2, 50.2, 50.2, 50.2, 50.2, 50.2, 50.2, 50.2, 50.2, 50.2, 

  one_random_weight_index=np.random.randint(0,len(entire_weights),size=1)[0]
  # print("one_random_weight_index",one_random_weight_index)
  # 18

  one_random_weight=entire_weights[one_random_weight_index]
  
  return one_random_weight

one_random_weight=continuous_random_variable()
# print("one_random_weight",one_random_weight)
# 70.1

# ================================================================================
number_of_extracting_people=1000000

weights_from_extracting_people=[]

for _ in range(number_of_extracting_people):
  one_random_weight=continuous_random_variable()
  weights_from_extracting_people.append(one_random_weight)

# print("weights_from_extracting_people",weights_from_extracting_people)
# [61.5, 70.1, 44.6, 61.5, 61.5, 60.5, 60.5, 60.5, 61.5,

fig,axes_for_weight_hist=plt.subplots()

axes_for_weight_hist.hist(weights_from_extracting_people,bins=20)

plt.title("Weight distribution from extracting people")
plt.xlabel("Weight")
plt.ylabel("Number of weight occuring")
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/001_Definition_of_probability_distribution/pics/2019_07_13_19:16:11.png

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/001_Definition_of_probability_distribution/pics/2019_07_13_19:16:55.png

# ================================================================================
