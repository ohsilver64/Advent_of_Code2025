import numpy as np




def read_file(filepath):
    with open(filepath,'r') as f:
        lines = [list(line.strip()) for line in f.readlines()]
        arr = np.array(lines)
    return arr

def is_paper(arr,row,col):
    char = arr[row,col]
    return char == "@"



def count_rolls(arr,row,col):
    if not is_paper(arr,row,col):
        return False
    search = arr[row-1:row+2, col-1:col+2].flatten()
    count = np.sum(search=="@")
    return count

def search_for_paper(arr,rows,cols):
    for i in rows:
        for j in cols:
            if is_paper(input,i,j) and count_rolls(input,i,j) <=4:
                count+=1
                arr[i,j] = "."
            else:
                continue
    return arr,count

def new_arr(input,rows,cols,count):
    arr = input
    for i in rows:
        for j in cols:
            if is_paper(arr,i,j) and count_rolls(arr,i,j) <=4:
                count +=1
                arr[i,j] = "."
            else:
                continue
    return arr,count
    

def solutionA(input):
    rows = range(1,137)
    cols = range(1,137) #since this is the shape of the array, but we want to take whats inside the padding
    count = 0
    for i in rows:
        for j in cols:
            if is_paper(input,i,j) and count_rolls(input,i,j) <=4:
                count+=1
            else:
                continue
    return count

def solutionB(input):
    rows = range(1,137)
    cols = range(1,137)
    count = 0
    iterations = 100
    for it in range(0,iterations): #I really should use a while loop
        arr,newcount = new_arr(input,rows,cols,count)
        if count == newcount:
            return count
        count = newcount
        input = arr
    return None


def main():
    input = read_file('input.txt')
    padded_input = np.pad(input, pad_width=1,mode='constant',constant_values = 0)
    print(solutionA(padded_input))
    print(solutionB(padded_input))


main()

