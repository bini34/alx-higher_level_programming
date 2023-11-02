#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    sum = 0
    if count == 0:
        print("0")
    else:
        for i in range(count):
            sum += int(sys.argv[i + 1])
        print(sum)
