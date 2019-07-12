# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee/003_Statistical_analysis/005_Configure_factor && \
# rm e.l && Rscript main.r \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# /home/young/Pictures/2019_07_12_19:59:52.png

# Factor: categorical data
# sex: 1,2 (man, woman)
# school: 1,2,3,4 (elementary, middle, high, univ)

# ================================================================================
gradetxt<-read.table(
  "./data/0201.grade.txt",header=FALSE,sep=",",stringsAsFactors=FALSE,na.strings=".")
# gradetxt
#      V1   V2      V3    V4
# 1 index  sex subject grade
# 2     1 Male       1     3
# 3     1 Male       1     4
# 4     1 Male       1     5
# 5     1 Male       1     3

# str(gradetxt)
# 'data.frame':	5 obs. of  4 variables:
#  $ V1: chr  "index" "1" "1" "1" ...
#  $ V2: chr  "sex" "Male" "Male" "Male" ...
#  $ V3: chr  "subject" "1" "1" "1" ...
#  $ V4: chr  "grade" "3" "4" "5" ...

# plot(x=gradetxt$V2,y=gradetxt$V4)
# Error because you didn't use "factor type"

# ================================================================================
gradetxt$V2<-factor(gradetxt$V2,levels=c("Male","Female"))
str(gradetxt)
# 'data.frame':	5 obs. of  4 variables:
#  $ V1: chr  "index" "1" "1" "1" ...
#  $ V2: Factor w/ 2 levels "male","female": NA NA NA NA NA
#  $ V3: chr  "subject" "1" "1" "1" ...
#  $ V4: chr  "grade" "3" "4" "5" ...

# table(gradetxt$V2)
#   Male Female 
#      4      0 

plot(x=gradetxt$V2,y=gradetxt$V4)
