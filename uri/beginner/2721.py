names = ['Dasher', 'Dancer', 'Prancer', 'Vixen',
         'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']


arr = [int(x) for x in input().split()]

print(names[sum(arr) % 9 - 1])
