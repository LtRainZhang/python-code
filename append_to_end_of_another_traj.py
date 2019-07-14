# coding=utf-8
#Append one trajectory to the end of another
from ase.io import Trajectory
t1 = Trajectory('t1.traj', 'a')
t2 = Trajectory('t2.traj')
for atoms in t2:
    t1.write(atoms)
t1.close()
