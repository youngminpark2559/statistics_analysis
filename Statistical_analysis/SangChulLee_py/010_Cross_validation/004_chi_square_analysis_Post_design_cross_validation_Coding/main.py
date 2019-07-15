# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/010_Cross_validation/004_chi_square_analysis_Post_design_cross_validation_Coding && \
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
import random
import scipy as sp
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt
import pandas

# ================================================================================
def get_num_people(src_df,column,column_data):
  num_of_people=(src_df[column]==column_data).sum()
  return num_of_people

# ================================================================================
smoke_cancer_df=pd.read_csv('./Data/13.PostCRO.csv',encoding='utf8')
# print("smoke_cancer_df",smoke_cancer_df)
#    smoking  lung  count
# 0  1        1     73   
# 1  1        2     18   
# 2  2        1     141  
# 3  2        2     196  

# ================================================================================
# group_sr=vitamin_plac_cold_df["group"]

# group_sr[group_sr==1]="Vitamin"
# group_sr[group_sr==2]="Placebo"

# # print("vitamin_plac_cold_df",vitamin_plac_cold_df)
# #       group  cold
# # 0   Vitamin  1   
# # 1   Vitamin  1   
# # 2   Vitamin  1   
# # 3   Vitamin  1   
# # 4   Vitamin  1   
# # 5   Vitamin  1   
# # 6   Vitamin  2   
# # 7   Vitamin  2   
# # 8   Vitamin  2   
# # 9   Vitamin  2   
# # 10  Placebo  1   
# # 11  Placebo  1   
# # 12  Placebo  1   
# # 13  Placebo  1   
# # 14  Placebo  2   
# # 15  Placebo  2   
# # 16  Placebo  2   
# # 17  Placebo  2   
# # 18  Placebo  2   
# # 19  Placebo  2   

# # ================================================================================
# cold_sr=vitamin_plac_cold_df["cold"]

# cold_sr[cold_sr==1]="No_cold"
# cold_sr[cold_sr==2]="Cold"

# # print("vitamin_plac_cold_df",vitamin_plac_cold_df)
# #       group     cold
# # 0   Vitamin  No_cold
# # 1   Vitamin  No_cold
# # 2   Vitamin  No_cold
# # 3   Vitamin  No_cold
# # 4   Vitamin  No_cold
# # 5   Vitamin  No_cold
# # 6   Vitamin  Cold   
# # 7   Vitamin  Cold   
# # 8   Vitamin  Cold   
# # 9   Vitamin  Cold   
# # 10  Placebo  No_cold
# # 11  Placebo  No_cold
# # 12  Placebo  No_cold
# # 13  Placebo  No_cold
# # 14  Placebo  Cold   
# # 15  Placebo  Cold   
# # 16  Placebo  Cold   
# # 17  Placebo  Cold   
# # 18  Placebo  Cold   
# # 19  Placebo  Cold   

# # ================================================================================
# vita_grp=vitamin_plac_cold_df[vitamin_plac_cold_df["group"]=="Vitamin"]
# # print("vita_grp",vita_grp)
# #      group     cold
# # 0  Vitamin  No_cold
# # 1  Vitamin  No_cold
# # 2  Vitamin  No_cold
# # 3  Vitamin  No_cold
# # 4  Vitamin  No_cold
# # 5  Vitamin  No_cold
# # 6  Vitamin  Cold   
# # 7  Vitamin  Cold   
# # 8  Vitamin  Cold   
# # 9  Vitamin  Cold   

# vita_no_cold_num=get_num_people(src_df=vita_grp,column="cold",column_data="No_cold")
# # print("vita_no_cold_num",vita_no_cold_num)
# # 6

# vita_cold_num=get_num_people(src_df=vita_grp,column="cold",column_data="Cold")
# # print("vita_cold_num",vita_cold_num)
# # 4

# # ================================================================================
# plac_grp=vitamin_plac_cold_df[vitamin_plac_cold_df["group"]=="Placebo"]
# # print("plac_grp",plac_grp)
# #       group     cold
# # 10  Placebo  No_cold
# # 11  Placebo  No_cold
# # 12  Placebo  No_cold
# # 13  Placebo  No_cold
# # 14  Placebo  Cold   
# # 15  Placebo  Cold   
# # 16  Placebo  Cold   
# # 17  Placebo  Cold   
# # 18  Placebo  Cold   
# # 19  Placebo  Cold   

# plac_no_cold_num=get_num_people(src_df=plac_grp,column="cold",column_data="No_cold")
# # print("plac_no_cold_num",plac_no_cold_num)
# # 4

# plac_cold_num=get_num_people(src_df=plac_grp,column="cold",column_data="Cold")
# # print("plac_cold_num",plac_cold_num)
# # 6

# # ================================================================================
# group_data=["Vitamin","Placebo"]
# no_cold_data=[vita_no_cold_num,plac_no_cold_num]
# cold_data=[vita_cold_num,plac_cold_num]

