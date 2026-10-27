# import sys
# from collections import Counter

# filename = sys.argv[1]

# with open(filename) as f:
#     lines = f.readlines()

# print("Total lines:",len(lines))

# counts = Counter()
# for line in lines :
#     fields = line.split()
#     if len(fields) > 0:
#         i = 0
#         key = fields[i]
#         while i<len(fields):
            
#             i+=1
#             counts[key] += 1 

# print("Top 5:")
# for item, n in counts.most_common(5):
#     print(item,n)




"""
Top 5:
2026-10-25 354573
so_gencnt: 318
WiFi 156
) 42
"Trusted 40
"""
"""
Top 5:
2026-10-25 17043
so_gencnt: 12
"Trusted 8
WiFi 6
"Cycle 4
"""


import sys
from collections import Counter
filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
print("Total lines:",len(lines))
counts = Counter()
for line in lines:
    fields = line.split()
    if len(fields) > 0:
        key = fields[0]
        counts[key] += 1
print("Top 5:")
for item, n in counts.most_common(5):
    print(item, n)

