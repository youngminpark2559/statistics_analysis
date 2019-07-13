# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/003_Statistical_analysis/010_Attach && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns',None)
import numpy as np

# ================================================================================
game_df=pd.read_csv('./data/0301.game.csv',encoding='utf8')
# print("game_df",game_df)
#    id  sex  age  job  mrg  school  g_day  age_c  g_day_c   o1  o2  fb1  fb2  \
# 0  1   1    18   1    2    1       3      1      2        4    4   1    4     
# 1  2   2    23   5    2    3       3      2      2        3    3   5    2     
# 2  3   1    23   1    2    3       1      2      1        3    3   2    3     
# 3  4   2    20   1    2    2       3      1      2        4 4  2   3    4     
# 4  5   1    22   2    2    4       1      2      1        3    3   3    3     
# 5  6   1    24   2    2    4       2      2      1        4    4   2    2     
# 6  7   1    21   5    2    2       1      2      1        3    4   3    3     

#    fb3  if1  if2  if3  d1  d2  d3  d4  c1  c2  c3  c4  f1  f2  f3   f4  
# 0  5    1    2    2    4   5   1   5   4   5   5   4   5   4   2   5.0  
# 1  5    3    3    3    3   3   3   5   3   3   3   3   3   3   3   3.0  
# 2  4    4    2    4    3   4   3   2   2   3   3   4   4   4   2   3.0  
# 3  2    2    3    5    2   5   3   4   4   2   3   2   2   5   1  NaN   
# 4  3    2    2    2    3   3   3   3   2   3   2   2   3   4   3   2.0  
# 5  2    2    2    2    3   2   3   2   3   3   3   3   1   3   3   3.0  
# 6  3    3    3    4    4   3   3   2   3   4   4   4   4   4   3   3.0  

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
# print('np.unique(game_df["job"])',np.unique(game_df["job"]))
# [1 2 5]

jobs={1:"Student",2:"Worker",3:"Housewife",4:"Self-employment",5:"etc"}

uniq_job=np.unique(game_df["job"])
job_people={}
for one_job in uniq_job:
  num_of_people_in_job=(game_df["job"]==one_job).sum()
  job_people[one_job]=num_of_people_in_job

# print("job_people",job_people)
# {1: 3, 2: 2, 5: 2}

job_str_people={}

for k,v in job_people.items():
  indexed_job=jobs[k]
  job_str_people[indexed_job]=v
# print("job_str_people",job_str_people)
# {'Student': 3, 'Worker': 2, 'etc': 2}

# ================================================================================
job_str_people_keys=list(job_str_people.keys())
job_str_people_values=list(job_str_people.values())
# print("job_str_people_keys",job_str_people_keys)
# ['Student', 'Worker', 'etc']
# print("job_str_people_values",job_str_people_values)
# [3, 2, 2]

# ================================================================================
percent_Student=round(job_str_people_values[0]/np.array(job_str_people_values).sum(),3)
percent_Worker=round(job_str_people_values[1]/np.array(job_str_people_values).sum(),3)
percent_etc=round(job_str_people_values[2]/np.array(job_str_people_values).sum(),3)
# print("percent_Student",percent_Student)
# 0.429
# print("percent_Worker",percent_Worker)
# 0.286
# print("percent_etc",percent_etc)
# 0.286

# ================================================================================
d={'job_str':job_str_people_keys,
   'job_num_of_people':job_str_people_values,
   'percent':[percent_Student,percent_Worker,percent_etc]}
df=pd.DataFrame(d)
# print("df",df)
#    job_str  job_num_of_people  percent
# 0  Student                  3    0.429
# 1   Worker                  2    0.286
# 2      etc                  2    0.286

# ================================================================================
