while True: 
  sol = []
  sol2 = []
  a, b = map(int, input().split())
  if a <= 0 or b <= 0:
    break
  for x in range(min(a,b), max(a,b)+1):
    sol.append(str(x))
    sol2.append(x)
  endS = ' Sum='+str(sum(sol2))+'\n'
  s = ' '.join(sol)
  print(s, end = endS)