#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:

    data = "\t".join(row.split(",")[3:5])

    sys.stdout.write('{}\n'.format(data))
