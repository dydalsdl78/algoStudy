T = int(input())

for tc in range(1, T+1):
  P = input().strip()
  Q = input().strip()

  if Q == P + "a":
    print("#{} N".format(tc))
  else:
    print("#{} Y".format(tc))
