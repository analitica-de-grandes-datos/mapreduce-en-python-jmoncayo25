#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    replace1 = [line.replace('\n', '') for line in sys.stdin]
    replace2 = [line.split('   ') for line  in replace1]
    l1 = [replace2[i][0] for i in range(len(replace2))]
    v1 = [replace2[i][2] for i in range(len(replace2))]

    for i in range(len(l1)):
        sys.stdout.write("{}\t{}\n".format(l1[i], v1[i]))
