import os
import numpy as np
import time
import pandas as pd
jishi = time.time()

path = "E:\\test\\temp"
inputfile = "ly2w_new.xyz"
outfile = "msd-system.csv"

limit = 500      #设定最大采样数

inpath = os.path.join(path, inputfile)
outpath = os.path.join(path, outfile)
species = dict()
with open(inpath, 'r') as fo:
    x = fo.readlines()
    num_atoms = int(x[0].strip())
    frame = len(x)//(num_atoms+2)
    arr = []
    for i in range(frame):
        temp = dict()
        for j in range(i*(num_atoms+2)+2, (i+1)*(num_atoms+2)):
            line = x[j].strip().split()
            if line[0] not in species:
                species[line[0]]  = []
            if line[0] not in temp:
                temp[line[0]] = []

            a = float(line[1])
            b = float(line[2])
            c = float(line[3])
            temp[line[0]].append([a,b,c])
        for key in temp.keys():
            species[key].append(temp[key])

print(species.keys())
res = dict()
for spe in species.keys():
    if spe not in res:
        res[spe] = []
    arr = np.array(species[spe])
    task = []
    for i in range(1, frame-limit):
        start = arr[:limit]
        end = arr[i:i+limit]
        row = len(start)
        col = len(start[0])
        cha = np.sum(pow((end - start), 2)) / (row*col)
        task.append(cha)
    res[spe] = task
    print(spe)

header = list(res.keys())
datas = pd.DataFrame(list(res.values())).T
datas.columns = header
datas.to_csv(outpath, sep='\t', index=None, header=True, encoding='utf_8_sig')

print(time.time()-jishi)




