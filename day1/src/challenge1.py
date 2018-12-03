#! /usr/bin/env python3

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
    print("Hello, world")
