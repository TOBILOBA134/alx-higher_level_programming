#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    if len(sys.argv) == 1:
        print('{}'.format(0))
    elif len(sys.argv) > 1:
        for i in range(int(sys.argv)):
            total += i
            print('{}'.format(total))
