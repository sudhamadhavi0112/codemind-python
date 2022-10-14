n = int(input())
s = n
t = 0
while n > 0:
    r = n**2
    t = r%10+r//10
    n = n//10
if s == t:
    print('Neon Number')
else:
    print('Not Neon Number')