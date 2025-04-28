import sys

my_list = [1.0] * 1000  # List of 1,000 floats
print(
    "List Memory:",
    sys.getsizeof(my_list) + sum(sys.getsizeof(i) for i in my_list),
    "bytes",
)  # ~8KB
