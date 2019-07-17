# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/005_Probability_distribution/002_Normal_distribution && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
from scipy.stats import norm

# ================================================================================
# Normal distribution
# By using accumulated data, you can predict the future via normal distribution

# ================================================================================
# <./pics/2019_07_16_11:59:26.png>

# 2 parameters in normal distribution
# mean
# variance

# ================================================================================
# <./pics/2019_07_16_12:24:08.png>

# <./pics/2019_07_16_12:25:10.png>

# ================================================================================
# <./pics/2019_07_16_12:25:44.png>

# region A to region B
# 100 measures
# mean 170 mins
# std 10 mins

# when you get random train, calculate
# P(x>185)

# ================================================================================
# - Perform standarization
# - Use std table

# ================================================================================
# Standardization fomular (x to z)
# z=(x-mu)/std

# ================================================================================
# Standardization function
def standarization_to_z_distribution(X,mu,sigma):
  z=(X-mu)/sigma
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
standard_normal_distribution_1_5=st.norm.cdf(1.5)
# print("standard_normal_distribution_1_5",standard_normal_distribution_1_5)
# 0.9331927987311419

# ================================================================================
X_seq_vals=np.arange(-3.0,3.1,0.1)
X_seq_vals=list(map(lambda x:round(x,2),X_seq_vals))
X_seq_vals=np.array(X_seq_vals)
# print("X_seq_vals",X_seq_vals)
# [-3.  -2.9 -2.8 -2.7 -2.6 -2.5 -2.4 -2.3 -2.2 -2.1 -2.  -1.9 -1.8 -1.7

z_prob_vals=list(map(lambda x:st.norm.cdf(x),X_seq_vals))
z_prob_vals=np.array(z_prob_vals)
# print("z_prob_vals",z_prob_vals)
# [0.0013499  0.00186581 0.00255513 0.00346697 0.00466119 0.00620967

plt.title("z distribution (cumulative)")
plt.plot(X_seq_vals,z_prob_vals)
plt.axvline(x=1.5,color='k',linestyle='--')
plt.xlim(-3.5,3.5)
plt.ylim(0,1)
plt.ylabel("Probability")
plt.show()
# <./pics/2019_07_16_13:04:20.png>

# ================================================================================
z_prob_vals=list(map(lambda x:norm.pdf(x),X_seq_vals))
z_prob_vals=np.array(z_prob_vals)
# print("z_prob_vals",z_prob_vals)
# [0.00443185 0.00595253 0.00791545 0.01042093 0.01358297 0.0175283

plt.title("z distribution (no cumulative)")
plt.plot(X_seq_vals,z_prob_vals)
plt.axvline(x=1.5,color='k',linestyle='--')
plt.xlim(-3.5,3.5)
plt.ylim(0,1)
plt.ylabel("Probability")
plt.show()
# <./pics/2019_07_16_13:05:31.png>

# ================================================================================
# <./pics/2019_07_16_13:06:17.png>

# ================================================================================
