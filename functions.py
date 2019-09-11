masterset = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

#completes a horizontal line with 1 missing number.
def complete_line(line):
 if line.count('-') == 1:
     missing = list(masterset.difference(set(line)))[0]
     line = (''.join(line)).replace('-', missing)
     return(line)
