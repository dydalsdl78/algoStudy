T = int(input())

for tc in range(1, T+1):
  tmp = list(map(int, input().split()))
  D, L, N = tmp[0], tmp[1], tmp[2]

  ans = 0
  for n in range(0, N):
    ans += D * (1 + n * L / 100)

  print("#{} {}".format(tc, int(ans)))