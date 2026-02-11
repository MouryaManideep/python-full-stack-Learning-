n, m = map(int, input().split())
happiness = 0
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

for i in range(0, m):
    if(A[i] in arr):
        happiness += 1
    if(B[i] in arr):
        happiness -= 1

print(happiness)