import sys

read = sys.stdin.readline
idx = 0
cnt = 0
species = dict()
li = []

while True:
    name = read().rstrip()
    # "EOF"냐? "빈 문자열"이냐?
    if not name:
        break
    if species.get(name) == None:
        species[name] = idx
        li.append(1)
        idx += 1
    else:
        li[species[name]] += 1

    cnt += 1

# print(species)
for key in sorted(species.keys()):
    print("{0} {1:0.4f}".format(key, li[species[key]]/cnt*100))
