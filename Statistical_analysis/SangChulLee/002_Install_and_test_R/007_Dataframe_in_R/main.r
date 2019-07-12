# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee/002_Install_and_test_R/007_Dataframe_in_R && \
# rm e.l && Rscript main.r \
# 2>&1 | tee -a e.l && code e.l

# https://www.youtube.com/watch?v=tMroNsF6_-k&list=PLEUKy_nwlzwFbxj6ilK2XXHJqBXMcTOOc&index=15

# ================================================================================
# Create vector
var1<-c(1,2,3,4)
var1
# 1 2 3 4

var2<-factor(c("M","F","F","M"))
var2
# M F F M

# ================================================================================
# Create dataframe
df=data.frame(id=var1,sex=var2)
df
#   id sex
# 1  1   M
# 2  2   F
# 3  3   F
# 4  4   M

# View(df)

# str(df)
