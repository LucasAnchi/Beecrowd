from collections import deque

k = int(input('digite um num: '))
k = [x for x in range(1, int(k)+1)]
d = deque(k)
print(d)