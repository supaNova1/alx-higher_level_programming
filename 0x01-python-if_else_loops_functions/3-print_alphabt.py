#!/usr/bin/python3
# Loop through the ASCII values of lowercase letters 'a' to 'z'
for i in range(ord('a'), ord('z') + 1):
    if i != 'q' and i != 'e':
        print("{:c}".format(i), end='')
