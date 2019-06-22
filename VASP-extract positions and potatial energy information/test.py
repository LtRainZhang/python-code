#!/usr/bin/env python
# coding=utf-8

'''
@author: Yingchun Zhang, modified by zhang_xiaoyu
@e-mail: yczhang@smail.nju.edu.cn
@time: 2019/6/5 11:36
@org: Nanjing University
'''

from ase import io
from ase import units

# units real in lammps: kcal/mol for energy; kcal/mol/A for force; A for length
# units in ASE: eV for energy; A for length;
kcalmol2ev = units.kcal / units.mol

#dirName = r'D:\simulationBackup\amp\reaxff-as-training-data\water\md-1/'
dirName = r'./'
lmpTrajFileName = 'XDATCAR'
lmpOutFileName = 'pot_en'
exyzFileName = 'sio2-0.7.xyz'
aseTrajFileName = 'sio2-0.7.traj'

lmpTraj = open(dirName + lmpTrajFileName, 'r')
traj = lmpTraj.read().split('Direct configuration=')[0:]    #divide the diffenrent part
lmpTraj.close()

infor = traj[0]
#print(infor[0])
hhh = infor.split('\n')
print(len(hhh))
print(hhh[3])
a, b, c = float(hhh[2].split(  )[0]), float(hhh[3].split(  )[1]), float(hhh[4].split(  )[2])
print(a, b, c)
ele1 = hhh[5].split(  )[0]
ele2 = hhh[5].split(  )[1]
print(ele1, ele2)
num_ele1 = int(hhh[6].split(  )[0])
num_ele2 = int(hhh[6].split(  )[1])
print(num_ele1, num_ele2)

#for mm, nn in enumerate(traj[0]):
#    print(nn)
#    liness = nn.split('\n')

#    a = float(liness[2].split(   )[0])
#    a, b, c = float(liness[2].split(   )[0]), float(liness[3].split(   )[1]), float(liness[4].split(   )[2])

#print(a) 
#print('frames:', len(traj))
#print(len(traj[0]))

outFile = open(dirName + lmpOutFileName, 'r')
out = outFile.readlines()
outFile.close()
#print(out[0])
#stepLineIndex = 0
#for i, line in enumerate(out):
#    if line.split()[0] == 'Step':
#        stepLineIndex = i
#out = out[stepLineIndex + 1:]
#print(out[:])
#print(out[0])
#print(out[1])

trajectory = traj[1:]
#print(trajectory[0])
#print(len(trajectory))

xyz = open(dirName + exyzFileName, 'w')
nAtoms = num_ele1 + num_ele2
for iframe, xtraj in enumerate(trajectory):
    lines = xtraj.split('\n')
#    print(lines[:])
#    print(len(lines))
#    print(lines[0])
#    nAtoms = int(lines[2])
#    a, b, c = float(lines[4].split()[1]), float(lines[5].split()[1]), float(lines[6].split()[1])
    print(nAtoms, file=xyz)
#    print(out[iframe])

    print(
        'Lattice="%5.3f 0.0 0.0 0.0 %5.3f 0.0 0.0 0.0 %5.3f" Properties=species:S:1:pos:R:3 energy=%15.8f pbc="T T T"' % (
        a, b, c, float(out[iframe])), file=xyz)

    for i in range(nAtoms):
        tmp = lines[i + 1].split()
        if i < num_ele1:
            print('%-4s %15.8f %15.8f %15.8f' % (ele1, float(tmp[0]) * a, float(tmp[1]) * b, float(tmp[2]) * c), file=xyz)
        else:
            print('%-4s %15.8f %15.8f %15.8f' % (ele2, float(tmp[0]) * a, float(tmp[1]) * b, float(tmp[2]) * c), file=xyz)

xyz.close()
#print(traj[1])

aseTrj = io.Trajectory(dirName + aseTrajFileName, 'w')
exyz = io.read(dirName + exyzFileName, index=':')
for atoms in exyz:
    atoms.set_pbc((1,1,1))
    aseTrj.write(atoms)
