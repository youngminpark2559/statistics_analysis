# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee/003_Statistical_analysis/002_Load_csv_file && \
# rm e.l && Rscript main.r \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# When you load csv file
# - You don't need to use stringAsFactor
# - You don't need to use sep because CSV uses ,

# ================================================================================
# Load txt file

gradecsv<-read.csv(
  "./data/0202.grade.csv",header=TRUE,na.strings=".")
gradecsv
#    sex subject grade
# 1 Male       1     3
# 2 Male       1     4
# 3 Male       1     5
# 4 Male       1     3

# ================================================================================
# See structure of data
str(gradecsv)
# 'data.frame':	4 obs. of  3 variables:
#  $ sex    : Factor w/ 1 level "Male": 1 1 1 1
#  $ subject: int  1 1 1 1
#  $ grade  : int  3 4 5 3

# ================================================================================
