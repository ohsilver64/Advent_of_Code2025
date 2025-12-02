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

def find_invalid(strings):
    """This function takes a string of form 'x-x' and returns a list of possible invalid integers within the range"""
    nums = strings.split('-')
    small,large = int(nums[0]),int(nums[1])
    invalids = []
    


    if find_digits(small) == find_digits(large) and find_digits(small) %2 == 0: #if the num of digits is the same and even
        minrepeater = int(str(small)[0:int(find_digits(small)/2)])
        maxrepeater = int(str(large)[0:int(find_digits(small)/2)])
        for i in range(minrepeater,maxrepeater+1):
            if small <= int(f'{i}{i}') <= large:
                invalids.append(int(f'{i}{i}'))
            

    if find_digits(small)%2 == 0 and find_digits(large) %2 != 0: 
        minrepeater = int(str(small)[0:int(find_digits(small)/2)])
        maxrepeater = int(str(large)[0:int(find_digits(large)/2+0.5)])
        for i in range(minrepeater,int(find_digits(minrepeater)*'9')+1):
            if small <= int(f'{i}{i}') <= large:
                invalids.append(int(f'{i}{i}'))
    
    if find_digits(small)%2 != 0 and find_digits(large) %2 == 0:
        try:
            minrepeater = int(str(small)[0:int(find_digits(small)/2-0.5)])
        except:
            minrepeater = 1
        maxrepeater = int(str(large)[0:int(find_digits(large)/2)])
        for i in range(minrepeater,maxrepeater+1):
            if small <= int(f'{i}{i}') <= large:
                invalids.append(int(f'{i}{i}'))

    else:
        pass
    return invalids

def main():
    input = open_file('input.txt')
    count = 0
    for line in input:
        for i in find_invalid(line):
            count += int(i)
    print(f"the sum of invalid ids is {count}")



main()