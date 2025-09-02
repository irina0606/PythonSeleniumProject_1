n = int(input())
arr = []

for _ in range(1, n+1):
    s = input()
    list_ = s.split(", ")
    result = list_[0][:-5] + ", " + list_[1]
    arr.append(result)
if arr == sorted(arr):
    print("YES")
else:
    print("NO")







