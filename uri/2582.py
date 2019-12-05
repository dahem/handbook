dic = ['PROXYCITY',
       'P.Y.N.G.',
       'DNSUEY!',
       'SERVERS',
       'HOST!',
       'CRIPTONIZE',
       'OFFLINE DAY',
       'SALT',
       'ANSWER!',
       'RAR?',
       'WIFI ANTENNAS']
n = int(input())
for x in range(n):
    a, b = map(int, input().split())
    print(dic[a+b])
