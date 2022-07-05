#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator 

if __name__ == '__main__':
    
    lista = {}

    for line in sys.stdin:
       line = line.strip()
       letter, value = line.split('\t')
       
       if letter in lista:
           lista[letter].append(float(value))
       else: 
           lista[letter] = []
           lista[letter].append(float(value))
           
    for letter in lista.keys():
        sum_letter = sum(lista[letter])
        mean_letter = sum(lista[letter])/ len(lista[letter])
        print('%s\t%s\t%s'% (letter, sum_letter, mean_letter)) #Impresión
