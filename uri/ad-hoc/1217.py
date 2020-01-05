
n = int(input())
tot_fruits = 0
tot_price = 0
for i in range(n):
    price = float(input())
    fruits = [x for x in input().split()]
    tot_fruits += len(fruits)
    tot_price += price
    print("day %d: %d kg" % (i+1, len(fruits)))
print("%.2f kg by day" % (tot_fruits/n))
print("R$ %.2f by day" % (tot_price/n))
