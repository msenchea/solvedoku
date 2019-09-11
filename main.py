import sys

data = sys.stdin.read().strip().split()

data = ''.join(data)

#set of 3 columns, starting step in range 0-2.
for i in range(1, 81, 9):
    print(data[i], data[i + 1], data[i + 2])




