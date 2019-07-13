# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/004_Statistical_analysis/004_Trimmed_mean && \
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

# ================================================================================
# /home/young/Pictures/2019_07_13_15:53:03.png

# ================================================================================
# Variance

houses=["A","B","C","D","E","F","G","H","I","J"]
num_of_children=[2,3,0,2,1,0,3,0,1,4]

d={'houses':houses,
   'num_of_children':num_of_children,}
df=pd.DataFrame(d)
# print("df",df)
#   houses  num_of_children
# 0  A      2              
# 1  B      3              
# 2  C      0              
# 3  D      2              
# 4  E      1              
# 5  F      0              
# 6  G      3              
# 7  H      0              
# 8  I      1              
# 9  J      4              

x_mean=df["num_of_children"].mean()
# print("x_mean",x_mean)
# 1.6

# ================================================================================
df["Difference (x_i-x_mean)"]=df["num_of_children"]-x_mean

# print("df",df)
#   houses  num_of_children  Difference (x_i-x_mean)
# 0  A      2                0.4                    
# 1  B      3                1.4                    
# 2  C      0               -1.6                    
# 3  D      2                0.4                    
# 4  E      1               -0.6                    
# 5  F      0               -1.6                    
# 6  G      3                1.4                    
# 7  H      0               -1.6                    
# 8  I      1               -0.6                    
# 9  J      4                2.4                    

# ================================================================================
# This is variance

df["Difference^2 (x_i-x_mean)^2"]=np.power(df["Difference (x_i-x_mean)"],2)
# print("df",df)
# df   houses  num_of_children  Difference (x_i-x_mean)  \
# 0  A      2                0.4                       
# 1  B      3                1.4                       
# 2  C      0               -1.6                       
# 3  D      2                0.4                       
# 4  E      1               -0.6                       
# 5  F      0               -1.6                       
# 6  G      3                1.4                       
# 7  H      0               -1.6                       
# 8  I      1               -0.6                       
# 9  J      4                2.4                       

#    Difference^2 (x_i-x_mean)^2  
# 0  0.16                         
# 1  1.96                         
# 2  2.56                         
# 3  0.16                         
# 4  0.36                         
# 5  2.56                         
# 6  1.96                         
# 7  2.56                         
# 8  0.36                         
# 9  5.76                         

# ================================================================================
# /home/young/Pictures/2019_07_13_16:03:17.png

# ================================================================================
# /home/young/Pictures/2019_07_13_16:04:38.png

# ================================================================================
