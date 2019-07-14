# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/010_011_012_Paired_sample_T_test && \
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
import random
import scipy.stats as scipy_stats
import math
import scipy as sp

# ================================================================================
# Paired sample: Paired sample with respect to time

# ================================================================================
# Problem

# - A company made diet drug
# - Diet drug should reduce weight within 3 months
# - Measrue one person's weight before drug
# - Measrue one person's weight after drug

# ================================================================================
# H_0: no reduction in weight
# $$$H_0:\mu_d = 0$$$

# H_1: weight reduction happened
# $$$H_1:\mu_d \ne 0$$$

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/010_011_Paired_sample_T_test/pics/2019_07_14_14:17:26.png

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/010_011_Paired_sample_T_test/pics/2019_07_14_14:17:54.png

# ================================================================================
weight_change_df=pd.read_csv('./Data/03.PST.csv',encoding='utf8')
# print("weight_change_df",weight_change_df)
#    ID  pre  post
# 0  1   82   75  
# 1  2   54   50  
# 2  3   74   74  
# 3  4   75   71  
# 4  5   71   69  
# 5  6   76   73  
# 6  7   70   68  
# 7  8   62   62  
# 8  9   77   68  
# 9  10  75   72  

# ================================================================================
weight_change_df["difference"]=weight_change_df["post"]-weight_change_df["pre"]
# print("weight_change_df",weight_change_df)
#    ID  pre  post  difference
# 0  1   82   75   -7         
# 1  2   54   50   -4         
# 2  3   74   74    0         
# 3  4   75   71   -4         
# 4  5   71   69   -2         
# 5  6   76   73   -3         
# 6  7   70   68   -2         
# 7  8   62   62    0         
# 8  9   77   68   -9         
# 9  10  75   72   -3         

# ================================================================================
weight_change_df_describe=weight_change_df.describe()
# print("weight_change_df_describe",weight_change_df_describe)
#              ID        pre       post  difference
# count  10.00000  10.000000  10.000000  10.000000 
# mean   5.50000   71.600000  68.200000 -3.400000  
# std    3.02765   8.099383   7.420692   2.836273  
# min    1.00000   54.000000  50.000000 -9.000000  
# 25%    3.25000   70.250000  68.000000 -4.000000  
# 50%    5.50000   74.500000  70.000000 -3.000000  
# 75%    7.75000   75.750000  72.750000 -2.000000  
# max    10.00000  82.000000  75.000000  0.000000  

# ================================================================================
axes1_for_box_plot=plt.subplot(2,1,1)
axes1_for_box_plot.hist(weight_change_df["pre"],bins=10)

plt.title('Weight histogram of before/after drug')
plt.xlabel("weights")
plt.ylabel("Number of people")

axes2_for_box_plot=plt.subplot(2,1,2)
axes2_for_box_plot.hist(weight_change_df["post"],bins=10)

plt.title('Weight histogram of before/after drug')
plt.xlabel("weights")
plt.ylabel("Number of people")

plt.tight_layout()
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/010_011_Paired_sample_T_test/pics/2019_07_14_15:17:51.png

# ================================================================================
fig1,axes1_for_boxplot=plt.subplots()

axes1_for_boxplot.boxplot([weight_change_df["difference"]],sym="bo")

plt.title('Box plot of weight changes')
plt.ylabel("Weight changes")
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/010_011_Paired_sample_T_test/pics/2019_07_14_15:20:58.png

# ================================================================================
tTestResult=scipy_stats.ttest_rel(weight_change_df["pre"],weight_change_df["post"])
# print("tTestResult",tTestResult)
# Ttest_relResult(statistic=3.790800145860548, pvalue=0.004277392636696301)

# "H_0: no reduction" is rejected

# ================================================================================
mu = 0
sigma = 0.7

x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

fig3,axes3_for_normal_dist=plt.subplots()

axes3_for_normal_dist.plot(x, scipy_stats.norm.pdf(x, mu, sigma))
axes3_for_normal_dist.axvline(x=0,color='k',linestyle='--')
# 95% credibility region --> 1.96
axes3_for_normal_dist.axvline(x=0+1.96*sigma,color='b',linestyle='--')
axes3_for_normal_dist.axvline(x=0-1.96*sigma,color='b',linestyle='--')
axes3_for_normal_dist.axvline(x=weight_change_df["difference"].mean(),color='r',linestyle='--')

plt.title("After perform paried_sample two-sided T test")
plt.xlabel("Weight change values")
plt.ylabel("Probability")
# plt.xlim(290, 330)
# plt.ylim(0, 0.4)
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/010_011_012_Paired_sample_T_test/pics/2019_07_14_15:43:57.png
