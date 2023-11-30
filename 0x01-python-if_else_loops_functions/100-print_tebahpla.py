#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    print("{:c}".format(i), end="" if i % 2 == 0 or (i >= ord('a') and i <= ord('z')) else "")
print()
