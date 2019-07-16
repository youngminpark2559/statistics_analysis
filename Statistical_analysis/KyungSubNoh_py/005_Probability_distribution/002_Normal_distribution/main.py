# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/006_Probability_distribution/002_Normal_distribution && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
from scipy.stats import norm

# ================================================================================
# Normal distribution
# By using acumulated data, you can predict the future via normal distribution

# ================================================================================
# /home/young/Pictures/2019_07_16_11:59:26.png

# 2 parameters
# mean
# variance

# ================================================================================
# /home/young/Pictures/2019_07_16_12:24:08.png

# /home/young/Pictures/2019_07_16_12:25:10.png

# ================================================================================
# /home/young/Pictures/2019_07_16_12:25:44.png

# region A to region B
# 100 measures
# mean 170 mins
# std 10 mins

# when you get random train, calculate
# P(x>185)

# ================================================================================
# Perform standarization
# Use std table

# ================================================================================
# Stardardization fomular
# z=(x-mu)/std

# ================================================================================
# Stardardization function
def standarization_to_z_distribution(X,mu,sigma):
  z=(X-mu)/sigma
  # print("z",z)
  # 1.5
  return z

# ================================================================================
z_value=standarization_to_z_distribution(X=185,mu=170,sigma=10)
# print("z_value",z_value)
# 1.5

# ================================================================================
# Calculate P(z>1.5) by using z-table instead of P(x>180)

# ================================================================================
# P(z>1.5)=0.933193
# 1-0.933193=0.066807=6.68%

# ================================================================================
# print("st.norm.cdf(1.5)",st.norm.cdf(1.5))
# 0.9331927987311419

# ================================================================================
seq=np.arange(-3.0, 3.1, 0.1)
seq=list(map(lambda x:round(x,2),seq))
seq=np.array(seq)
# print("seq",seq)
# [-3.0, -2.9, -2.8, -2.7,
# print("seq",type(seq[0]))
# print("seq",seq.shape)

z_vals=list(map(lambda x:st.norm.cdf(x),seq))
z_vals=np.array(z_vals)
# z_vals=list(map(lambda x:round(x,2),z_vals))
# print("z_vals",z_vals)
# print("z_vals",z_vals.shape)
# print("z_vals",type(z_vals[0]))
# [0.0013498980316300933, 0.0018658133003840375, 0.002555130330427932, 0.0034669738030406647, 0.004661188023718747, ...
#  0.998134186699616, 0.9986501019683699]

plt.title("Z distribution (cumulative)")
plt.plot(seq,z_vals)
plt.axvline(x=1.5,color='k',linestyle='--')
plt.xlim(-3.5,3.5)
plt.ylim(0,1)
plt.ylabel("Probability")
plt.show()
# /home/young/Pictures/2019_07_16_13:04:20.png

# ================================================================================
z_vals=list(map(lambda x:norm.pdf(x),seq))
z_vals=np.array(z_vals)
# print("z_vals",z_vals)
# [0.00443185 0.00595253 0.00791545 0.01042093 0.01358297 0.0175283
#  0.02239453 0.02832704 0.03547459 0.0439836  0.05399097 0.06561581

plt.title("Z distribution")
plt.plot(seq,z_vals)
plt.axvline(x=1.5,color='k',linestyle='--')
plt.xlim(-3.5,3.5)
plt.ylim(0,1)
plt.ylabel("Probability")
plt.show()
# /home/young/Pictures/2019_07_16_13:05:31.png

# ================================================================================
# /home/young/Pictures/2019_07_16_13:06:17.png

# ================================================================================
