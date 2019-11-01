pFactors = [[2, 2], [3, 2]]

num = (2**2)*(3**2)
sol = []


def getDivisors(indFactor, lastDivisor):
    if indFactor >= len(pFactors):
        return
    for i in range(pFactors[indFactor][1] + 1):
        if indFactor + 1 < len(pFactors):
            getDivisors(indFactor + 1, lastDivisor)
            lastDivisor *= pFactors[indFactor][0]
        else:
            if i > 0:
                lastDivisor *= pFactors[indFactor][0]
            a = lastDivisor
            b = num / a
            sol.append(a)
            # if a == b:
            #     sol.append(a)
            # else:
            #     sol.append(a)
            #     sol.append(b)


getDivisors(0, 1)
print(sol)
sol2 = []
print("=========")


def getDivisors2(indFactor, lastDivisor):
    for i in range(pFactors[indFactor][1] + 1):
        if indFactor + 1 < len(pFactors):
            getDivisors2(indFactor + 1, lastDivisor)
            lastDivisor *= pFactors[indFactor][0]
        else:
            if i > 0:
                lastDivisor *= pFactors[indFactor][0]
            if lastDivisor ** 2 > num:
                return
            sol2.append(lastDivisor)
            if lastDivisor ** 2 != num:
                sol2.append(int(num / lastDivisor))


# sol.sort()


getDivisors2(0, 1)
print(sol2)
