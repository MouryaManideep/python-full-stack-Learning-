from collections import Counter
arr = "Mourya Manideep Kandregula"

freq = Counter(arr)
print(type(freq))
print(freq)
l = list(freq.items())
print(l)
print(type(l))
print(l[0])