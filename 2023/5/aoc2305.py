seeds = [int(x) for x in input().split(':')[1].split()]
input()
maps = []
try:
    while(True):
        input()
        maps.append([])
        while l := input():
            maps[-1].append([int(x) for x in l.split()])
except EOFError:
    pass

locations = []
for seed in seeds:
    x = seed
    for map in maps:
        for m in map:
            if m[1] <= x < (m[1] + m[2]):
                d = x - m[1]
                x = m[0] + d
                break
    locations.append(x)

print(min(locations))
