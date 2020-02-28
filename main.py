import sys
import tkinter as tk
import time

def solver(data):
    master_set = {1,2,3,4,5,6,7,8,9}

    data = data

    empty_count = 0
    for i in data:
        if i == '0':
            empty_count += 1

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

    def basic_solver(rows):
        stump_count = 1
        for i in range(9):
            for j in range(9):
                if rows[i][j] == 0:
                    poss_vals = get_vals(i,j)
                    if len(poss_vals) == 1:
                        rows[i][j] = poss_vals[0]
                        stump_count = 0
        return(rows, stump_count)

    def advanced_solver(i,j,rows):
        if rows[i][j] == 0:
            poss_vals = get_vals(i,j)

            #row check
            row_poss = []
            for x in range(9):
                if x == j:
                    continue
                if rows[i][x] == 0:
                    for val in get_vals(i,x):
                        row_poss.append(val)
            if len(set(poss_vals) - set(row_poss)) == 1:
                rows[i][j] = list(set(poss_vals) - set(row_poss))[0]
                return rows

            #col check
            col_poss = []
            for y in range(9):
                if y == i:
                    continue
                if rows[y][j] == 0:
                    for val in get_vals(y,j):
                        col_poss.append(val)
            if len(set(poss_vals) - set(col_poss)) == 1:
                rows[i][j] = list(set(poss_vals) - set(col_poss))[0]
                return rows

            #box check
            first = [0,1,2]
            second = [3,4,5]
            third = [6,7,8]
            boxes = [first,second,third]

            for l in boxes:
                if i in l:
                    row = l
                if j in l:
                    col = l

            box_poss = []
            for x in row:
                for y in col:
                    if rows[x][y] == 0:
                        for val in get_vals(x,y):
                            box_poss.append(val)
            if len(set(poss_vals) - set(box_poss)) == 1:
                rows[i][j] = list(set(poss_vals) - set(box_poss))[0]
                return rows
        return rows


    ### MAIN BODY
    while empty_count > 0:
        seconds = time.time()
        rows, stump_count = basic_solver(rows)

        if stump_count > 0:
            for i in range(9):
                for j in range(9):
                    rows = advanced_solver(i,j,rows)

        empty_count = 0
        for i in range(9):
            for j in range(9):
                if rows[i][j] == 0:
                    empty_count += 1

        #if seconds > 60:
        #    print('Invalid Sudoku, please try again.')
        #    return(rows)

    for x in range(9):
        for y in range(9):
            rows[x][y] = str(rows[x][y])
    return(rows)

def main():
    class Window(tk.Tk):
        large_font = ('Verdana',30)

        def __init__(self):
            tk.Tk.__init__(self)
            self.title("Solvedoku")
            self.resizable(False, False)
            large_font = ('Verdana',30)
            self.entries = [[None for col in range(9)] for row in range(9)]
            cornercolor =[0,1,2,6,7,8]
            centercolor = [3,4,5]
            vcmd = (self.register(self.NumberValidation),
                 '%P')

            for row in range(9):
                for col in range(9):
                    if (row in cornercolor and col in cornercolor) or (row in centercolor and col in centercolor) :
                        self.e = tk.Entry(self,font=large_font, width=2, highlightbackground='black', highlightthickness=0,bg='#E8E8E8' , justify='center', validate='key', validatecommand=vcmd)
                    else:
                        self.e = tk.Entry(self,font=large_font, width=2, highlightbackground='black', highlightthickness=0, justify='center', validate='key',validatecommand=vcmd)
                    self.e.grid(row=row, column=col, columnspan=1, rowspan=1, padx=3, pady=3)
                    self.entries[row][col] = self.e

            instructions = tk.Label(text='Enter known numbers into grid and press "Solve".')
            instructions.grid(row=10, columnspan=9, rowspan=2)
            B_solve = tk.Button(self,text='Solve', command=self.on_button)
            B_solve.grid(column=4, row=13)

        def on_button(self):
            accepted=['1','2','3','4','5','6','7','8','9']
            data = ''
            for x in range(9):
                for y in range(9):
                    if self.entries[x][y].get() not in accepted:
                        data += ('0')
                    else:
                        data += (self.entries[x][y].get())
            complete = solver(data)

            for x in range(9):
                for y in range(9):
                    self.entries[x][y].delete(0,1)
                    self.entries[x][y].insert(0,complete[x][y])

        def NumberValidation(self, S):
            if (S in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and len(S) < 2) or S == '':
                return True
            self.bell() # .bell() plays that ding sound telling you there was invalid input
            return False


    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()