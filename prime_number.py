N = int(input())
cnt = 0
for i in range(1, N + 1):
  if N%i == 0:
     cnt += 1
if cnt == 2:
     print("prime")
else:
     print("not a prime")
     