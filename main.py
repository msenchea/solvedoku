import sys
import functions

data = sys.stdin.read().strip().split()

data = ''.join(data)

#data initialisation
v_lines = []
h_lines = []

j = 0
while j < 9:
    temp = []
    for i in range(j, 81, 9):
        temp.append(data[i])
    h_lines.append(temp)
    j += 1

j = 1
while j <= 9:
    temp = []
    for i in range((j - 1) * 9, 9 * j, 1):
        temp.append(data[i])
    v_lines.append(temp)
    j += 1

print(v_lines)
print(h_lines)
