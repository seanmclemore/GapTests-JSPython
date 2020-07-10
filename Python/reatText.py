# INSTRUCTIONS
# 1. Install Python 3.7.6 in MAC operative system.
# 2. Right click on readText.py file, open with,  and then select python launcher.
# 3. Verify the console which opens after launching python.

large_line = ''
large_line_len = 0
filename = "inputText.txt"

with open(filename, 'r') as f:
    for line in f:
        if len(line) > len(large_line):
            large_line = line

print large_line

reversedstring=''.join(reversed(large_line))
print reversedstring
