#!/usr/bin/env python
# coding=utf-8

'''
@author: Yingchun Zhang, modified by Xiaoyu Zhang
@e-mail: yczhang@smail.nju.edu.cn
@time: 2019/6/5 11:36
@org: Nanjing University
first 2000 sampled every 2 and last 2000 sampled every 2
'''
import numpy as np
from ase import io
from ase import units

# units real in lammps: kcal/mol for energy; kcal/mol/A for force; A for length
# units in ASE: eV for energy; A for length;
kcalmol2ev = units.kcal / units.mol

#dirName = r'D:\simulationBackup\amp\reaxff-as-training-data\water\md-1/'
dirName = r'./'
lmpTrajFileName = 'XDATCAR'
lmpOutFileName = 'pot_en'
exyzFileName = 'sio2-alfa_quart_298_ori.xyz'
aseTrajFileName = 'sio2-alfa_quart_298_ori.traj'

lmpTraj = open(dirName + lmpTrajFileName, 'r')
traj = lmpTraj.read().split('Direct configuration=')[0:]    #divide the diffenrent part
lmpTraj.close()

infor = traj[0]
hhh = infor.split('\n')
print(len(hhh))
print(hhh[3])
ax, bx, by, cz = float(hhh[2].split(  )[0]), float(hhh[3].split( )[0]), float(hhh[3].split(  )[1]), float(hhh[4].split(  )[2])
print(ax, bx, by, cz)
lattice_vector = np.array([[ax,0,0],[bx,by,0],[0,0,cz]])


ele1 = hhh[5].split(  )[0]
ele2 = hhh[5].split(  )[1]
print(ele1, ele2)
num_ele1 = int(hhh[6].split(  )[0])
num_ele2 = int(hhh[6].split(  )[1])
print(num_ele1, num_ele2)

outFile = open(dirName + lmpOutFileName, 'r')
out = outFile.readlines()
outFile.close()

trajectory = traj[1:]

xyz = open(dirName + exyzFileName, 'w')
nAtoms = num_ele1 + num_ele2

first_configure = open(dirName + '1.xyz', 'w')
for iframe, xtraj in enumerate(trajectory):
    lines = xtraj.split('\n')
    if iframe == 0:
        print(nAtoms, file=first_configure)
        print(
            'Lattice="%5.3f 0.0 0.0 %5.3f %5.3f 0.0 0.0 0.0 %5.3f" Properties=species:S:1:pos:R:3 energy=%15.8f pbc="T T T"' % (
                ax, bx, by, cz, float(out[iframe])), file=xyz)
        for i in range(nAtoms):
            tmp = lines[i + 1].split()
            u = float(tmp[0])
            v = float(tmp[1])
            w = float(tmp[2])
            frac_coor = np.array([[u], [v], [w]])
            cart_coor = (lattice_vector.T).dot(frac_coor)
            if i < num_ele1:
                print('%-4s %15.8f %15.8f %15.8f' % (ele1, cart_coor[0], cart_coor[1], cart_coor[2]), file=xyz)
            else:
                print('%-4s %15.8f %15.8f %15.8f' % (ele2, cart_coor[0], cart_coor[1], cart_coor[2]), file=xyz)

    while iframe < 2000  and iframe%2 == 0:
        print(nAtoms, file=xyz)
        print(
            'Lattice="%5.3f 0.0 0.0 %5.3f %5.3f 0.0 0.0 0.0 %5.3f" Properties=species:S:1:pos:R:3 energy=%15.8f pbc="T T T"' % (
            ax, bx, by, cz, float(out[iframe])), file=xyz)
        for i in range(nAtoms):
            tmp = lines[i + 1].split()
            u = float(tmp[0])
            v = float(tmp[1])
            w = float(tmp[2])
            frac_coor = np.array([[u],[v],[w]])
            cart_coor = (lattice_vector.T).dot(frac_coor)
            if i < num_ele1:
                print('%-4s %15.8f %15.8f %15.8f' % (ele1, cart_coor[0], cart_coor[1], cart_coor[2]), file=xyz)
            else:
                print('%-4s %15.8f %15.8f %15.8f' % (ele2, cart_coor[0], cart_coor[1], cart_coor[2]), file=xyz)
        break

    while iframe >= 2000 and iframe%2 == 0:
        print(nAtoms, file=xyz)
        print(
            'Lattice="%5.3f 0.0 0.0 %5.3f %5.3f 0.0 0.0 0.0 %5.3f" Properties=species:S:1:pos:R:3 energy=%15.8f pbc="T T T"' % (
            ax, bx, by, cz, float(out[iframe])), file=xyz)
        for i in range(nAtoms):
            tmp = lines[i + 1].split()
            u = float(tmp[0])
            v = float(tmp[1])
            w = float(tmp[2])
            frac_coor = np.array([[u], [v], [w]])
            cart_coor = (lattice_vector.T).dot(frac_coor)
            if i < num_ele1:
                print('%-4s %15.8f %15.8f %15.8f' % (ele1, cart_coor[0], cart_coor[1], cart_coor[2]), file=xyz)
            else:
                print('%-4s %15.8f %15.8f %15.8f' % (ele2, cart_coor[0], cart_coor[1], cart_coor[2]), file=xyz)
        break 
xyz.close()

aseTrj = io.Trajectory(dirName + aseTrajFileName, 'w')
exyz = io.read(dirName + exyzFileName, index=':')
for atoms in exyz:
    atoms.set_pbc((1,1,1))
    aseTrj.write(atoms)
