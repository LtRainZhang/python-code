# coding=utf-8

'''
author: Yingchun Zhang
organization:Nanjing University
'''

from ase import io
from amp import Amp
from amp.descriptor.gaussian import Gaussian
from amp.model.neuralnetwork import NeuralNetwork
from amp.model import LossFunction

test_images = io.read('last_ten_percent_for_comparasion.traj', index=':')
test_energy = [image.get_total_energy() for image in test_images]
calc = Amp.load('sio2-checkpoint.amp', cores=8)   # 'sio2-checkpoint.amp'
nnp_energy = [calc.get_potential_energy(image) for image in test_images]
x = len(test_images)
testfile = open('test.dat','w')
for i in range(x):
    print('%15.8f %15.8f'%(test_energy[i], nnp_energy[i]), file=testfile)
testfile.close()


#dirName = r'D:\simulationBackup\amp\randomStructures/'
#initialStructure = '64w-equied.xyz'
#initialTrj = '2000-trj.xyz'
#x = io.read(dirName + initialStructure, format='xyz'
