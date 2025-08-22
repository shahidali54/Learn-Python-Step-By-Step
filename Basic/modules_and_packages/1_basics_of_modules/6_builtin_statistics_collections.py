# Is file me hum 2 built-in modules cover karenge:
# 1. statistics → mathematical statistics ke functions
# 2. collections → special container datatypes

import statistics
from collections import Counter, namedtuple, deque, defaultdict, OrderedDict

print("========== STATISTICS Module ==========\n")

data = [10, 20, 20, 30, 40, 50, 50, 50]

# Mean (average)
print("Mean:", statistics.mean(data))

# Median
print("Median:", statistics.median(data))

# Mode (most frequent value)
print("Mode:", statistics.mode(data))

# Standard Deviation (spread of data)
print("Standard Deviation:", statistics.stdev(data))


print("\n========== COLLECTIONS Module ==========\n")

# Counter (counts frequency of elements)
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(fruits)
print("Counter:", counter)

# namedtuple (like lightweight class)
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print("namedtuple Point:", p, "x =", p.x, "y =", p.y)

# deque (double-ended queue)
dq = deque([1, 2, 3])
dq.appendleft(0)   # add to left
dq.append(4)       # add to right
dq.pop()           # remove from right
print("Deque after operations:", dq)

# defaultdict (default value if key missing)
dd = defaultdict(int)
dd["a"] += 1
dd["b"] += 2
print("Defaultdict:", dict(dd))

#  OrderedDict (remembers insertion order)
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
print("OrderedDict:", od)
