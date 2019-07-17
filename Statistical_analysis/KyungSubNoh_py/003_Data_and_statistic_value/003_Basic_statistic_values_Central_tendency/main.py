# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/003_Data_and_statistic_value/003_Basic_statistic_values_Central_tendency && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns',None)
import matplotlib.pyplot as plt
import numpy as np

# ================================================================================
# ./pics/2019_07_16_08:01:06.png

# ./pics/2019_07_16_08:01:57.png

# ================================================================================
# Central tendency values

# mean
# median
# mode (most frequent value)
# etc

# ================================================================================
# ./pics/2019_07_16_08:03:07.png

# ================================================================================
# ./pics/2019_07_16_08:04:15.png

# ================================================================================
# ./pics/2019_07_16_08:04:39.png

# ================================================================================
scores_in_class=[10,40,70,85,85,100]
num_of_students=len(scores_in_class)
score_of_student_A=70

# ================================================================================
# Calculate mean

summed_score=0
for one_score in scores_in_class:
  summed_score+=one_score
# print("summed_score",summed_score)
# 390

mean_score_value=summed_score/num_of_students
# print("mean_score_value",mean_score_value)
# 65.0

# print("Student A's score is higher than average score of the class?")
# print(score_of_student_A>mean_score_value)
# True

# ================================================================================
# Calculate median value

scores_in_class_for_sort=scores_in_class.copy()
scores_in_class_for_sort.sort()
# print("scores_in_class_for_sort",scores_in_class_for_sort)
# [10, 40, 70, 85, 85, 100]

scores_in_class_median=np.median(scores_in_class_for_sort)
# print("scores_in_class_median",scores_in_class_median)
# 77.5

# print("Student A's score is higher than median score of the class?")
# print(score_of_student_A>scores_in_class_median)
# False

# ================================================================================
# Calculate mode value 

def most_common(lst):
  return max(set(lst), key=lst.count)

most_frequent_value=most_common(scores_in_class)
# print("most_frequent_value",most_frequent_value)
# 85

# print("Student A's score is higher than most frequent score of the class?")
# print(score_of_student_A>most_frequent_value)
# False

# ================================================================================
# ./pics/2019_07_16_08:18:00.png

# dispersion (degree of scattering)

# ./pics/2019_07_16_08:19:08.png

# ================================================================================
# degree of scattering
# - Variance
# - etc

# ./pics/2019_07_16_08:20:06.png

# ================================================================================
# ./pics/2019_07_16_08:20:34.png

# ================================================================================
height_in_2_classes_df=pd.read_csv('./Data/001_height_in_2_classes.csv',encoding='utf8')
# print("height_in_2_classes_df",height_in_2_classes_df)
#    Id    A    B
# 0  1   168  175
# 1  2   160  179

# ================================================================================
def calculate_mean_and_variance(src_df,class_name):
  mean_val=round(src_df[class_name].mean(),1)
  variance_val=round(src_df[class_name].var(),1)
  return mean_val,variance_val

mean_val_A,variance_val_A=calculate_mean_and_variance(src_df=height_in_2_classes_df,class_name="A")
# print("mean_val_A",mean_val_A)
# 164.9
# print("variance_val_A",variance_val_A)
# 11.4

mean_val_B,variance_val_B=calculate_mean_and_variance(src_df=height_in_2_classes_df,class_name="B")
# print("mean_val_B",mean_val_B)
# 164.8
# print("variance_val_B",variance_val_B)
# 117.3

# ================================================================================
# Histogram

# ================================================================================
fig=plt.figure()

# ================================================================================
axes1=plt.subplot(1,2,1)

n,bins,patches=axes1.hist(height_in_2_classes_df["A"],bins=5)

plt.xlim(140,190)
plt.title("Height histogram of class A (small variance)")
plt.xlabel("Height values")
plt.ylabel("Number of students")

# ================================================================================
axes2=plt.subplot(1,2,2)

n,bins,patches=axes2.hist(height_in_2_classes_df["B"],bins=5)

plt.xlim(140,190)
plt.title("Height histogram of class B (large variance)")
plt.xlabel("Height values")
plt.ylabel("Number of students")

# ================================================================================
plt.subplots_adjust(wspace=None,hspace=0.3)
plt.tight_layout()
plt.show()
# ./pics/2019_07_16_08:33:30.png

# ================================================================================
# ./pics/2019_07_16_08:35:31.png

# Degree of freedom, DOF, df

# Why you use DOF?

# Calculate parameter of population is generally impossible

# In that situation, you calculate sample's parameters

# ./pics/2019_07_16_08:37:21.png

# Free components are only 2 out of 3 components
# because 1 component's freedom is confined by 2 components

# ./pics/2019_07_16_08:39:46.png

# ================================================================================
# Calculate "sample variance" (use DOF, n-1)

# ./pics/2019_07_16_08:38:50.png

# ================================================================================
# ./pics/2019_07_16_08:40:38.png

# Using "absolute value" for std is called "average standard deviation"
