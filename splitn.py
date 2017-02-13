import sys

input = open(sys.argv[1])
output = open(sys.argv[2], 'w')
output.write('-------\n' + 'Forth one' + '\n')
while True:
        line = input.readline()
        if len(line) == 0:
                break
        elif len(line) > 1:
                output.write(line)
input.close()
output.close()