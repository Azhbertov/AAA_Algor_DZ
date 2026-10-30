N = int(input())

names = []
for _ in range(N):
    name = input()
    names.append("".join(sorted(name)))

names_dict = {}

for name in names:
    if name not in names_dict:
        names_dict[name] = 1
    else:
        names_dict[name] += 1

max_names = 0
for k, v in names_dict.items():
    if v > max_names:
        max_names = v

print(len(names_dict), max_names)
