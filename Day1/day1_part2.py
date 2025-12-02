import pandas as pd

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

tester = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']

def correct_count(input):  #this function corrects the number if it is less than 0 or greater than 99
    if input < 0:
        return 100 + input
    if input > 99 : # must be smaller than 198 though!
        return input - 100
    else:
        return input

def count_rotations(magnitude): #this function counts how many times the dial passes 0 as it rotates. Essentially a '%' operation that also returns the n of rotations
    rotations = 0
    while magnitude >= 100:
        rotations += 1
        magnitude -= 100
    return rotations

def turn_dial(inp,current,rotations = 0):
    direction = inp[0]
    magnitude = int(inp[1:])
    rotations += count_rotations(magnitude) 
    magnitude = magnitude % 100 # since the dial is circular, ensures the change is not more than 99


    if direction == "L":
        if current == 0:
            current = correct_count(current - magnitude) #to ensure we dont double-count when it starts on 0 and rotates left
            return current, rotations
        current = current - magnitude
        if current <= 0:
            rotations += 1 #i.e. it passed zero if the number before correcting is less than or equal to 0
        current = correct_count(current) #we can do this since magnitude <100 and we already counted rotations
    
    if direction == "R":
        current = current + magnitude
        if current > 99:
            rotations += 1 #i.e. if the number is greater than 99, it invariably passed 0 so we increase the zero counter
        current = correct_count(current) #we can do this since magnitude <100
    return current, rotations

def solution_2(input):
    current = 50
    zeros = 0
    for line in input:
        current,rotations = turn_dial(line,current)
        zeros += rotations
    return zeros

def __main__():
    input = read_file('day1_input.txt')
    sol2 = solution_2(input)
    print(f"The code for problem 2 is {sol2}")
    pass

if __name__ == "__main__":
    __main__()
