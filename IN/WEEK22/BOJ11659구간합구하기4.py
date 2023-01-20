import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_list = list(map(int, input().split()))
sum_list = [0] * len(num_list)
sum_list[0] = num_list[0]

if N == 1:
	print(num_list[0])
else:
	for i in range(1, len(num_list)):
		sum_list[i] += sum_list[i-1] + num_list[i]

	for i in range(M):
		st, en = map(int, input().split())
		print(sum_list[en-1] - sum_list[st-1] + num_list[st-1])