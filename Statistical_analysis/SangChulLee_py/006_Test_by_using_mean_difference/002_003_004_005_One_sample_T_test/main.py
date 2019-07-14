# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/002_003_004_005_One_sample_T_test && \
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
# from scipy import stats
import scipy.stats as stats
import math

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/002_003_004_005_One_sample_T_test/pics/2019_07_14_07:39:41.png

# Most cases use "two-sided test"
# equal or not equal

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/002_003_004_005_One_sample_T_test/pics/2019_07_14_07:41:32.png

# Probability of H_0 is true is tested by using "two-sided test"

# ================================================================================
# Some cases should have to see "greater or less"
# Then, you can use "right-sided test" or "left-sided test"

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/002_003_004_005_One_sample_T_test/pics/2019_07_14_07:43:12.png

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/002_003_004_005_One_sample_T_test/pics/2019_07_14_07:42:47.png

# ================================================================================
OST_df=pd.read_csv('./Data/01.OST.csv',encoding='utf8')
# print("OST_df",OST_df)
#      weight
# 0  319.3148
# 1  241.9693
# 2  290.9807
# 3  276.0801
# 4  347.5499
# 5  298.8435
# 6  292.8708
# 7  303.5787
# 8  296.1497

# ================================================================================
# print("OST_df",OST_df.describe())
#            weight
# count  9.000000  
# mean   296.370833
# std    28.758441 
# min    241.969300
# 25%    290.980700
# 50%    296.149700
# 75%    303.578700
# max    347.549900

# ================================================================================
# print("type(OST_df.describe())",type(OST_df.describe()))
# <class 'pandas.core.frame.DataFrame'>

# ================================================================================
OST_df.describe().plot(kind="bar")
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/002_003_004_005_One_sample_T_test/pics/2019_07_14_09:11:24.png

# ================================================================================
fig,axes0_for_box_plot=plt.subplots()

axes0_for_box_plot.boxplot(OST_df["weight"],sym="bo")

plt.title('Box plot of weight')
plt.xticks([1], ['weight'])
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/002_003_004_005_One_sample_T_test/pics/2019_07_14_09:10:52.png

# ================================================================================
fig2,axes2_for_hist=plt.subplots()

# n,bins,patches=axes2_for_hist.hist(OST_df["weight"],bins=10)
n,bins,patches=axes2_for_hist.hist(OST_df["weight"])

plt.title("Histogram of weight data")
plt.xlabel("Weight values")
plt.ylabel("Number of people")
plt.subplots_adjust(wspace=None,hspace=0.3)
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/002_003_004_005_One_sample_T_test/pics/2019_07_14_09:15:57.png

# ================================================================================
#generate 20 random heights with mean of 180, standard deviation of 5
# heights = [180 + np.random.normal(0, 5) for _ in range(20)]
 
#perform 1-sample t-test
tTestResult=stats.ttest_1samp(OST_df["weight"], 320)
# print("tTestResult",tTestResult)
# Ttest_1sampResult(statistic=-2.4649285039859006, pvalue=0.039017756111045764)

# ================================================================================
statistic,pvalue=tTestResult

# print("T-statistic",round(statistic,2))
# -2.46

# print("pvalue",round(pvalue,2))
# 0.04

# If p<0.05, H_0 is rejected

# From above result, you obtained p=0.04

# p=0.04 means "if H_0 is true, the probability of you getting above sample is 0.04 (very low)"
# So, you can say H_0 is false claim, which should be rejected

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/002_003_004_005_One_sample_T_test/pics/2019_07_14_09:44:30.png

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/002_003_004_005_One_sample_T_test/pics/2019_07_14_09:44:46.png

# ================================================================================
mu = 320
variance = 2
sigma = math.sqrt(variance)

x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

fig3,axes3_for_normal_dist=plt.subplots()

axes3_for_normal_dist.plot(x, stats.norm.pdf(x, mu, sigma))
axes3_for_normal_dist.axvline(x=320,color='k',linestyle='--')
# 95% credibility region --> 1.96
axes3_for_normal_dist.axvline(x=320+1.96*sigma,color='b',linestyle='--')
axes3_for_normal_dist.axvline(x=320-1.96*sigma,color='b',linestyle='--')
axes3_for_normal_dist.axvline(x=OST_df["weight"].mean(),color='r',linestyle='--')

plt.title("After perform two-sided T test")
plt.xlabel("Weight of icecreat pint")
plt.ylabel("Probability")
plt.xlim(290, 330)
plt.ylim(0, 0.4)
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/002_003_004_005_One_sample_T_test/pics/2019_07_14_10:05:18.png
