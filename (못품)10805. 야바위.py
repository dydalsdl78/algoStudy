T = int(input())

for tc in range(1, T+1):
  N, Q = map(int, input().split())
  N_cup = [c for c in range(N)]
  
  for i in range(Q):
    A, B = map(int, input().split())
    N_cup[A], N_cup[B] = N_cup[B], N_cup[A]
  