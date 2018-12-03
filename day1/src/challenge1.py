#! /usr/bin/env python3

import sys
import os

def add_to_frequency(current, value):
    return current + int(value)

def find_final_frequency(value_list):
    current = 0
    for value in value_list:
        current = add_to_frequency(current, value)
    return current

def get_data(path):
    values = []
    with open(path) as f:
        contents = f.read()
        values = contents.split("\n")
    if values[-1] == "":
        del(values[-1])
    return values

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need a path to a file to read")
        exit(-1)
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print("File doesn't exist, check the command")
    values = get_data(file_path)
    freq = find_final_frequency(values)
    print("Frequency is: ", freq)
