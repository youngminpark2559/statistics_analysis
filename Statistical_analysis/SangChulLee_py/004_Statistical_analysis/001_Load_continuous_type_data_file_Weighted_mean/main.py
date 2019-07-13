# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/004_Statistical_analysis/001_Load_continuous_type_data_file && \
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
wgt_df=pd.read_csv('./Data/0401.wgt.csv',encoding='utf8')
# print("wgt_df",wgt_df)
#    id  weight  sex
# 0  1   40      2  
# 1  2   50      2  
# 2  3   56      1  
# 3  4   51      2  
# 4  5   55      1  
# 5  6   61      1  
# 6  7   70      1  
# 7  8   44      2  
# 8  9   66      1  
# 9  10  60      1  

# ================================================================================
wgt_sex_sr=wgt_df["sex"]

wgt_sex_sr[wgt_sex_sr==1]="Man"
wgt_sex_sr[wgt_sex_sr==2]="Woman"
# print("wgt_df",wgt_df)
#    id  weight    sex
# 0  1   40      Woman
# 1  2   50      Woman
# 2  3   56      Man  
# 3  4   51      Woman
# 4  5   55      Man  
# 5  6   61      Man  
# 6  7   70      Man  
# 7  8   44      Woman
# 8  9   66      Man  
# 9  10  60      Man  

# ================================================================================
# /home/young/Pictures/2019_07_13_14:42:57.png

# ================================================================================
# /home/young/Pictures/2019_07_13_14:43:14.png

# If even numbers, sum(center1,center2)/2

# ================================================================================
# /home/young/Pictures/2019_07_13_14:44:11.png

# ================================================================================
mean_of_weight=wgt_df["weight"].mean()
# print("mean_of_weight",mean_of_weight)
# 55.3

mean_of_weight=wgt_df["weight"].median()
# print("mean_of_weight",mean_of_weight)
# 55.0

# ================================================================================
# Weighted mean tutorial

classroom=["A","B","C"]
num_of_student=[10,50,40]
average_score_of_classroom=[60,70,80]

sum_of_all_students=np.array(num_of_student).sum()
# print("sum_of_all_students",sum_of_all_students)
# 100

# ================================================================================
upper_term=0

for num_of_student,average_score in list(zip(num_of_student,average_score_of_classroom)):
  multipled=num_of_student*average_score
  # print("multipled",multipled)
  # 600
  upper_term+=multipled

weighted_avg=upper_term/sum_of_all_students
# print("weighted_avg",weighted_avg)
# 73.0

# ================================================================================
# Vanila average

vanila_average=np.array(average_score_of_classroom).sum()/len(average_score_of_classroom)
# print("vanila_average",vanila_average)
# 70.0

# ================================================================================
is_weighted_avg_greater_than_vanila_average=weighted_avg>vanila_average
# print("is_weighted_avg_greater_than_vanila_average",is_weighted_avg_greater_than_vanila_average)
# True

# ================================================================================
