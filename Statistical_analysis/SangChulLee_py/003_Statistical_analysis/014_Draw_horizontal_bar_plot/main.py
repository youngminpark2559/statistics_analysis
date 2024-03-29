# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/003_Statistical_analysis/014_Draw_horizontal_bar_plot && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns',None)
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

# ================================================================================
game_df=pd.read_csv('./data/0301.game.csv',encoding='utf8')
# print("game_df",game_df)
#    id  sex  age  job  mrg  school  g_day  age_c  g_day_c  o1  o2  fb1  fb2  \
# 0  1   1    18   1    2    1       3      1      2        4   4   1    4     
# 1  2   2    23   5    2    3       3      2      2        3   3   5    2     
# 2  3   1    23   1    2    3       1      2      1        3   3   2    3     
# 3  4   2    20   1    2    2       3      1      2        4   4   2    3     
# 4  5   1    22   2    2    4       1      2      1        3   3   3    3     
# 5  6   1    24   2    2    4       2      2      1        4   4   2    2     
# 6  7   1    21   5    2    2       1      2      1        3   4   3    3     

#    fb3  if1  if2  if3  d1  d2  d3  d4  c1  c2  c3  c4  f1  f2  f3  f4  
# 0  5    1    2    2    4   5   1   5   4   5   5   4   5   4   2   5   
# 1  5    3    3    3    3   3   3   5   3   3   3   3   3   3   3   3   
# 2  4    4    2    4    3   4   3   2   2   3   3   4   4   4   2   3   
# 3  4    2    2    3    5   2   5   3   4   4   2   3   2   2   5   1   
# 4  3    2    2    2    3   3   3   3   2   3   2   2   3   4   3   2   
# 5  2    2    2    2    3   2   3   2   3   3   3   3   1   3   3   3   
# 6  3    3    3    4    4   3   3   2   3   4   4   4   4   4   3   3   

# ================================================================================
school_num_sr=game_df.groupby('school').size()
# print("school_num_sr",school_num_sr)
# school
# 1    1
# 2    2
# 3    2
# 4    2

# ================================================================================
school_num_sr.index=["Under_high_school","High_school","University","Over_university"]
# print(school_num_sr)
# Under_high_school    1
# High_school          2
# University           2
# Over_university      2
# dtype: int64

# ================================================================================
index_li=list(school_num_sr.index)
# print("index_li",index_li)
# ['Under_high_school', 'High_school', 'University', 'Over_university']

num_people_il=list(school_num_sr)
# print("num_people_il",num_people_il)
# [1, 2, 2, 2]

# ================================================================================
fig,ax0=plt.subplots(figsize=(15,5))
ax0.barh(y=index_li[0], width=num_people_il[0],label="Under_high_school")
ax0.barh(y=index_li[1], width=num_people_il[1],label="High_school")
ax0.barh(y=index_li[2], width=num_people_il[1],label="University")
ax0.barh(y=index_li[3], width=num_people_il[1],label="Over_university")
ax0.legend()
plt.title("School distribution of responders")
plt.xlabel("School")
plt.ylabel("Number of responders")
plt.show()
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/003_Statistical_analysis/014_Draw_horizontal_bar_plot/pics/2019_07_13_13:50:42.png

# ================================================================================
