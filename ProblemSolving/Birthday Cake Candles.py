n = int(input())
arr = list(map(int, input().rstrip().split()))
arr.sort()
print(arr.count(arr[-1]))
