N, K = map(int, input().split())

views = list(map(int, input().split()))

window_dict = {}
result = []

for i in range(K):
    view = views[i]
    if view not in window_dict:
        window_dict[view] = 1
    else:
        window_dict[view] += 1

dict_len = len(window_dict)
result.append(dict_len)

for i in range(1, N - K + 1):
    pop_view = views[i - 1]
    if window_dict[pop_view] > 1:
        window_dict[pop_view] -= 1
    else:
        del window_dict[pop_view]
        dict_len -= 1
    add_view = views[i + K - 1]

    if add_view not in window_dict:
        window_dict[add_view] = 1
        dict_len += 1
    else:
        window_dict[add_view] += 1
    result.append(dict_len)

print(*result)
