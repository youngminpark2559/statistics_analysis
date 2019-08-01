# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/009_Analysis_of_variance/002_One_way_ANOVA && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np

# ================================================================================
# <./pics/2019_07_17_19:11:34.png>

# Null hypothesis: satisfactions are same on each store

# c x_bar_A: satisfaction mean on store A
# x_bar_A=x_bar_B=x_bar_C

# ================================================================================
# Research hypothesis: satisfactions are different on each store

# c x_bar_A: satisfaction mean on store A
# x_bar_A!=x_bar_B!=x_bar_C

# ================================================================================
# <./pics/2019_07_17_19:14:12.png>

scores_on_A=[1,4,3,3,3,3,3]
print(np.mean(scores_on_A))
# 2.857142857142857

# ================================================================================
scores_on_B=[4,4,3,4,4,5,4,4]
print(np.mean(scores_on_B))
# 4.0

# ================================================================================
scores_on_C=[4,3,4,3,4,4,3,3,3]
print(np.mean(scores_on_C))
# 3.4444444444444446

# ================================================================================
scores_on_entire=scores_on_A+scores_on_B+scores_on_C
# print(np.mean(scores_on_entire))
# 3.4583333333333335

# ================================================================================
# sum_of_squares_total
sst=np.power(scores_on_entire-np.mean(scores_on_entire),2)
sst=np.sum(sst)
# print("sst",sst)
# 13.958333333333334

# ================================================================================
# sum of squares between samples

ssb=\
len(scores_on_A)*np.power(np.mean(scores_on_A)-np.mean(scores_on_entire),2)+\
len(scores_on_B)*np.power(np.mean(scores_on_B)-np.mean(scores_on_entire),2)+\
len(scores_on_C)*np.power(np.mean(scores_on_C)-np.mean(scores_on_entire),2)
# print("ssb",ssb)
# 4.878968253968253

# ================================================================================
# sum of squares within samples

ssw_A=np.sum(np.power(scores_on_A-np.mean(scores_on_A),2))
ssw_B=np.sum(np.power(scores_on_B-np.mean(scores_on_B),2))
ssw_C=np.sum(np.power(scores_on_C-np.mean(scores_on_C),2))
ssw=ssw_A+ssw_B+ssw_C
# print("ssw",ssw)
# 9.079365079365077

# ================================================================================
# <./pics/2019_07_17_19:28:51.png>

# ================================================================================
# 편차의 평균=편차/자유도

# <./pics/2019_07_17_19:42:22.png>

# <./pics/2019_07_17_19:42:49.png>

# <./pics/2019_07_17_19:43:19.png>

# <./pics/2019_07_17_19:44:07.png>

# Lowest_satisfaction*5.664=Higest_satisfaction

# ================================================================================
# <./pics/2019_07_17_19:46:20.png>

# ================================================================================


