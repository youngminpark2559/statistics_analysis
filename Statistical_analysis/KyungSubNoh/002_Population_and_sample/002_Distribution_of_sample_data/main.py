# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/002_Population_and_sample/002_Distribution_of_sample_data && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# Why sample's distribution is important (case1 and case2)
# <./pics/2019_07_15_20:49:07.png>

# ================================================================================
# In conclusion, you need to inspect the distribution of sample data

# ================================================================================
# Normal distribution
# <./pics/2019_07_15_20:49:59.png>

# ================================================================================
# Normalization
# <./pics/2019_07_15_21:02:20.png>

# ================================================================================
# cm kg
# <./pics/2019_07_15_21:03:17.png>

# 50 90
# <./pics/2019_07_15_21:03:25.png>

# ================================================================================
# Standard normal distribution
# = z distribution

# <./pics/2019_07_15_21:04:26.png>

# - When there is enough many sample
# - perform normalization on normal distribution
# - and get z distribution (standard normal distribution)

# - Use std of population

# ================================================================================
# t distribution

# <./pics/2019_07_15_21:05:11.png>

# - When there is not-enough many sample
# - perform normalization on normal distribution
# - and get t distribution (standard normal distribution)

# - Use std (s) of sample

# ================================================================================
# <./pics/2019_07_15_21:06:02.png>

# ================================================================================
# Relation between z distribution and t distribution
# <./pics/2019_07_15_21:07:30.png>

# ================================================================================
# chi-square distribution

# /home/young/Pictures/2019_07_22_05:36:05.png

# chi square distribution is induced from standard normal distribution

# chi square distribution = distribution of (z distribution)^2 

# random variable X: $$$x_1, x_2, x_3, ..., x_n$$$
# perform power of 2: $$$x_1^2, x_2^2, x_3^2, ..., x_n^2$$$
# $$$x_1^2, x_2^2, x_3^2, ..., x_n^2$$$ consist of new random variable $$$\chi^2$$$

# Distribution of $$$\chi^2$$$:
# dof is n
# $$$\chi^2$$$ distribution

# More number of sample in chi-square distribution ---> normal distribution

# ================================================================================
# F distribution
# <./pics/2019_07_15_21:08:45.png>

# 2 chi-square distributions
# 2 chi-square distributions' variance: $$$v_1, v_2$$$

# ================================================================================
# p hat distribution (sample ratio's distribution)
# <./pics/2019_07_15_21:09:19.png>
