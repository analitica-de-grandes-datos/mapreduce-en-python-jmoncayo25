#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    replace=[]

    for line in sys.stdin:

        c1, c2, c3 = line.split(",")
        c3 = int(c3)
        aux = (c1, c2, c3)
        replace.append(aux)

    replace2 = sorted(sorted(replace, key = lambda item: item[2]), key = lambda item: item[0])

    for line in replace2:
        sys.stdout.write("{}   {}   {}\n".format(line[0], line[1], line[2]))
