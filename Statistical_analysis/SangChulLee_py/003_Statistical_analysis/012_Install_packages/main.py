# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/003_Statistical_analysis/012_Install_packages && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns',None)
import numpy as np
from collections import Counter

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
man_df=game_df[game_df["sex"]==1]
# print("man_df",man_df)
#    id  sex  age  job  mrg  school  g_day  age_c  g_day_c  o1  o2  fb1  fb2  \
# 0  1   1    18   1    2    1       3      1      2        4   4   1    4     
# 2  3   1    23   1    2    3       1      2      1        3   3   2    3     
# 4  5   1    22   2    2    4       1      2      1        3   3   3    3     
# 5  6   1    24   2    2    4       2      2      1        4   4   2    2     
# 6  7   1    21   5    2    2       1      2      1        3   4   3    3     

#    fb3  if1  if2  if3  d1  d2  d3  d4  c1  c2  c3  c4  f1  f2  f3  f4  
# 0  5    1    2    2    4   5   1   5   4   5   5   4   5   4   2   5   
# 2  4    4    2    4    3   4   3   2   2   3   3   4   4   4   2   3   
# 4  3    2    2    2    3   3   3   3   2   3   2   2   3   4   3   2   
# 5  2    2    2    2    3   2   3   2   3   3   3   3   1   3   3   3   
# 6  3    3    3    4    4   3   3   2   3   4   4   4   4   4   3   3   

man_school=list(man_df["school"])
# print("man_school",man_school)
# [1, 3, 4, 4, 2]

man_school_cnt=Counter(man_school)
# print("man_school_cnt",man_school_cnt)
# Counter({4: 2, 1: 1, 3: 1, 2: 1})

man_school_cnt["University"] = man_school_cnt.pop(3)
man_school_cnt["High_school"] = man_school_cnt.pop(2)
man_school_cnt["Over_university"] = man_school_cnt.pop(4)
man_school_cnt["Under_high_school"] = man_school_cnt.pop(1)
# print("man_school_cnt",man_school_cnt)
# Counter({'Over_university': 2, 'University': 1, 'High_school': 1, 'Under_high_school': 1})

# ================================================================================
woman_df=game_df[game_df["sex"]==2]
# print("woman_df",woman_df)
#    id  sex  age  job  mrg  school  g_day  age_c  g_day_c  o1  o2  fb1  fb2  \
# 1  2   2    23   5    2    3       3      2      2        3   3   5    2     
# 3  4   2    20   1    2    2       3      1      2        4   4   2    3     

#    fb3  if1  if2  if3  d1  d2  d3  d4  c1  c2  c3  c4  f1  f2  f3  f4  
# 1  5    3    3    3    3   3   3   5   3   3   3   3   3   3   3   3   
# 3  4    2    2    3    5   2   5   3   4   4   2   3   2   2   5   1   

woman_school=list(woman_df["school"])
# print("woman_school",woman_school)
# [3, 2]

woman_school_cnt=Counter(woman_school)
# print("woman_school_cnt",woman_school_cnt)
# Counter({3: 1, 2: 1})

woman_school_cnt["University"] = woman_school_cnt.pop(3)
woman_school_cnt["High_school"] = woman_school_cnt.pop(2)
# print("woman_school_cnt",woman_school_cnt)
# Counter({'University': 1, 'High_school': 1})

# ================================================================================
