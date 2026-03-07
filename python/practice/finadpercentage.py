# import statistics as st
# n = int(input())
# d = {}
# for i in range(0,n-1):
#     l = list(input().split())
#     k = l[0]
#     d[k] = []
#     l.remove(k)
#     for j in range(0,n-1):
#         d[k].append(int(l[j]))

# key = input()

# if (key in d):
#     print(f"{st.mean(d.get(key)):.2f}")

l =[]
for i in range(5):
    l[i]=input().split()

for i in range(5):
    print(f"{i} is {type(l[i])}")