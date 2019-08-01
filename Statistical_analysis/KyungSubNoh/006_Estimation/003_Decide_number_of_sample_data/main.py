# ================================================================================
# Large sample data: good, credibility increases

# $$$\bar{X} \pm z_{\frac{\alpha}{2}} \times \text{standard error} \\ $$$
# $$$= \bar{X} \pm z_{\frac{\alpha}{2}} \times \frac{\sigma}{\sqrt{n}}$$$

# ================================================================================
# Simplify above equation with respect to n

# ================================================================================
# c n: proper size of sample from the population
# $$$ n = \dfrac{z_{\frac{\alpha}{2} \times \sigma}}{d} $$$
# $$$ n = \left \dfrac{z_{\frac{\alpha}{2} \times \sigma}}{d} \right^2 $$$
# d: allowed error

# ================================================================================
# <./pics/2019_07_16_19:16:53.png>

# confidence: 99%
z=2.58

# allowed error += 100ml
d=100

# population_std: 150ml
population_std=150

/home/young/Pictures/2019_07_22_08:34:29.png

# ================================================================================
# confidence: 99%
z_half_alpha=2.58

d=100

# When you don't know population std, you extract 10 number of samples to calculate sample_std
sample_std=170

/home/young/Pictures/2019_07_22_08:34:43.png

