# INSTRUCTIONS
# 1. Install Python 3.7.6 in MAC operative system.
# 2. Right click on readText.py file, open with,  and then select python launcher.
# 3. Verify the console which opens after launching python.

import unittest

file_path = "inputText.txt"

def fun(filename):
    
    #Parameters:
    #   filename: longest string which is to be reversed.
    
    #Returns:
    #   large_line: longest string within the file.
    #   reversed_string: string within the file.
    
    large_line = ''
    with open(filename, 'r') as f:
        for line in f:
            if len(line) > len(large_line):
               large_line = line

    reversed_string = ''.join(reversed(large_line))
    return large_line, reversed_string

print("large text!", fun(file_path))








