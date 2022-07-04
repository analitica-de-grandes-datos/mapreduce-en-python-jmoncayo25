#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    dicc = {}

    for line in sys.stdin:
        key,val = line.split('\t')
        val = int(val)
        
        if key not in dicc.keys():
            dicc[key] = val
            
        else:
            if dicc[key] < val:
                dicc[key] = val
            else:
                pass
    for key, val in dicc.items():
        sys.stdout.write('{}\t{}\n'.format(key, val))
