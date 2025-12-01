import pandas as pd

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

#tester = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']

def correct_count(input):  #this function corrects the number if it is less than 0 or greater than 99
    if input < 0:
        return 100 + input
    if input > 99 : # must be smaller than 198 though!
        return input - 100
    else:
        return input



def turn_dial(inp,current):
    direction = inp[0]
    magnitude = int(inp[1:])
    magnitude = magnitude % 100 # since the dial is circular, ensures the change is not more than 99


    if direction == "L":
        current = current - magnitude
        current = correct_count(current)
    
    if direction == "R":
        current = current + magnitude
        current = correct_count(current)
    return current

def solution_1(input):
    current = 50
    zeros = 0
    for line in input:
        current = turn_dial(line,current)
        if current == 0:
            zeros = zeros + 1
        print(current)
    return zeros

def __main__():
    input = read_file('day1_input.txt')
    sol1 = solution_1(input)
    print(f"The code for problem 1 is {sol1}")
    pass

if __name__ == "__main__":
    __main__()