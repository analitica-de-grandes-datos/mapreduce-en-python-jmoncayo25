#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    values = []
    
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            values.append(val)
        else:

            if curkey is not None:
                
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, sum(values), sum(values)/len(values)))
                values = []

            curkey = key
            values.append(val)
