# Exercise 2
#Evaluate the following expressions, giving that a = 6, b = 5, and c = 2.
# -5 * (781 % 3) + 4 * (1.6 + 2.9 / 2) – ( (19 // 5) % 2)
a = 4
b = 7
c = 2

-5 * (781 % 3) + 4 * (1.6 + 2.9 / 2) - ( (19 // 5) % 2)
# Remember the law of precendence
-5*(1) + 4 * (1.6 + 1.45) - (3%2)
-5 + 4 * 3.05 - 1
-5 + 12.2 - 1
6.2

# 4 * ( ( a % 5) * (4 + ( b – 3))) / ((c + 2) **2 )
4 * ( ( a % 5) * (4 + ( b - 3))) / ((c + 2) **2 )
4 * (1 * 4 + 2) / (4**2)
4 * (6) / 16
24/16
1.5

# Where P = 5.0, Q = 6.0, R = 8.0 and FLAG = True
P , Q, R, FLAG = 5.0, 6.0, 8.0, True
not FLAG and (((P*Q) > R) or ((P + Q) < R))
ans = False


# Suppose A = 4, B = 7 and C = 2, find the values of D and M, given  that
a = 4
b = 7
c = 2

d = not(a + b > 12) or (b-a < 2)
answer_to_d = True

m = (a < b) and (b < c) or (b == a)
answer_to_m = False