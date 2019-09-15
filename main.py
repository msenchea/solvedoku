import sys

master_set = {1,2,3,4,5,6,7,8,9}

data = sys.stdin.read().strip().split()
data = ''.join(data)

empty_count = 0
for i in data:
    if i == '0':
        empty_count += 1

#data initialisation, changing numbers from strings to ints.
rows = []

j = 1
while j <= 9:
    temp = []
    for i in range((j - 1) * 9, 9 * j, 1):
        temp.append(int(data[i]))
    rows.append(temp)
    j += 1


### FUNCTIONS
def get_vals(i,j):
    poss_vals = list(check_rows(i,j).intersection(check_cols(j)).intersection(check_box(i,j)))
    return poss_vals

def check_rows(i,j):
    return master_set - set(rows[i])

def check_cols(j):
    temp = []
    for n in range(9):
        temp.append(rows[n][j])
    return master_set - set(temp)

def check_box(i,j):
    first = [0,1,2]
    second = [3,4,5]
    third = [6,7,8]
    boxes = [first,second,third]

    for l in boxes:
        if i in l:
            row = l
        if j in l:
            col = l

    temp = []
    for x in row:
        for y in col:
            temp.append(rows[x][y])
    return master_set - set(temp)

### MAIN BODY

while empty_count > 0:
    for i in range(9):
        for j in range(9):
            if rows[i][j] == 0:
                poss_vals = get_vals(i,j)
                if len(poss_vals) == 1:
                    rows[i][j] = poss_vals[0]
                    empty_count -= 1
                    print(f'steps left: {empty_count}')

for i in rows:
    print(i)