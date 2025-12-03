def read_file(filepath):
    with open(filepath,'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]
    
def sort_desc(line):
    return sorted(line,reverse=True)

def find_largest_two(line):

    nums = sort_desc(line)
    largest,second = nums[:2]
    
    if line.index(second) > line.index(largest):
        return int(f'{largest}{second}')
    if line.index(largest) == len(line) - 1:
        return int(f'{second}{largest}')
    else:
        num2 = sorted(line[line.index(largest):],reverse=True)[1]
        return int(f'{largest}{num2}')
    


def find_largest_12(line):
    num = []
    added = 0
    largest_idx = -1
    while len(num)<12:
        start = largest_idx+1
        search = line[start:len(line)-11+added]
        largest = sort_desc(search)[0]
        
        offset = search.index(largest)
        largest_idx = start + offset
        num.append(largest)
        added +=1


    return num

def solutionA(input):
    count = 0
    for l in input:
        count += find_largest_two(l)
    return count

def solutionB(input):
    count = 0
    for l in input:
        num_list = find_largest_12(l)
        number = int(''.join(tuple(num_list)))
        count+= number
    return count

def main():
    input = read_file('input.txt')
    print(solutionA(input))
    print(solutionB(input))

main()