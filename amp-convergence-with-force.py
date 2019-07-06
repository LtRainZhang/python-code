#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
# judge whether number or not
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


dirName = r'./'
fileName = 'sio2-log-2.txt'
file = open(dirName + fileName,'r')
eachline = file.read().split('weight duplicates:False')
maindata = eachline[1].split('\n')[:]

while '' in maindata:
    maindata.remove('')

c = []
for frame1, line1 in enumerate(maindata):
    if is_number(line1.split()[0]):
        c.append(line1)
print(c[0])
listnum = []
Loss = []
EnergyRMSE = []
Energy_MaxResid = []
ForceRMSE = []
Force_MaxResid = []

for frame2,line2 in enumerate(c):
    listnum.append(int(line2.split()[0]))
    Loss.append(float(line2.split()[2]))
    EnergyRMSE.append(float(line2.split()[3]))
    Energy_MaxResid.append(float(line2.split()[5]))
    ForceRMSE.append(float(line2.split()[7]))
    Force_MaxResid.append(float(line2.split()[9]))


print(listnum)
print(Loss)
print(Energy_MaxResid)
print(EnergyRMSE)
print(Force_MaxResid)
print(ForceRMSE)



figsize = 8,6
figure, ax = plt.subplots(figsize=figsize)

font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 12,
         }
#plt.plot(listnum, Loss label='Loss Function', linewidth=5.0)
plt.scatter(listnum, Loss, label='Loss Function', color='red', s=4)
plt.scatter(listnum, EnergyRMSE, label='EnergyRMSE', color='green', s=4)
plt.scatter(listnum, Energy_MaxResid, label='Energy_MaxResid', color ='blue', s=4)
plt.scatter(listnum, ForceRMSE, label='ForceRMSE', color='yellow', s=4)
plt.scatter(listnum, Force_MaxResid, label='Force_MaxResid', color ='purple', s=4)

#plt.xscale('linear')
plt.yscale('log')

plt.xlabel('Loss Function call', font1)
plt.ylabel('error', font1)

plt.ylim((0.001,100.0))

plt.tick_params(labelsize=12)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

plt.title(" ")

plt.legend(prop=font1)

#plt.show()

plt.savefig('out2.png', dpi=300)
