#####################
filename = 'CONFIG'
title = 'lif'
TandP = '523-0.3'
distance = '6.0'
#######################
outCoorName = 'coor_'+title+'_'+TandP+'_'+distance+'A.xyz'
outVeloName = 'velocity_'+title+'_'+TandP+'_'+distance+'A.xyz'
fp = open(filename, 'r')
line = fp.readline()
num = int(fp.readline().strip().split()[2])
print(num)
ele = []
coor = [[0]*3 for i in range(num)]
velo = [[0]*3 for i in range(num)]
cell = []
tran = 4.5710E-05    #A/ps  to .a.u
for i in range(3):
    line = fp.readline().strip().split()
    cell.append(float(line[i]))
print(cell)
for i in range(num):
    ele.append(fp.readline().strip().split()[0])
    coor[i][0:2] = map(float, fp.readline().strip().split())
    velo[i][0:2] = map(float, fp.readline().strip().split())
    fp.readline()
fp.close()
for i in range(num):
    velo[i][0] *= tran
    velo[i][1] *= tran
    velo[i][2] *= tran

print(coor)
outcoor = open(outCoorName, 'w')
print('%d'% num, file=outcoor)
print('%s [%f %f %f 90 90 90] %s %s A' % (title, cell[0], cell[1], cell[2], TandP, distance), file=outcoor)
for i in range(num):
    print('%s    %12.9f    %12.9f    %12.9f' % (ele[i], coor[i][0], coor[i][1], coor[i][2]), file= outcoor)
outcoor.close()
outvelo = open(outVeloName, 'w')
for i in range(num):
    print('   %12.9f    %12.9f    %12.9f' % (velo[i][0], velo[i][1], velo[i][2]), file= outvelo)
outcoor.close()