def read_file(filepath):
    with open(filepath, 'r') as f:
        lines =  f.readlines()
    data =  [line.strip() for line in lines]
    linebreak = data.index('')
    ranges = data[0:linebreak]
    ingredients = data[linebreak+1:]
    return ranges, ingredients
    

test = [['3-5',
'10-14',
'16-20',
'12-18'],['1','4','10','15']]

def process_range(r):
    left, right = r.split('-')
    return int(left), int(right)

def check_is_fresh(ingredient,ranges):
    ingredient = int(ingredient)
    for r in ranges:
        left,right= process_range(r)
        if left <= ingredient <= right:
            return True
    return False

def sort_ranges(ranges):
    return sorted(ranges, key=lambda r: process_range(r)[0])
        

def solutionA(input):
    ranges,ingredients = input
    count = 0
    for i in ingredients:
        if check_is_fresh(i,ranges):
            count += 1
    return count

def process_range(r):
    left, right = r.split('-')
    return int(left), int(right)


def solutionB(inp):
    ranges, ingredients = inp  # ingredients ignored for part B

    # 1) Parse to numeric intervals
    intervals = [process_range(r) for r in ranges]

    # 2) Sort by start
    intervals.sort(key=lambda x: x[0])

    # 3) Merge and accumulate length
    total = 0
    cur_start, cur_end = intervals[0]

    for s, e in intervals[1:]:
        if s > cur_end:  # disjoint interval
            # add length of finished merged interval
            total += cur_end - cur_start + 1
            cur_start, cur_end = s, e
        else:  # overlapping or touching
            cur_end = max(cur_end, e)

    # add last merged interval
    total += cur_end - cur_start + 1

    return total

def main():
    input = read_file('input.txt')
    #input = test
    print(solutionA(input))
    print(solutionB(input))


main()