# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/008_ANOVA/001_002_003_004_One_way_ANOVA && \
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
import plotly
import scipy as sp
# ================================================================================
# K companies run 4 cafes (A region, B region, C region, D region)

# Satisfaction of each cafes has different values?

# If difference happens, which cafe has lowest satisfaction?

# ================================================================================
# H_0:
# there is no satisfaction difference in 4 cafes
# $$$H_0:\mu_1=\mu_2=\mu_3=\mu_4$$$

# H_1:
# there is at least one pair of difference from 4 cafes
# $$$H_1: \mu_1 \ne \mu_2 \;\;\; or \mu_1 \ne \mu_3 \;\;\; ... \;\;\; \mu_3 \ne \mu_4$$$

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/001_One_way_ANOVA/pics/2019_07_14_16:13:10.png

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/001_One_way_ANOVA/pics/2019_07_14_16:22:32.png

# ================================================================================
cafes_scores_df=pd.read_csv('./Data/04.OWA.csv',encoding='utf8')
# print("cafes_scores_df",cafes_scores_df)
#     group  score
# 0   cafeA  85   
# 1   cafeB  78   
# 2   cafeC  63   
# 3   cafeD  88   
# 4   cafeA  93   
# 5   cafeB  83   
# 6   cafeC  56   
# 7   cafeD  53   
# 8   cafeA  94   
# 9   cafeB  97   
# 10  cafeC  94   
# 11  cafeD  88   

# ================================================================================
cafes_group_sr=cafes_scores_df["group"]
# print("cafes_group_sr",cafes_group_sr)

# print('cafes_group_sr[cafes_group_sr=="cafeA"]',cafes_scores_df[cafes_group_sr=="cafeA"])
#    group  score
# 0  cafeA  85   
# 4  cafeA  93   
# 8  cafeA  94   

fig,axes0=plt.subplots()

axes0.boxplot([
  cafes_scores_df[cafes_group_sr=="cafeA"]["score"],cafes_scores_df[cafes_group_sr=="cafeB"]["score"],
  cafes_scores_df[cafes_group_sr=="cafeC"]["score"],cafes_scores_df[cafes_group_sr=="cafeD"]["score"]],sym="bo")

plt.title('Box plot of safisfaction score')
plt.ylabel('Safisfaction score')
plt.xticks([1,2,3,4], ['cafeA','cafeB','cafeC','cafeD'])
plt.show()
# /home/young/Pictures/2019_07_14_17:24:11.png

# ================================================================================
axes1_for_hist=plt.subplot(2,2,1)
axes1_for_hist.hist(cafes_scores_df[cafes_group_sr=="cafeA"]["score"],bins=10)
plt.title("Satisfaction score histogram of cafeA")
plt.ylabel("Satisfaction score")

axes1_for_hist=plt.subplot(2,2,2)
axes1_for_hist.hist(cafes_scores_df[cafes_group_sr=="cafeB"]["score"],bins=10)
plt.title("Satisfaction score histogram of cafeB")
plt.ylabel("Satisfaction score")

axes1_for_hist=plt.subplot(2,2,3)
axes1_for_hist.hist(cafes_scores_df[cafes_group_sr=="cafeC"]["score"],bins=10)
plt.title("Satisfaction score histogram of cafeC")
plt.ylabel("Satisfaction score")

axes1_for_hist=plt.subplot(2,2,4)
axes1_for_hist.hist(cafes_scores_df[cafes_group_sr=="cafeD"]["score"],bins=10)
plt.title("Satisfaction score histogram of cafeD")
plt.ylabel("Satisfaction score")

plt.show()
# /home/young/Pictures/2019_07_14_17:30:02.png

# ================================================================================
# 1. Equal variance test
# equal variance on each group?

x1=cafes_scores_df["score"]
x2=cafes_scores_df["score"]

x1=cafes_scores_df[cafes_group_sr=="cafeA"]["score"]
x2=cafes_scores_df[cafes_group_sr=="cafeB"]["score"]
x3=cafes_scores_df[cafes_group_sr=="cafeC"]["score"]
x4=cafes_scores_df[cafes_group_sr=="cafeD"]["score"]


# H_1: there is equal variance

res_bartlett=sp.stats.bartlett(x1,x2,x3,x4)
# print("res_bartlett",res_bartlett)
# BartlettResult(statistic=3.3770601080649034, pvalue=0.33706051468621384)

res_fligner=sp.stats.fligner(x1,x2,x3,x4)
# print("res_fligner",res_fligner)
# FlignerResult(statistic=0.29300193695256604, pvalue=0.9613392090236069)

res_levene=sp.stats.levene(x1,x2,x3,x4)
# print("res_levene",res_levene)
# LeveneResult(statistic=0.3358790056903263, pvalue=0.8000711689586899)

# Equal variance is confirmed

# ================================================================================
F_statistic,pVal=sp.stats.f_oneway(x1,x2,x3,x4)
# print("F_statistic",F_statistic)
# 1.0236742424242422

# print("pVal",pVal)
# 0.4319224208419047

# ================================================================================
if pVal < 0.05:
  print("pVal is enough small")
  print("It means there is mean-differences between groups")
else:
  print("pVal is not enough small")
  print("It means there is no mean-differences between groups")
# pVal is not enough small
# It means there is no mean-differences between groups

# ================================================================================
# print("cafes_scores_df",cafes_scores_df)
#     group  score
# 0   cafeA  85   
# 1   cafeB  78   
# 2   cafeC  63   
# 3   cafeD  88   
# 4   cafeA  93   
# 5   cafeB  83   
# 6   cafeC  56   
# 7   cafeD  53   
# 8   cafeA  94   
# 9   cafeB  97   
# 10  cafeC  94   
# 11  cafeD  88   

from statsmodels.stats.multicomp import pairwise_tukeyhsd

posthoc = pairwise_tukeyhsd(cafes_scores_df['score'], cafes_scores_df['group'], alpha=0.05)
print("posthoc",posthoc)

# ================================================================================
# posthoc Multiple Comparison of Means - Tukey HSD,FWER=0.05
# ==============================================
# group1 group2 meandiff  lower    upper  reject
# ----------------------------------------------
# cafeA  cafeB  -4.6667  -44.7251 35.3917 False 
# cafeA  cafeC  -19.6667 -59.7251 20.3917 False 
# cafeA  cafeD  -14.3333 -54.3917 25.7251 False 
# cafeB  cafeC   -15.0   -55.0584 25.0584 False 
# cafeB  cafeD  -9.6667  -49.7251 30.3917 False 
# cafeC  cafeD   5.3333  -34.7251 45.3917 False 
# ----------------------------------------------

# ================================================================================
fig = posthoc.plot_simultaneous()
plt.show()

