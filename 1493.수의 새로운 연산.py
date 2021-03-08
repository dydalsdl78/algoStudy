T = int(input())

for tc in range(1, T+1):
  p, q = map(int, input().split())
  
  sum1 = 0
  x1, y1 = 0, 0

  for i in range(10000):
    sum1 += i
    # sum1이 p값을 넘어 갈 때가 i(대각선)의 값
    if sum1 >= p:
      x1 = i - (sum1 - p)
      # i = x + y + 1을 만족
      y1 =  i + 1 - x1
      break

  sum2 = 0
  x2, y2 = 0, 0

  for j in range(10000):
    sum2 += j
    if sum2 >= q:
      x2 = j - (sum2 - q)
      y2 = j + 1 - x2
      break

  r_x = x1 + x2
  r_y = y1 + y2

  r_s = 0
  for k in range(1, r_x + r_y):
    r_s += k
  
  ans = r_s - (r_y - 1)

  print("#{} {}".format(tc, ans))

  