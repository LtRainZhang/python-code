#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
import numpy as np
dirName = r'./'
fileName = 'test.dat'
file = open(dirName + fileName,'r')
eachline = file.read().split('\n')
while '' in eachline:
    eachline.remove('')
number = len(eachline)
listnum = range(1, number+1, 1)
print(number)
print(listnum)
c1 = []
c2 = []
for iframe,line in enumerate(eachline):
    c1.append(float(line.split()[0]))
    c2.append(float(line.split()[1]))
c1 =np.array(c1)
c2 =np.array(c2)
print(len(c1))
c3 = (c1 - c2)*96.487

figsize = 8,6
figure, ax = plt.subplots(figsize=figsize)

font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 12,
         }
#plt.plot(listnum, Loss label='Loss Function', linewidth=5.0)
#plt.scatter(listnum, c1, label='test_energy', color='red', marker='o', s=4)
#plt.scatter(listnum, c2, label='nnp_energy', color='green', marker='*', s=3)
plt.scatter(listnum, c3, label='test-nnp', color='green', marker='*', s=4)
#plt.xscale('linear')
plt.yscale('linear')

plt.xlabel('number', font1)
plt.ylabel('energy', font1)

#plt.ylim((0.00001,10.0))

plt.tick_params(labelsize=12)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

plt.title(" ")

plt.legend(prop=font1)

#plt.show()

plt.savefig('out_deviation.png', dpi=600)

