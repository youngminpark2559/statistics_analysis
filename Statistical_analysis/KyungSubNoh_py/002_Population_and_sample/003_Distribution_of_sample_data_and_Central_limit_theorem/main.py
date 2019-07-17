# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/002_Population_and_sample/003_Distribution_of_sample_data_and_Central_limit_theorem && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import random
import itertools
import numpy as np
import matplotlib.pyplot as plt

# ================================================================================
# <./pics/2019_07_15_21:11:19.png>

# <./pics/2019_07_15_21:11:53.png>

# ================================================================================
def extract_sample_data(src_data,num_of_element):
  l=src_data
  comb = []
  for i in range(len(l)):
    element=list(itertools.combinations(l,i+1))
    # print("element",element)

    if len(element[0])==num_of_element:
      comb.append(element)
    else:
      pass
  return comb

# ================================================================================
def calculate_min_max_vals(src_data,min=False):
  # print("src_data",src_data)
  # [31.0, 43.0, 35.0, 46.5, 37.0, 29.0, 40.5, 41.0, 52.5, 44.5]

  if min==True:
    argmin_val=np.argmin(np.array(src_data))
    # print("argmin_val",argmin_val)
    # 5
    min_val=src_data[argmin_val]
    # print("min_val",min_val)
    return argmin_val,min_val
  
  elif min==False:
    argmax_val=np.argmax(np.array(src_data))
    # print("argmax_val",argmax_val)
    # 5
    max_val=src_data[argmax_val]
    # print("min_val",min_val)
    return argmax_val,max_val

# ================================================================================
time_for_going_to_school=[37,25,49,33,56]

comb_2=extract_sample_data(src_data=time_for_going_to_school,num_of_element=2)
# print("comb_2",comb_2)
# [[(37, 25), (37, 49), (37, 33), (37, 56), (25, 49), (25, 33), (25, 56), (49, 33), (49, 56), (33, 56)]]
# print("comb_2",len(comb_2[0]))
# 10 = 5C2

comb_3=extract_sample_data(src_data=time_for_going_to_school,num_of_element=3)
# print("comb_3",comb_3)
# [[(37, 25, 49), (37, 25, 33), (37, 25, 56), (37, 49, 33), (37, 49, 56), (37, 33, 56), (25, 49, 33), (25, 49, 56), (25, 33, 56), (49, 33, 56)]]
# print("comb_3",len(comb_3[0]))
# 10 = 5C3

# ================================================================================
# <./pics/2019_07_15_21:28:03.png>

def calculate_sample_data_mean_value(sample_data):
  sample_data_mean_vals=[]
  for one_sample_data in sample_data[0]:
    # print("one_sample_data",one_sample_data)
    # (37, 25)

    sum_val=np.array(one_sample_data).sum()
    # print("sum_val",sum_val)
    # 62

    avg_val=sum_val/len(one_sample_data)
    # print("avg_val",avg_val)
    # 31.0

    sample_data_mean_vals.append(round(avg_val,1))
  
  # print("sample_data_mean_vals",sample_data_mean_vals)
  
  return sample_data_mean_vals

sample_data_mean_vals_comb_2=calculate_sample_data_mean_value(sample_data=comb_2)
sample_data_mean_vals_comb_3=calculate_sample_data_mean_value(sample_data=comb_3)

# print("sample_data_mean_vals_comb_2",sample_data_mean_vals_comb_2)
# [31.0, 43.0, 35.0, 46.5, 37.0, 29.0, 40.5, 41.0, 52.5, 44.5]

# print("sample_data_mean_vals_comb_3",sample_data_mean_vals_comb_3)
# [37.0, 31.7, 39.3, 39.7, 47.3, 42.0, 35.7, 43.3, 38.0, 46.0]

# ================================================================================
# <./pics/2019_07_15_21:34:56.png>

# ================================================================================
fig=plt.figure()

axe1=plt.subplot(1,2,1)

axe1.plot(sample_data_mean_vals_comb_2)

min_val=calculate_min_max_vals(sample_data_mean_vals_comb_2,min=True)
# print("min_val",min_val)
# (1, 43.0)
plt.plot(min_val[0],min_val[1],'ro')
max_val=calculate_min_max_vals(sample_data_mean_vals_comb_2,min=False)
# print("max_val",max_val)
# (4, 37.0)
plt.plot(max_val[0],max_val[1],'ro')
plt.title("Distribution of 2 element sample data's mean values")
plt.xlabel("Sample data point's index")
plt.ylabel("Time")
plt.xlim(0,10)
plt.ylim(0,60)

# ================================================================================
axe1=plt.subplot(1,2,2)

# print("sample_data_mean_vals_comb_3",sample_data_mean_vals_comb_3)
axe1.plot(sample_data_mean_vals_comb_3)

min_val=calculate_min_max_vals(sample_data_mean_vals_comb_3,min=True)
# print("min_val",min_val)
# (1, 43.0)
plt.plot(min_val[0],min_val[1],'ro')
max_val=calculate_min_max_vals(sample_data_mean_vals_comb_3,min=False)
# print("max_val",max_val)
# (4, 37.0)

plt.plot(max_val[0],max_val[1],'ro')
plt.xlabel("Sample data point's index")
plt.ylabel("Time")
plt.xlim(0,10)
plt.ylim(0,60)

plt.title("Distribution of 3 element sample data's mean values")

# ================================================================================
plt.show()
# <./pics/2019_07_16_06:25:37.png>

# ================================================================================
# <./pics/2019_07_16_06:26:11.png>
