# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/006_007_008_009_Independent_sample_T_test && \
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
# Problem:
# - You want to replace the car tire
# - You want to use long lifespan tire
# - There are A tire company and B tire company
# - Suppose you tested 30 number of tires (60 tires in total) until it becomes worn out
# to measure "worn out time"
# - Data: 2.IST.sav

# ================================================================================
# H_0: 
# - null hypothesis
# - Tire of A company and tire of B company have no difference in "worn out"
# $$$H_0: \mu_1=\mu_2$$$
# $$$H_0: \mu_1-\mu_2=0$$$
# $$$H_0: \mu_1-\mu_2=D_0$$$

# H_1: 
# - research hypothesis
# - Tire of A company and tire of B company have difference in "worn out"
# - two sided test
# $$$H_1:\mu_1 \ne \mu_2$$$
# $$$H_1:\mu_1 - \mu_2 \ne 0$$$
# $$$H_1:\mu_1 - \mu_2 \ne D_0$$$


# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/006_007_008_009_Independent_sample_T_test/pics/2019_07_14_11:36:15.png

# 2 populations

# $$$\bar{X}$$$ is sample mean

# Difference between $$$\bar{X}_A$$$ and $$$\bar{X}_A$$$ comes from sample or population 
# Prove it by using statistical test

# ================================================================================
# When 2 distributions have same variance, you can calculate difference by using 48.670 and 51.377

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/006_007_008_009_Independent_sample_T_test/pics/2019_07_14_11:40:30.png

# ================================================================================
# When 2 distributions have difference variance, you can calculate difference by using 48.670 and 51.377

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/006_007_008_009_Independent_sample_T_test/pics/2019_07_14_11:40:47.png

# ================================================================================
# Those 2 methods have difference calculation because they have difference variance

# ================================================================================
# If 2 populations have "same variance"

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/006_007_008_009_Independent_sample_T_test/pics/2019_07_14_11:41:55.png

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/006_007_008_009_Independent_sample_T_test/pics/2019_07_14_11:42:15.png

# ================================================================================
# If 2 populations have "unequal variance"

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/006_007_008_009_Independent_sample_T_test/pics/2019_07_14_11:42:30.png

# ================================================================================
# How to solve above problem

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/006_007_008_009_Independent_sample_T_test/pics/2019_07_14_11:44:49.png

# - Confirmed they have equal variance

# p=0.01 < 0.05

# 0.01: probability of H_0 correct

# From 1.0 probability of H_0 correct, probability goes up to 0.05
# If $$$0.05 \le p \le 1.0$$$, " $$$H_0$$$ is correct" is proved, (it has "allowed error")

# Since p=0.01 < 0.05, $$$H_0$$$ (tire of A company and tire of B company have no difference in lifespan) is proved as false sentence

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/006_007_008_009_Independent_sample_T_test/pics/2019_07_14_11:48:55.png

# ================================================================================
tire_time_df=pd.read_csv('./Data/02.ist.csv',encoding='utf8')
# print("tire_time_df",tire_time_df)
#     t_group  t_time
# 0   1        38187 
# 1   1        37245 
# 2   1        41020 
# 3   1        30732 
# 4   1        52416 
# 5   1        49278 
# 6   1        38214 
# 7   1        36742 
# 8   2        48760 
# 9   2        54280 
# 10  2        50635 
# 11  2        51052 
# 12  2        59214 
# 13  2        54052 
# 14  2        44187 
# 15  2        45187 

# ================================================================================
t_group_sr=tire_time_df["t_group"]
t_group_sr[t_group_sr==1]="A_tire"
t_group_sr[t_group_sr==2]="B_tire"

tire_time_df["t_group"]=t_group_sr

# print("tire_time_df",tire_time_df)
#    t_group  t_time
# 0   A_tire  38187 
# 1   A_tire  37245 
# 2   A_tire  41020 
# 3   A_tire  30732 
# 4   A_tire  52416 
# 5   A_tire  49278 
# 6   A_tire  38214 
# 7   A_tire  36742 
# 8   B_tire  48760 
# 9   B_tire  54280 
# 10  B_tire  50635 
# 11  B_tire  51052 
# 12  B_tire  59214 
# 13  B_tire  54052 
# 14  B_tire  44187 
# 15  B_tire  45187 

# ================================================================================
tire_time_df_describe=tire_time_df.describe()
# print("tire_time_df_describe",tire_time_df_describe)
#              t_time
# count  16.000000   
# mean   48200.062500
# std    4673.170836 
# min    38214.000000
# 25%    46353.250000
# 50%    49019.000000
# 75%    51028.000000
# max    54280.000000

