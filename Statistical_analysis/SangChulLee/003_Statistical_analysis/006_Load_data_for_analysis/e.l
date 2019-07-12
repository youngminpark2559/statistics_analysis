  id sex age job mrg school g_day age_c g_day_c  o1 o2 fb1 fb2 fb3 if1 if2 if3
1  1   1  18   1   2      1     3     1       2   4  4   1   4   5   1   2   2
2  2   2  23   5   2      3     3     2       2   3  3   5   2   5   3   3   3
3  3   1  23   1   2      3     1     2       1   3  3   2   3   4   4   2   4
4  4   2  20   1   2      2     3     1       2 4 4  2   3   4   2   2   3   5
5  5   1  22   2   2      4     1     2       1   3  3   3   3   3   2   2   2
6  6   1  24   2   2      4     2     2       1   4  4   2   2   2   2   2   2
7  7   1  21   5   2      2     1     2       1   3  4   3   3   3   3   3   4
  d1 d2 d3 d4 c1 c2 c3 c4 f1 f2 f3 f4
1  4  5  1  5  4  5  5  4  5  4  2  5
2  3  3  3  5  3  3  3  3  3  3  3  3
3  3  4  3  2  2  3  3  4  4  4  2  3
4  2  5  3  4  4  2  3  2  2  5  1 NA
5  3  3  3  3  2  3  2  2  3  4  3  2
6  3  2  3  2  3  3  3  3  1  3  3  3
7  4  3  3  2  3  4  4  4  4  4  3  3

'data.frame':	7 obs. of  29 variables:
 $ id     : int  1 2 3 4 5 6 7
 $ sex    : int  1 2 1 2 1 1 1
 $ age    : int  18 23 23 20 22 24 21
 $ job    : int  1 5 1 1 2 2 5
 $ mrg    : int  2 2 2 2 2 2 2
 $ school : int  1 3 3 2 4 4 2
 $ g_day  : int  3 3 1 3 1 2 1
 $ age_c  : int  1 2 2 1 2 2 2
 $ g_day_c: int  2 2 1 2 1 1 1
 $ o1     : Factor w/ 3 levels "3","4","4 4": 2 1 1 3 1 2 1
 $ o2     : int  4 3 3 2 3 4 4
 $ fb1    : int  1 5 2 3 3 2 3
 $ fb2    : int  4 2 3 4 3 2 3
 $ fb3    : int  5 5 4 2 3 2 3
 $ if1    : int  1 3 4 2 2 2 3
 $ if2    : int  2 3 2 3 2 2 3
 $ if3    : int  2 3 4 5 2 2 4
 $ d1     : int  4 3 3 2 3 3 4
 $ d2     : int  5 3 4 5 3 2 3
 $ d3     : int  1 3 3 3 3 3 3
 $ d4     : int  5 5 2 4 3 2 2
 $ c1     : int  4 3 2 4 2 3 3
 $ c2     : int  5 3 3 2 3 3 4
 $ c3     : int  5 3 3 3 2 3 4
 $ c4     : int  4 3 4 2 2 3 4
 $ f1     : int  5 3 4 2 3 1 4
 $ f2     : int  4 3 4 5 4 3 4
 $ f3     : int  2 3 2 1 3 3 3
 $ f4     : int  5 3 3 NA 2 3 3
