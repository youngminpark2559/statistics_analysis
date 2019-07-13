# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/005_Probability_distribution/002_Binomial_distribution && \
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
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/002_Binomial_distribution/pics/2019_07_13_19:28:02.png

# ================================================================================
# Binomial distribution is the probability distribution 
# which is used for "possible case" has 2 (man or woman, yes or no)

# ================================================================================
# Bernoulii experiments: birthing baby (boy or girl)

# ================================================================================
# Bernoulii experiments ---> Binomial distribution

# ================================================================================
# Fortune cookie: 
# luck chance: 90%
# unluck chance: 10%

# Probability of 3 customers not getting "luck"

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/002_Binomial_distribution/pics/2019_07_13_19:30:48.png

# ================================================================================
cookies=["luck","luck","luck","luck","luck","luck","luck","luck","luck","bad"]

customer1=cookies[np.random.randint(0,len(cookies),size=1)[0]]
# print("customer1",customer1)
# luck

customer2=cookies[np.random.randint(0,len(cookies),size=1)[0]]
# print("customer2",customer2)
# luck

customer3=cookies[np.random.randint(0,len(cookies),size=1)[0]]
# print("customer3",customer3)
# bad

# ================================================================================
number_of_customers=100000

history=[]
for _ in range(number_of_customers):
  customer_i=cookies[np.random.randint(0,len(cookies),size=1)[0]]  
  history.append(customer_i)

# print("history",history)
# ['luck', 'luck', 'luck', 'luck', 'luck', 'luck', 'luck', 'luck', 'luck', 'luck',

# ================================================================================
fig,axes_for_luck_hist=plt.subplots()

axes_for_luck_hist.hist(history,bins=20)

plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/002_Binomial_distribution/pics/2019_07_13_19:41:17.png

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/002_Binomial_distribution/pics/2019_07_13_19:44:59.png
