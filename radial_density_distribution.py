#coding=utf-8
import numpy as np
import math

def getlen(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    z1 = p1[2]
    x2 = p2[0]
    y2 = p2[1]
    z2 = p2[2]
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return distance


dirname = r'./'
filename = 'HISTORY'
file = open(dirname + filename, 'r')
traj = file.read().split('timestep')[0:]
pro = traj[0].split('\n')
while '' in pro:
    pro.remove('')

pro = pro[1].split()
atom_num = int(pro[2])
print(atom_num)


traj = traj[500:]
file.close()
print(len(traj))
#canshu


def isDigit(x):
    try:
        if x == 'O' or x == 'H' or x =='Na' or x == 'F' or x =='K':
            return False
        else:

            return True
    except ValueError:
        return False

jishu = 0
density = []
densities = []
elements = []
a = 19.65833264
num = 0

for infor in traj:
    num = num + 1

    if num % 10 == 0:
        print(num)

    hhh =infor.split('\n')

    coorlist = np.zeros(shape=(atom_num, 4))

    while '' in hhh:
        hhh.remove('')
    hhh = hhh[4:]
    nn = 0
    mm = 0
    for i,xtraj in enumerate(hhh):
        xtraja = xtraj.split()
        while '' in xtraja:
            xtraja.remove('')

        x = xtraja[0]
        a = isDigit(xtraja[0])
        if not(a):
            elements.append(x)
            nn = nn + 1
        else:
            coorlist[mm][0] = float(xtraja[0])
            coorlist[mm][1] = float(xtraja[1])
            coorlist[mm][2] = float(xtraja[2])

            if elements[mm] == 'Na':
                coorlist[mm][3] = 1
            elif elements[mm] == 'F':
                coorlist[mm][3] = 2
            elif elements[mm] == 'O':
                coorlist[mm][3] = 3
            else:                           # element  = 'H'
                coorlist[mm][3] = 4
            mm = mm + 1
    aaa = coorlist[:, 0:3] / 19.65833264
    bbb = coorlist[:, 3:4]
    finele = np.concatenate((aaa, bbb), axis=1)

    j1 = len(finele)

    tot_j1 = 0
    tot_j1 = tot_j1 + j1
    tot_ele = finele
    linshi = np.concatenate((np.ones(shape=(j1,1)), np.zeros(shape=(j1,1)), np.zeros(shape=(j1,1)), np.zeros(shape=(j1,1))), axis=1)

    tot_ele = np.concatenate((tot_ele, (finele + linshi)), axis=0)
    tot_j1 = tot_j1 + j1
    tot_ele = np.concatenate((tot_ele, (finele - linshi)), axis=0)
    tot_j1 = tot_j1 + j1
    j1 = j1 * 3
    tot_y = tot_ele



    linshi = np.concatenate((np.zeros(shape=(j1,1)), np.ones(shape=(j1,1)), np.zeros(shape=(j1,1)), np.zeros(shape=(j1,1))), axis=1)
    tot_ele = np.concatenate((tot_ele, (tot_y + linshi)), axis=0)
    tot_j1 = tot_j1 + j1
    tot_ele = np.concatenate((tot_ele, (tot_y - linshi)), axis=0)
    tot_j1 = tot_j1 + j1
    tot_z = tot_ele
    j1 = j1 * 3





    linshi = np.concatenate((np.zeros(shape=(j1,1)), np.zeros(shape=(j1,1)), np.ones(shape=(j1,1)), np.zeros(shape=(j1,1))), axis=1)

    tot_ele = np.concatenate((tot_ele, (tot_z + linshi)), axis=0)

    tot_j1 = tot_j1 + j1
    tot_ele = np.concatenate((tot_ele, (tot_z - linshi)), axis=0)
    tot_j1 = tot_j1 + j1



    aaaa = tot_ele[:, 0:3] * 19.65833264
    bbbb = tot_ele[:, 3:4]
    zuizhong = np.concatenate((aaaa, bbbb), axis=1)


    for i in range(5):
        if zuizhong[i,3] == 1:
            target_ele = zuizhong[i,:]   # Na
            break
    for r in np.linspace(0.05,8,160):

        for element in zuizhong:
            if element[3] == 3:
                ele_select = element
                distance = getlen(target_ele, ele_select)
                if distance < r:
                    jishu = jishu + 1
        density.append((jishu * 18/ (6.022 * math.pow(10, 23)) / (4 / 3 * 3.1415926 * (r * math.pow(10, -8))**3)))

        jishu = 0
    densities.append(density)
    density = []

average_density = np.sum(densities, axis=0) / len(densities)



print(density)
print(len(density))


print(np.linspace(0.05,8,160))
print(densities)
print(average_density)
print(len(average_density))

total_densisties = open(dirname + 'densities_tot.data', 'w')
fr = 0
for i in np.linspace(0.05,8,160):
    total_densisties.write(' %12.8f ' % i)


for iframe in densities:
    fr = fr + 0.05
    total_densisties.write('\n')
    for frame in iframe:
        total_densisties.write(' %12.8f ' % frame)
total_densisties.close()


out_density = open(dirname + 'density.data','w')
for i in average_density:
    print('%15.8f' % i, file= out_density)

out_density.close()
'''
first_figure = open(dirname + '1.xyz', 'w')
    print(j1*3, file = first_figure)
    print('atoms', file = first_figure)
    for atom in zuizhong:
        if atom[3] == 1:
            print('Na %15.8f %15.8f %15.8f' % (atom[0], atom[1], atom[2]), file = first_figure)
        elif atom[3] == 2:
            print('F %15.8f %15.8f %15.8f' % (atom[0], atom[1], atom[2]), file=first_figure)
        elif atom[3] == 3:
            print('O %15.8f %15.8f %15.8f' % (atom[0], atom[1], atom[2]), file=first_figure)
        else:
            print('H %15.8f %15.8f %15.8f' % (atom[0], atom[1], atom[2]), file=first_figure)
'''





