flagAsk = False 
x = None
while True:
  if flagAsk:
    while True:
      print("novo calculo (1-sim 2-nao)")
      res = input()
      if res == '1':
        flagAsk = False
        break
      elif res == '2':
         exit()
  a = float(input())
  
  if 0 <= a <= 10:
    if x == None:
      x = a
      continue
    else:
      print("media = %.2f" % ((x + a)*0.5))
      flagAsk = True
      x = None
  else:
    print("nota invalida")
  
