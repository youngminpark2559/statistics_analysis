# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/003_Data_and_statistic_value/002_How_to_represent_data && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import pandas as pd
import matplotlib.pyplot as plt

# ================================================================================
# How to represent data
# - Table
#   - Frequency distribution table

# - Graph

# ================================================================================
weight_before_after_df=pd.read_csv('./Data/001_weight_before_after.csv',encoding='utf8')
# print("weight_before_after_df",weight_before_after_df)
#      id  before  after
# 0     1      75     73
# 1     2      74     74
# 2     3      75     76

# ================================================================================
min_weight_from_before=weight_before_after_df["before"].min()
# print("min_weight_from_before",min_weight_from_before)
# 54

max_weight_from_before=weight_before_after_df["before"].max()
# print("max_weight_from_before",max_weight_from_before)
# 83

min_weight_from_after=weight_before_after_df["after"].min()
# print("min_weight_from_after",min_weight_from_after)
# 50

max_weight_from_after=weight_before_after_df["after"].max()
# print("max_weight_from_after",max_weight_from_after)
# 76

# ================================================================================
def interval_weight_frequecy(src_df,time="before",min_weight=None,max_weight=None):

  if max_weight==None:
    before_class_under_50=src_df[src_df[time]<min_weight]
    # print("before_class_under_50",before_class_under_50)
    return before_class_under_50
  elif min_weight==None:
    pass
  else:
    before_class_50_55_1=src_df[time]<max_weight
    before_class_50_55_2=src_df[time]>=min_weight
    before_class_50_55_mask=before_class_50_55_1&before_class_50_55_2
    before_class_50_55=src_df[before_class_50_55_mask]
    # print("before_class_50_55",before_class_50_55)
    #     id  before  after
    # 17  18      54     50
    # 32  33      54     50
    # 47  48      54     50
    # 59  60      54     50
    # 69  70      54     50
    # 73  74      54     50
    # 86  87      54     50
    return before_class_50_55

# ================================================================================
weight_list=[[50,None],[50,55],[55,60],[60,65],[65,70],[70,75],[75,80],[80,85]]

# ================================================================================
for one_weight_interval in weight_list:
  # print("one_weight_interval",one_weight_interval)
  # [50, None]

  num_people=interval_weight_frequecy(src_df=weight_before_after_df,time="before",min_weight=one_weight_interval[0],max_weight=one_weight_interval[1])
  # print("num_people",num_people.shape[0])

# num_people 0
# num_people 7
# num_people 0
# num_people 6
# num_people 8
# num_people 22
# num_people 41
# num_people 16

# ================================================================================
for one_weight_interval in weight_list:
  # print("one_weight_interval",one_weight_interval)
  # [50, None]

  num_people=interval_weight_frequecy(src_df=weight_before_after_df,time="after",min_weight=one_weight_interval[0],max_weight=one_weight_interval[1])
  # print("num_people",num_people.shape[0])

# num_people 0
# num_people 7
# num_people 0
# num_people 6
# num_people 26
# num_people 39
# num_people 22
# num_people 0

# ================================================================================
# ./pics/2019_07_16_07:44:32.png

# ================================================================================
fig=plt.figure()

# ================================================================================
axes1=plt.subplot(1,2,1)

n,bins,patches=axes1.hist(weight_before_after_df["before"],bins=5)

plt.xlim(45,85)
plt.title("Weight histogram before taking drug")
plt.xlabel("Weight values")
plt.ylabel("Number of people")

# ================================================================================
axes2=plt.subplot(1,2,2)

n,bins,patches=axes2.hist(weight_before_after_df["after"],bins=5)

plt.xlim(45,85)
plt.title("Weight histogram after taking drug")
plt.xlabel("Weight values")
plt.ylabel("Number of people")

# ================================================================================
plt.subplots_adjust(wspace=None,hspace=0.3)
plt.tight_layout()
plt.show()
# ./pics/2019_07_16_07:56:09.png

# ================================================================================
