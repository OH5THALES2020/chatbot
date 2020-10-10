'''
Created on 10 oct. 2020

@author: carl
'''

import csv
filename='./data/annuaire_maree_BREST_2020.csv'
reader=csv.reader(filename)
with open(filename, 'r') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
     for row in spamreader:
        print(', '.join(row))
