#!/usr/bin/env python
# coding=utf-8

'''
@author: Yingchun Zhang  modified by Xiaoyu Zhang
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
lmpForceFileName = 'PosAndForce'
lmpOutFileName = 'pot_en'
exyzFileName = 'sio2-0.7.xyz'
aseTrajFileName = 'sio2-0.7.traj'

lmpTraj = open(dirName + lmpTrajFileName, 'r')
traj = lmpTraj.read().split('Direct configuration=')[0:1]    #divide the diffenrent part
lmpTraj.close()

lmpTrajAndForce = open(dirName + lmpForceFileName, 'r')
ForceAndTraj = lmpTrajAndForce.read().split('POSITION')[0:]    #divide the diffenrent part
lmpTraj.close()

infor = traj[0]
hhh = infor.split('\n')
print(len(hhh))
print(hhh[3])
ax, bx, by, cz = float(hhh[2].split(  )[0]), float(hhh[3].split(  )[0]), float(hhh[3].split(  )[1]), float(hhh[4].split(  )[2])
print(ax, bx, by, cz)
ele1 = hhh[5].split(  )[0]
ele2 = hhh[5].split(  )[1]
print(ele1, ele2)
num_ele1 = int(hhh[6].split(  )[0])
num_ele2 = int(hhh[6].split(  )[1])
print(num_ele1, num_ele2)

outFile = open(dirName + lmpOutFileName, 'r')
out = outFile.readlines()
outFile.close()

xyz = open(dirName + exyzFileName, 'w')
nAtoms = num_ele1 + num_ele2
for iframe, xtraj in enumerate(ForceAndTraj):

    while iframe < 2000 and iframe%20 == 0:
        lines = xtraj.split('\n')
        print(nAtoms, file=xyz)
        print(
            'Lattice="%5.3f 0.0 0.0 %5.3f %5.3f 0.0 0.0 0.0 %5.3f" Properties=species:S:1:pos:R:3:forces:R:3 energy=%15.8f pbc="T T T"' % (
            ax, bx, by, cz, float(out[iframe])), file=xyz)
        for i in range(nAtoms):
            tmp = lines[i + 2].split()
            if i < num_ele1:
                print('%-4s %15.8f %15.8f %15.8f %15.8f %15.8f %15.8f' % (ele1, float(tmp[0]), float(tmp[1]), float(tmp[2]),
                                                                          float(tmp[3]), float(tmp[4]), float(tmp[5])), file=xyz)
            else:
                print('%-4s %15.8f %15.8f %15.8f %15.8f %15.8f %15.8f' % (ele2, float(tmp[0]), float(tmp[1]), float(tmp[2]),
                                                                          float(tmp[3]), float(tmp[4]), float(tmp[5])), file=xyz)

    while iframe >= 2000 and iframe%20 == 0:
        lines = xtraj.split('\n')
        print(nAtoms, file=xyz)
        print(
            'Lattice="%5.3f 0.0 0.0 %5.3f %5.3f 0.0 0.0 0.0 %5.3f" Properties=species:S:1:pos:R:3:forces:R:3 energy=%15.8f pbc="T T T"' % (
            ax, bx, by, cz, float(out[iframe])), file=xyz)
        for i in range(nAtoms):
            tmp = lines[i + 2].split()
            if i < num_ele1:
                print('%-4s %15.8f %15.8f %15.8f %15.8f %15.8f %15.8f' % (ele1, float(tmp[0]), float(tmp[1]), float(tmp[2]),
                                                                          float(tmp[3]), float(tmp[4]), float(tmp[5])), file=xyz)
            else:
                print('%-4s %15.8f %15.8f %15.8f %15.8f %15.8f %15.8f' % (ele2, float(tmp[0]), float(tmp[1]), float(tmp[2]),
                                                                          float(tmp[3]), float(tmp[4]), float(tmp[5])), file=xyz)

xyz.close()

aseTrj = io.Trajectory(dirName + aseTrajFileName, 'w')
exyz = io.read(dirName + exyzFileName, index=':')
for atoms in exyz:
    atoms.set_pbc((1,1,1))
    aseTrj.write(atoms)