# d={'Group':group_data,
#    'No_cold':no_cold_data,
#    'Cold':cold_data}
# df=pd.DataFrame(d)
# # print("df",df)
# #      Group  No_cold  Cold
# # 0  Vitamin  7        3   
# # 1  Placebo  4        6   

# # ================================================================================
# num_of_people_taking_vitamin=np.array(list(df.iloc[0,:])[1:]).sum()
# # print("num_of_people_taking_vitamin",num_of_people_taking_vitamin)
# # 10

# num_of_people_taking_placebo=np.array(list(df.iloc[1,:])[1:]).sum()
# # print("num_of_people_taking_placebo",num_of_people_taking_placebo)
# # 10

# num_of_people_no_cold=np.array(list(df.iloc[:,1])).sum()
# # print("num_of_people_no_cold",num_of_people_no_cold)
# # 11

# num_of_people_cold=np.array(list(df.iloc[:,2])).sum()
# # print("num_of_people_cold",num_of_people_cold)
# # 9

# # ================================================================================
# # H_0: vitamin and cold have no relationship
# # $$$H_0:\pi_1=\pi_2$$$

# # You will get p value
# # If p>0.05, H_0 is adopted

# # ================================================================================
# no_cold_data=vitamin_plac_cold_df[vitamin_plac_cold_df["cold"]=="No_cold"]
# # print("no_cold_data",no_cold_data)
# #       group     cold
# # 0   Vitamin  No_cold
# # 1   Vitamin  No_cold
# # 2   Vitamin  No_cold
# # 3   Vitamin  No_cold
# # 4   Vitamin  No_cold
# # 5   Vitamin  No_cold
# # 6   Vitamin  No_cold
# # 10  Placebo  No_cold
# # 11  Placebo  No_cold
# # 12  Placebo  No_cold
# # 13  Placebo  No_cold

# num_no_cold_vita=(no_cold_data["group"]=="Vitamin").sum()
# # print("num_no_cold_vita",num_no_cold_vita)
# # 7
# num_no_cold_plac=(no_cold_data["group"]=="Placebo").sum()
# # print("num_no_cold_plac",num_no_cold_plac)
# # 4

# cold_data=vitamin_plac_cold_df[vitamin_plac_cold_df["cold"]=="Cold"]
# num_cold_vita=(cold_data["group"]=="Vitamin").sum()
# # print("num_cold_vita",num_cold_vita)
# # 3
# num_cold_plac=(cold_data["group"]=="Placebo").sum()
# # print("num_cold_plac",num_cold_plac)
# # 6

# # ================================================================================
# # Bar plot

# x_data=["Vitamin","Placebe"]
# y1_data=[num_no_cold_vita,num_no_cold_plac]
# y2_data=[num_cold_vita,num_cold_plac]

# fig = plt.figure()

# ax0=fig.add_subplot(1,2,1)
# ax0.bar(x=x_data[0], height=y1_data[0],label="Vitamin")
# ax0.bar(x=x_data[1], height=y1_data[1],label="Placebo")

# plt.legend()
# plt.title("No_cold case")
# plt.xlabel("Vitamin or Placebo")
# plt.ylabel("Number of no_cold people")

# # ================================================================================
# ax1=fig.add_subplot(1,2,2)

# ax1.bar(x=x_data[0], height=y2_data[0],label="Vitamin")
# ax1.bar(x=x_data[1], height=y2_data[1],label="Placebo")

# plt.legend()
# plt.title("Cold case")
# plt.xlabel("Vitamin or Placebo")
# plt.ylabel("Number of cold people")

# plt.show()
# # https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/010_Cross_validation/003_chi_square_analysis_Pre_design_cross_validation_Coding/pics/2019_07_15_11:22:09.png

# # ================================================================================
# # mosaic plot

# # vitamin=[num_no_cold_vita,num_cold_vita]
# # placebo=[num_no_cold_plac,num_cold_plac]

# # d_for_mosaic={
# #   'vitamin':vitamin,
# #   'placebo':placebo}
# # # df_for_mosaic=pd.DataFrame(d)
# # # print("df_for_mosaic",df_for_mosaic)
# # #      Group  No_cold  Cold
# # # 0  Vitamin  7        3   
# # # 1  Placebo  4        6   

# # vitamin_plac_cold_df
# # print("vitamin_plac_cold_df",vitamin_plac_cold_df)
# # afaf

# mosaic(vitamin_plac_cold_df,['group','cold'])
# plt.show()
# # https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/010_Cross_validation/003_chi_square_analysis_Pre_design_cross_validation_Coding/pics/2019_07_15_11:37:30.png

# # ================================================================================
# # print("vitamin_plac_cold_df",vitamin_plac_cold_df)
# #       group     cold
# # 0   Vitamin  No_cold
# # 1   Vitamin  No_cold
# # 2   Vitamin  No_cold
# # 3   Vitamin  No_cold
# # 4   Vitamin  No_cold
# # 5   Vitamin  No_cold

