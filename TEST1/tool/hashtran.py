import numpy as np
import shelve

inputfile = raw_input("Enter the raw feature file: ")
print('Auto load ../data/newdic.dat ....')

rawfile = shelve.open(inputfile)
rawdata = rawfile['res']
dictfile = shelve.open('../data/newdic.dat')
dict = dictfile['DICT']

res = {}

for i in rawdata:
    tmp = []
    if len(rawdata[i]) == 7:
        for x in rawdata[i]:
            if x in dict:
                tmp.append(dict[x])
                res[i] = np.vstack(tuple(tmp))
    if len(rawdata[i]) < 7:
        for x in rawdata[i]:
            if x in dict:
                tmp.append(dict[x])
        for t in range(7 - len(rawdata[i])):
            tmp.append(dict['unknown'])
        res[i] = np.vstack(tuple(tmp))

savefile = raw_input(
    'Translate have finish,choose a new file to save the result: ')
temp = shelve.open(savefile)
temp['res'] = res
temp.close()