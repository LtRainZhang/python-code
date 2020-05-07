import os

position = ['2.0', '2.2', '2.4', '2.6', '2.8',
            '3.0', '3.2', '3.4', '3.6', '3.8',
            '4.0', '4.2', '4.4', '4.6', '4.8',
            '5.0', '5.2', '5.4', '5.6', '5.8',
            '6.0']
tran = 4.5710E-05    #A/ps  to .a.u
for pos in position:
    path_or = 'E:/数据备份/htempkf/653_0.6/'+pos+'/REVCON'
    path_ta = 'E:/CP2K-LiCl/1273-0.6/0.6-initial/'+pos
    f_coor = '/coor_licl_1273-0.6_'+pos+'A.xyz'
    f_velo = '/velocity_licl_1273-0.6_'+pos+'A.xyz'

    fid = open(path_or, 'r')
    x = fid.readline()

    atoms = int(fid.readline().split()[2])
    print(atoms)
    cell = []
    for i in range(3):
        cell.append(fid.readline().split())
    print(cell)
    elem = []
    coor = []
    velo = []

    for i in range(atoms):
        line1 = fid.readline()
        elem.append(line1.split()[0])
        coor.append([float(i) for i in fid.readline().split()])
        velo.append([float(i)*tran for i in fid.readline().split()])
        line2 = fid.readline()
    elem[0] = 'Li'
    elem[1] = 'Cl'
    print(coor)
    print(velo)
    fid.close()
    if not os.path.exists(path_ta):
        os.makedirs(path_ta)
    path_ta_coor = path_ta + f_coor
    path_ta_velo = path_ta + f_velo

    print(path_ta_coor)

    fc = open(path_ta_coor, 'w')
    fv = open(path_ta_velo, 'w')

    fc.write('%d\n' % atoms)
    fc.write('LiCl [19.66  19.66  19.66  90 90 90] 1273-0.6 %s A\n' % pos)
    for i in range(atoms):
        fc.write('%s  %12.9f  %12.9f  %12.9f\n' % (elem[i], coor[i][0], coor[i][1], coor[i][2]))
        fv.write('     %12.9f    %12.9f    %12.9f\n' % (velo[i][0], velo[i][1], velo[i][2]))
    fc.close()
    fv.close()