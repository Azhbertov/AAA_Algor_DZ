N, S = map(int, input().split())
nums = list(map(int, input().split()))

prefix_dict = {0: 1}
prefix_sum = 0
result = 0

for i in range(N):
    prefix_sum += nums[i]

    if prefix_sum - S in prefix_dict:
        result += prefix_dict[prefix_sum - S]

    if prefix_sum not in prefix_dict:
        prefix_dict[prefix_sum] = 1
    else:
        prefix_dict[prefix_sum] += 1

print(result)
