# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/003_Statistical_analysis/011_Contingency_table && \
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
# print('np.unique(game_df["school"])',np.unique(game_df["school"]))
# [1 2 3 4]

# ================================================================================
schools={1:"Under_high_school",2:"High_school",3:"Univ",4:"Over_unive"}

uniq_school=np.unique(game_df["school"])
school_people={}
for one_school in uniq_school:
  num_of_people_in_school=(game_df["school"]==one_school).sum()
  school_people[one_school]=num_of_people_in_school

# print("school_people",school_people)
# {1: 1, 2: 2, 3: 2, 4: 2}

# ================================================================================
school_str_people={}

for k,v in school_people.items():
  indexed_job=schools[k]
  school_str_people[indexed_job]=v
# print("school_str_people",school_str_people)
# {'Student': 3, 'Worker': 2, 'etc': 2}

# ================================================================================
school_str_people_keys=list(school_str_people.keys())
school_str_people_values=list(school_str_people.values())
# print("school_str_people_keys",school_str_people_keys)
# ['Student', 'Worker', 'etc']
# print("school_str_people_values",school_str_people_values)
# [3, 2, 2]

# ================================================================================
percent_Student=round(school_str_people_values[0]/np.array(school_str_people_values).sum(),3)
percent_Worker=round(school_str_people_values[1]/np.array(school_str_people_values).sum(),3)
percent_etc=round(school_str_people_values[2]/np.array(school_str_people_values).sum(),3)
percent_etc2=round(school_str_people_values[2]/np.array(school_str_people_values).sum(),3)
# print("percent_Student",percent_Student)
# 0.429
# print("percent_Worker",percent_Worker)
# 0.286
# print("percent_etc",percent_etc)
# 0.286

# ================================================================================
d={'school_str':school_str_people_keys,
   'school_num_of_people':school_str_people_values,
   'percent':[percent_Student,percent_Worker,percent_etc,percent_etc2]}
df=pd.DataFrame(d)
# print("df",df)
#           school_str  school_num_of_people  percent
# 0  Under_high_school  1                     0.143  
# 1  High_school        2                     0.286  
# 2  Univ               2                     0.286  
# 3  Over_unive         2                     0.286  









# ================================================================================
men_data=game_df[game_df["sex"]==1]
# print("men_data",men_data)
#    id  sex  age  job  mrg  school  g_day  age_c  g_day_c o1  o2  fb1  fb2  \
# 0  1   1    18   1    2    1       3      1      2        4  4   1    4     
# 2  3   1    23   1    2    3       1      2      1        3  3   2    3     
# 4  5   1    22   2    2    4       1      2      1        3  3   3    3     
# 5  6   1    24   2    2    4       2      2      1        4  4   2    2     
# 6  7   1    21   5    2    2       1      2      1        3  4   3    3     

#    fb3  if1  if2  if3  d1  d2  d3  d4  c1  c2  c3  c4  f1  f2  f3   f4  
# 0  5    1    2    2    4   5   1   5   4   5   5   4   5   4   2   5.0  
# 2  4    4    2    4    3   4   3   2   2   3   3   4   4   4   2   3.0  
# 4  3    2    2    2    3   3   3   3   2   3   2   2   3   4   3   2.0  
# 5  2    2    2    2    3   2   3   2   3   3   3   3   1   3   3   3.0  
# 6  3    3    3    4    4   3   3   2   3   4   4   4   4   4   3   3.0  

women_data=game_df[game_df["sex"]==2]
# print("women_data",women_data)
#    id  sex  age  job  mrg  school  g_day  age_c  g_day_c   o1  o2  fb1  fb2  \
# 1  2   2    23   5    2    3       3      2      2        3    3   5    2     
# 3  4   2    20   1    2    2       3      1      2        4 4  2   3    4     

#    fb3  if1  if2  if3  d1  d2  d3  d4  c1  c2  c3  c4  f1  f2  f3   f4  
# 1  5    3    3    3    3   3   3   5   3   3   3   3   3   3   3   3.0  
# 3  2    2    3    5    2   5   3   4   4   2   3   2   2   5   1  NaN   

# ================================================================================
def process_with_school(game_df):
  schools={1:"Under_high_school",2:"High_school",3:"Univ",4:"Over_unive"}

  uniq_school=np.unique(game_df["school"])
  school_people={}
  for one_school in uniq_school:
    num_of_people_in_school=(game_df["school"]==one_school).sum()
    school_people[one_school]=num_of_people_in_school

  # print("school_people",school_people)
  # {1: 1, 2: 1, 3: 1, 4: 2}

  # ================================================================================
  school_str_people={}

  for k,v in school_people.items():
    indexed_job=schools[k]
    school_str_people[indexed_job]=v
  # print("school_str_people",school_str_people)
  # {'Under_high_school': 1, 'High_school': 1, 'Univ': 1, 'Over_unive': 2}

  # ================================================================================
  school_str_people_keys=list(school_str_people.keys())
  school_str_people_values=list(school_str_people.values())
  school_key_val=list(zip(school_str_people_keys,school_str_people_values))

  school_str_people_values_np=np.array(list(school_str_people.values()))
  # print("school_str_people_keys",school_str_people_keys)
  # ['Under_high_school', 'High_school', 'Univ', 'Over_unive']
  # print("school_str_people_values",school_str_people_values)
  # [1 1 1 2]

  # ================================================================================
  # print("school_str_people_values.shape",school_str_people_values.shape)
  # (4,)

  school_str_people_percent={}
  for k,v in school_key_val:
    percent_Student=round(v/school_str_people_values_np.sum(),3)
    # print("percent_Student",percent_Student)
    # 0.2

    school_str_people_percent[k]=percent_Student
    
  # print("school_str_people_percent",school_str_people_percent)
  # {'Under_high_school': 0.2, 'High_school': 0.2, 'Univ': 0.2, 'Over_unive': 0.4}

  # ================================================================================
  d={'school_str':school_str_people_keys,
    'school_num_of_people':school_str_people_values,
    'percent':[percent_Student,percent_Worker,percent_etc,percent_etc2]}
  df=pd.DataFrame(d)
  # print("df",df)
  #           school_str  school_num_of_people  percent
  # 0  Under_high_school  1                     0.143  
  # 1  High_school        2                     0.286  
  # 2  Univ               2                     0.286  
  # 3  Over_unive         2                     0.286  

# ================================================================================
process_with_school(men_data)
process_with_school(women_data)
afaf