import numpy as np
from astropy.table import Table
from astropy.io import ascii
from astropy.io import fits

def writeTables():
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)
    data = Table([x, y], names=['x', 'sin x'])
    ascii.write(data, 'sinxTable.txt', format='commented_header')
    data_in = ascii.read('sinxTable.txt')
    print(data_in)
    
def main():
    writeTables()
    
if __name__ == '__main__':
    main()