# ================================================================================
A_tire_sr=tire_time_df[tire_time_df["t_group"]=="A_tire"]
# print("A_tire_sr",A_tire_sr)
#   t_group  t_time
# 0  A_tire  38187 
# 1  A_tire  37245 
# 2  A_tire  41020 
# 3  A_tire  30732 
# 4  A_tire  52416 
# 5  A_tire  49278 
# 6  A_tire  38214 
# 7  A_tire  36742 

B_tire_sr=tire_time_df[tire_time_df["t_group"]=="B_tire"]
# print("B_tire_sr",B_tire_sr)
#    t_group  t_time
# 8   B_tire  48760 
# 9   B_tire  54280 
# 10  B_tire  50635 
# 11  B_tire  51052 
# 12  B_tire  59214 
# 13  B_tire  54052 
# 14  B_tire  44187 
# 15  B_tire  45187 

# ================================================================================
axes1_for_box_plot=plt.subplot(2,2,1)

axes1_for_box_plot.boxplot([A_tire_sr["t_time"]],sym="bo")

plt.title('Box plot of worn out time')
plt.xticks([1], ['A_tire'])
plt.ylabel("Worn out time")

# ================================================================================
axes2_for_box_plot=plt.subplot(2,2,2)

axes2_for_box_plot.boxplot([B_tire_sr["t_time"]],sym="bo")

plt.title('Box plot of worn out time')
plt.xticks([1], ['B_tire'])
plt.ylabel("Worn out time")

# ================================================================================
axes3_for_hist=plt.subplot(2,2,3)

axes3_for_hist.hist(A_tire_sr["t_time"],bins=10)

plt.title('Histogram of worn out time of A tire')
plt.ylabel("Worn out time")
plt.ylabel("Number of tire")

# ================================================================================
axes4_for_hist=plt.subplot(2,2,4)

axes4_for_hist.hist(B_tire_sr["t_time"],bins=10)

plt.title('Histogram of worn out time of B tire')
plt.ylabel("Worn out time")
plt.ylabel("Number of tire")

# ================================================================================
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/006_007_008_009_Independent_sample_T_test/pics/2019_07_14_13:46:14.png

# ================================================================================
# Equal variance test
# Use 3 algorithms (bartlett, fligner, levene)

x1=A_tire_sr["t_time"]
x2=B_tire_sr["t_time"]

# H_0: 2 variances are equal

res_bartlett=sp.stats.bartlett(x1, x2)
# print("res_bartlett",res_bartlett)
# BartlettResult(statistic=0.796720673493735, pvalue=0.3720756463616187)

res_fligner=sp.stats.fligner(x1, x2)
# print("res_fligner",res_fligner)
# FlignerResult(statistic=0.034077062093495175, pvalue=0.8535429939557165)

res_levene=sp.stats.levene(x1, x2)
# print("res_levene",res_levene)
# LeveneResult(statistic=0.21551444557159374, pvalue=0.6496157686988846)

# ================================================================================
tTestResult = scipy_stats.ttest_ind(x1, x2)
# print("tTestResult",tTestResult)
# Ttest_indResult(statistic=-3.4171504415997087, pvalue=0.004168243859583699)

# p=0.8>0.05
# Therefore, "H_0: Tire of A company and tire of B company have no difference in 'worn out'" is adopted

# ================================================================================
A_tire_mean=x1.mean()
# print("A_tire_mean",A_tire_mean)
# 40479.25

A_tire_var=x1.var()
# print("A_tire_var",A_tire_var)
# 50002639.071428575

A_tire_std=x1.std()
# print("A_tire_std",A_tire_std)
# 7071.254419933466

B_tire_mean=x2.mean()
# print("B_tire_mean",B_tire_mean)
# 50920.875

B_tire_var=x2.var()
# print("B_tire_var",B_tire_var)
# 24693468.69642857

B_tire_std=x2.std()
# print("B_tire_std",B_tire_std)
# 4969.252327707718

# ================================================================================
mu = A_tire_mean
variance = A_tire_var
sigma = A_tire_std

x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

fig3,axes3_for_normal_dist=plt.subplots()

axes3_for_normal_dist.plot(x, scipy_stats.norm.pdf(x, mu, sigma))
axes3_for_normal_dist.axvline(x=mu,color='r',linestyle='--')

# ================================================================================
mu_B = B_tire_mean
variance_B = B_tire_var
sigma_B = B_tire_std

x_B = np.linspace(mu_B - 3*sigma_B, mu_B + 3*sigma_B, 100)

axes3_for_normal_dist.plot(x_B, scipy_stats.norm.pdf(x_B, mu_B, sigma_B))
axes3_for_normal_dist.axvline(x=mu_B,color='r',linestyle='--')

# ================================================================================
plt.title("Plots about 2 samples from 2 populations")
plt.xlabel("Worn time")
plt.ylabel("Number of tires")
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/006_007_008_009_Independent_sample_T_test/pics/2019_07_14_13:43:45.png

# ================================================================================