# vitamin_data=vitamin_plac_cold_df[vitamin_plac_cold_df["group"]=="Vitamin"]
# vitamin_cold=list(vitamin_data["cold"])
# vitamin_cold=[1 if x=="No_cold" else x for x in vitamin_cold]
# vitamin_cold=[2 if x=="Cold" else x for x in vitamin_cold]
# # print("vitamin_cold",vitamin_cold)
# # [1, 1, 1, 1, 1, 1, 1, 2, 2, 2]

# placebo_data=vitamin_plac_cold_df[vitamin_plac_cold_df["group"]=="Placebo"]
# placebo_cold=list(placebo_data["cold"])
# placebo_cold=[1 if x=="No_cold" else x for x in placebo_cold]
# placebo_cold=[2 if x=="Cold" else x for x in placebo_cold]
# # print("placebo_cold",placebo_cold)
# # [1, 1, 1, 1, 2, 2, 2, 2, 2, 2]

# ================================================================================
#    smoking  lung  count
# 0  1        1     73   
# 1  1        2     17   
# 2  2        1     40  
# 3  2        2     50  

smoking_data=np.array([1]*73+[2]*17)
# print("smoking_data",smoking_data)
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

non_smoking_data=np.array([1]*40+[2]*50)
# print("non_smoking_data",non_smoking_data)
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

obs = np.array([smoking_data,non_smoking_data])
# print("obs",obs)

# [list([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
#  list([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])]


result=sp.stats.chi2_contingency(obs)
# print("result",result)
# (6.710881174899866, 
#  1.0, 
#  89, 
#  array([[0.86639676, 0.86639676, 0.86639676, 0.86639676, 0.86639676,
#          0.86639676, 0.86639676, 0.86639676, 0.86639676, 0.86639676,
#          0.86639676, 0.86639676, 0.86639676, 0.86639676, 0.86639676,
#          0.86639676, 0.86639676, 0.86639676, 0.86639676, 0.86639676,
#          0.86639676, 0.86639676, 0.86639676, 0.86639676, 0.86639676,
#          0.86639676, 0.86639676, 0.86639676, 0.86639676, 0.86639676,
#          0.86639676, 0.86639676, 0.86639676, 0.86639676, 0.86639676,
#          0.86639676, 0.86639676, 0.86639676, 0.86639676, 0.86639676,
#          1.29959514, 1.29959514, 1.29959514, 1.29959514, 1.29959514,
#          1.29959514, 1.29959514, 1.29959514, 1.29959514, 1.29959514,
#          1.29959514, 1.29959514, 1.29959514, 1.29959514, 1.29959514,
#          1.29959514, 1.29959514, 1.29959514, 1.29959514, 1.29959514,
#          1.29959514, 1.29959514, 1.29959514, 1.29959514, 1.29959514,
#          1.29959514, 1.29959514, 1.29959514, 1.29959514, 1.29959514,
#          1.29959514, 1.29959514, 1.29959514, 1.73279352, 1.73279352,
#          1.73279352, 1.73279352, 1.73279352, 1.73279352, 1.73279352,
#          1.73279352, 1.73279352, 1.73279352, 1.73279352, 1.73279352,
#          1.73279352, 1.73279352, 1.73279352, 1.73279352, 1.73279352],
#         [1.13360324, 1.13360324, 1.13360324, 1.13360324, 1.13360324,
#          1.13360324, 1.13360324, 1.13360324, 1.13360324, 1.13360324,
#          1.13360324, 1.13360324, 1.13360324, 1.13360324, 1.13360324,
#          1.13360324, 1.13360324, 1.13360324, 1.13360324, 1.13360324,
#          1.13360324, 1.13360324, 1.13360324, 1.13360324, 1.13360324,
#          1.13360324, 1.13360324, 1.13360324, 1.13360324, 1.13360324,
#          1.13360324, 1.13360324, 1.13360324, 1.13360324, 1.13360324,
#          1.13360324, 1.13360324, 1.13360324, 1.13360324, 1.13360324,
#          1.70040486, 1.70040486, 1.70040486, 1.70040486, 1.70040486,
#          1.70040486, 1.70040486, 1.70040486, 1.70040486, 1.70040486,
#          1.70040486, 1.70040486, 1.70040486, 1.70040486, 1.70040486,
#          1.70040486, 1.70040486, 1.70040486, 1.70040486, 1.70040486,
#          1.70040486, 1.70040486, 1.70040486, 1.70040486, 1.70040486,
#          1.70040486, 1.70040486, 1.70040486, 1.70040486, 1.70040486,
#          1.70040486, 1.70040486, 1.70040486, 2.26720648, 2.26720648,
#          2.26720648, 2.26720648, 2.26720648, 2.26720648, 2.26720648,
#          2.26720648, 2.26720648, 2.26720648, 2.26720648, 2.26720648,
#          2.26720648, 2.26720648, 2.26720648, 2.26720648, 2.26720648]]))

# ================================================================================
# chi2 : float
# The test statistic.

# p : float
# The p-value of the test

# dof : int
# Degrees of freedom

# expected : ndarray, same shape as observed
# The expected frequencies, based on the marginal sums of the table.

# ================================================================================
