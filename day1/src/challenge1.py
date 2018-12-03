#! /usr/bin/env python3

def add_to_frequency(current, value):
    return current + int(value)

def find_final_frequency(value_list):
    current = 0
    for value in value_list:
        current = add_to_frequency(current, value)
    return current

if __name__ == "__main__":
    print("Hello, world")
