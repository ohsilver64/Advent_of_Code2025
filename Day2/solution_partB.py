import math

def open_file(filepath):
    with open(filepath,'r') as f:
        lines = f.readline()
        return lines.split(',')
        

def find_digits(num): #finds the n of digits in the number
    if type(num) != int:
        raise ValueError
    n = math.log10(num)
    if int(n) - n  == 0:
        return int(n) + 1
    n = math.ceil(n)
    return n

def find_blocksizes(num): # finds all possible block sizes a number can be split into
    blocksize = []
    digits = find_digits(num)
    for i in range(1,9):
        if digits % i == 0 and digits != i:
            blocksize.append(i)
    return blocksize

def find_invalid(strings):
    """This function takes a string of form 'x-x' and returns a list of possible invalid integers within the range"""
    nums = strings.split('-')
    small,large = int(nums[0]),int(nums[1])
    invalids = []
    

    if find_digits(small) == find_digits(large): #if the num of digits is the same 
        blocksizes = find_blocksizes(small)

        for size in blocksizes:
            minrepeater = int(str(small)[0:size])
            maxrepeater = int(str(large)[0:size])
            for i in range(minrepeater,maxrepeater+1):
                x = int(int(find_digits(small)/size) * str(i)) #make the invalid code
                if small <= x <= large:
                    invalids.append(x)
            
    if find_digits(small) != find_digits(large): #if small number and large number have different n of digits 
        midsmall = int((find_digits(small)) * '9')
        midlarge = midsmall +1

        blocksizes_a = find_blocksizes(small)
        blocksizes_b = find_blocksizes(large)

        for size in blocksizes_a:
            minrepeater = int(str(small)[0:size])
            maxrepeater = int(str(midsmall)[0:size])
            for i in range(minrepeater,maxrepeater+1):
                x = int(int(find_digits(small)/size) * str(i)) #make the invalid code
                if small <= x <= midsmall:
                    invalids.append(x)
    
        for size in blocksizes_b:
            minrepeater = int(str(midlarge)[0:size])
            maxrepeater = int(str(large)[0:size])
            for i in range(minrepeater,maxrepeater+1):
                x = int(int(find_digits(large)/size) * str(i)) #make the invalid code
                if midlarge <= x <= large:
                    invalids.append(x)
    else:
        pass
    return set(invalids)

def main():
    input = open_file('input.txt')
    count = 0
    for line in input:
        for i in find_invalid(line):
            count += int(i)
    print(f"the sum of invalid ids is {count}")



main()