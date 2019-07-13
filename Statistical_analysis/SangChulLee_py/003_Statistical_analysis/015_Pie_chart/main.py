# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/003_Statistical_analysis/015_Pie_chart && \
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
job_num_sr=game_df.groupby('job').size()
# print("job_num_sr",job_num_sr)
# job_num_sr job
# 1    3
# 2    2
# 5    2

# ================================================================================
job_num_sr.index=["Student","Housewife","Worker"]
# print(job_num_sr)
# Student      3
# Housewife    2
# Worker       2

# ================================================================================
index_li=list(job_num_sr.index)
# print("index_li",index_li)
# ['Student', 'Housewife', 'Worker']

num_people_il=list(job_num_sr)
# print("num_people_il",num_people_il)
# [3, 2, 2]

# ================================================================================
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

fig,ax0=plt.subplots(figsize=(10,10))
# ax0.pie(num_people_il,labels=index_li,shadow=False,startangle=90,autopct='%.2f')
ax0.pie(num_people_il,labels=index_li,shadow=False,startangle=90,autopct=make_autopct(num_people_il))
ax0.legend()
plt.title("Job distribution of responders")
plt.show()
# /home/young/Pictures/2019_07_13_14:08:28.png

# ================================================================================
