n = int(input())
s = n*n
rev = 0
while n>0:
    r = n % 10
    rev = rev*10+r
    n = n//10
k = rev*rev
rev1 = 0
while k>0:
    r = k%10
    rev1 = rev1*10+r
    k = k//10
print(rev1 == s)