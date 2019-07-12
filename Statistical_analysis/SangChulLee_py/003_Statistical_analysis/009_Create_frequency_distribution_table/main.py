# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/003_Statistical_analysis/009_Create_frequency_distribution_table && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import pandas as pd
import numpy as np

# ================================================================================
game_df=pd.read_csv('./data/0301.game.csv',encoding='utf8')
# print("game_df",game_df)
#    id  sex  age  job  mrg  school  g_day ...   c2  c3 c4  f1  f2  f3   f4
# 0   1    1   18    1    2       1      3 ...    5   5  4   5   4   2  5.0
# 1   2    2   23    5    2       3      3 ...    3   3  3   3   3   3  3.0
# 2   3    1   23    1    2       3      1 ...    3   3  4   4   4   2  3.0
# 3   4    2   20    1    2       2      3 ...    2   3  2   2   5   1  NaN
# 4   5    1   22    2    2       4      1 ...    3   2  2   3   4   3  2.0
# 5   6    1   24    2    2       4      2 ...    3   3  3   1   3   3  3.0
# 6   7    1   21    5    2       2      1 ...    4   4  4   4   4   3  3.0

# ================================================================================
num_of_men=(game_df["sex"]==1).sum()
num_of_women=(game_df["sex"]==2).sum()
n_sex={"Man":num_of_men,"Woman":num_of_women}
# print("n_sex",n_sex)
# {'Man': 5, 'Woman': 2}

# ================================================================================
men_percent=round(num_of_men/(num_of_men+num_of_women),3)
women_percent=round(num_of_women/(num_of_men+num_of_women),3)
# print("men_percent",men_percent)
# print("women_percent",women_percent)
# 0.714
# 0.286

# ================================================================================
d={'sex':["Man","Woman","Entire"],
   'frequency':[num_of_men,num_of_women,num_of_men+num_of_women],
   'percent':[men_percent,women_percent,men_percent+women_percent]}

# c freq_dist_table: frequency distribution table
freq_dist_table_df=pd.DataFrame(d)
# print("freq_dist_table_df",freq_dist_table_df)
#       sex  frequency  percent
# 0     Man          5    0.714
# 1   Woman          2    0.286
# 2  Entire          7    1.000

# ================================================================================
