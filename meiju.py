# 开发时间 2023/1/16 14:10


"""
a+b+c=1000 且 a^2+b^2=c^2  求出abc的所有可能
"""

# 改进  c = 1000 - a - b
import time

start_time = time.time()
count = 0

"""
花费时间100s
"""
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a + b + c == 1000 and a * a + b * b == c * c:
#                 count += 1
#                 print(a, b, c)

"""
花费时间0.23s
"""
for a in range(1001):
    for b in range(1001):
        c = 1000 - a - b
        if a * a + b * b == c * c:
            count += 1
            print(a, b, c)

end_time = time.time()
print(f"使用时间{end_time - start_time}")
print(count)
