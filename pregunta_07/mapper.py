#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    replace1 = [line.replace('\n', '') for line in sys.stdin]
    replace2 = [line.split('   ') for line  in replace1]
    c1 = [replace2[i][0] for i in range(len(replace2))]
    c2 = [replace2[i][1] for i in range(len(replace2))]
    c3 = [replace2[i][2] for i in range(len(replace2))]

    for i in range(len(c1)):

        sys.stdout.write("{},{},{}\n".format(c1[i], c2[i], c3[i]))
        
