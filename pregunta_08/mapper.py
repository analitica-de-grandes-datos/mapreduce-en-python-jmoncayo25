#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':

  for line in sys.stdin:

    lines = line.strip().replace('-', ' ').split(' ')

    sys.stdout.write("{}\t{}\n".format(lines[0], lines[8]))
    
