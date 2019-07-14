# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/008_ANOVA/005_006_One_way_ANOVA_Repeated_measure_ANOVA && \
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
import scipy as sp
# ================================================================================
# - on same experimental unit
# - multiple measurements

# ================================================================================
# 6 months language course

# you need to measure the effectiveness of that language course

# Extract students

# Test English skill at before course, at after 3 months, at after 6 months

# That language course is really effective?

# If so, when does that effectiveness start?

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/005_006_One_way_ANOVA_Repeated_measure_ANOVA/pics/2019_07_14_20:17:41.png

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/005_006_One_way_ANOVA_Repeated_measure_ANOVA/pics/2019_07_14_20:18:08.png

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/005_006_One_way_ANOVA_Repeated_measure_ANOVA/pics/2019_07_14_20:18:24.png

# One way ANOVA separates "equal variance between groups" and "unequal variance between groups"

# ================================================================================
# Repeated measures ANOVA

# If you measure 3 times, 3 measurements should have same "error", which is called sphericity

# If sphericity is proved, you can use general repeated measures ANOVA
# Otherwise, you first need to perform "error fix" by using Greenhouse-Geisser, Huynh and Feldt fixing coefficient

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/005_006_One_way_ANOVA_Repeated_measure_ANOVA/pics/2019_07_14_20:24:06.png

# ================================================================================
time_score_df=pd.read_csv('./Data/05.RMA.csv',encoding='utf8')
# print("time_score_df",time_score_df)
#     id  time  score
# 0   1   1     64   
# 1   2   1     60   
# 2   3   1     57   
# 3   4   1     58   
# 4   5   1     77   
# 5   6   2     63   
# 6   7   2     74   
# 7   8   2     66   
# 8   9   2     86   
# 9   10  2     65   
# 10  11  3     87   
# 11  12  3     86   
# 12  13  3     98   
# 13  14  3     67   
# 14  15  3     81   

# ================================================================================
time_df=time_score_df["time"]
time_df[time_df==1]="pre"
time_df[time_df==2]="3month"
time_df[time_df==3]="6month"

# print("time_score_df",time_score_df)
#     id    time  score
# 0   1   pre     64   
# 1   2   pre     60   
# 2   3   pre     57   
# 3   4   pre     58   
# 4   5   pre     77   
# 5   6   3month  63   
# 6   7   3month  74   
# 7   8   3month  66   
# 8   9   3month  86   
# 9   10  3month  65   
# 10  11  6month  87   
# 11  12  6month  86   
# 12  13  6month  98   
# 13  14  6month  67   
# 14  15  6month  81   

# ================================================================================
pre_sr=time_score_df[time_score_df["time"]=="pre"]
three_month_sr=time_score_df[time_score_df["time"]=="3month"]
six_month_sr=time_score_df[time_score_df["time"]=="6month"]

fig0,axes0=plt.subplots()

axes0.boxplot([pre_sr["score"],three_month_sr["score"],six_month_sr["score"]],sym="bo")

plt.title("Box plot of time-score data")
plt.xlabel("Time")
plt.ylabel("Score")
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/005_006_One_way_ANOVA_Repeated_measure_ANOVA/pics/2019_07_14_20:45:00.png

# ================================================================================
x1=pre_sr['score']
# print("x1",x1)

x2=three_month_sr['score']
# print("x2",x2)

x3=six_month_sr['score']
# print("x3",x3)

F_statistic,pVal=sp.stats.f_oneway(x1,x2,x3)
# print("F_statistic",F_statistic)
# F_statistic 5.7499116919816275

# print("pVal",pVal)
# pVal 0.017729638743387958

# ================================================================================
if pVal < 0.05:
  print("pVal is enough small")
  print("It means there is mean-differences between groups")
else:
  print("pVal is not enough small")
  print("It means there is no mean-differences between groups")
# pVal is enough small
# It means there is mean-differences between groups

# ================================================================================
from statsmodels.stats.multicomp import pairwise_tukeyhsd

posthoc = pairwise_tukeyhsd(time_score_df['score'], time_score_df['time'], alpha=0.05)
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
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/005_006_One_way_ANOVA_Repeated_measure_ANOVA/pics/2019_07_14_20:55:13.png

# ================================================================================
