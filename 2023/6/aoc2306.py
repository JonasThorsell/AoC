import math

time = [int(x) for x in input().split()[1:]]
dist = [int(x) for x in input().split()[1:]]
p = [0]*len(time)
for i in range(len(time)):
    t = time[i]
    for t0 in range(t+1):
        if t*t0-t0**2 > dist[i]:
            p[i] += 1
print(math.prod(p))

time2 = int(''.join([str(x) for x in time]))
dist2 = int(''.join([str(x) for x in dist]))
t0a = (-time2 + math.sqrt(time2**2 - 4 * dist2)) / (-2)
t0b = (-time2 - math.sqrt(time2**2 - 4 * dist2)) / (-2)
print(math.floor(t0b)-math.floor(t0a))
