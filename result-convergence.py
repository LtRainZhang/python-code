'''
仅在训练能量数据时使用，使用前请修改xxx.amp文件名，其他参数根据需要自行修改，在python3 环境下执行 python result-convergence.py
author：Xiaoyu Zhang
organization:NJU
'''


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
fileName = 'sio2-log.txt'      # change fileName
file = open(dirName + fileName,'r')
eachline = file.read().split('weight duplicates:False')
maindata = eachline[1].split('\n')[6:]
#print(maindata)
c = []
for frame1, line1 in enumerate(maindata):
    if is_number(line1.split()[0]):
        c.append(line1)
print(c)
print(len(c))
listnum = []
Loss = []
EnergyRMSE = []
Energy_MaxResid = []
for frame2,line2 in enumerate(c):
    listnum.append(int(line2.split()[0]))
    Loss.append(float(line2.split()[2]))
    EnergyRMSE.append(float(line2.split()[3]))
    Energy_MaxResid.append(float(line2.split()[5]))
'''
print(listnum)
print(Loss)
print(Energy_MaxResid)
print(EnergyRMSE)
'''

figsize = 8,6
figure, ax = plt.subplots(figsize=figsize)

font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 12,
         }
#投图
#plt.plot(listnum, Loss label='Loss Function', linewidth=5.0)   #绘制折线图
plt.scatter(listnum, Loss, label='Loss Function', color='red', s=4)
plt.scatter(listnum, EnergyRMSE, label='EnergyRMSE', color='green', s=4)
plt.scatter(listnum, Energy_MaxResid, label='Energy_MaxResid', color ='blue', s=4)

#设置对数坐标
#plt.xscale('linear')
plt.yscale('log')

#设置坐标轴标题及字体大小
plt.xlabel('Loss Function call', font1)
plt.ylabel('error', font1)

#设置坐标轴范围
plt.ylim((0.00001,10.0))

#设置坐标轴字体，大小
plt.tick_params(labelsize=12)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#设置主标题名称
plt.title(" ")

#设置图例及格式
plt.legend(prop=font1)

#绘图
#plt.show()

plt.savefig('out.png', dpi=300)      #输出图片