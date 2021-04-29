import os
import xlrd
import pandas as pd
import tkinter.filedialog
from tkinter import *
from tkinter import messagebox

sequence = list( map( lambda x: chr( x ), range( ord( 'A' ), ord( 'Z' ) + 1 ) ) )
##-----字母转数字（python实现 1-26=A-Z, then AA-AZ）
def ten2TwentySix(num):
    L = []
    num=num-1;  #实现从1对应A
    if num > 25:
        while True:
            d = int( num / 26 )
            remainder = num % 26
            if d <= 25:
                L.insert( 0, sequence[remainder] )
                L.insert( 0, sequence[d - 1] )
                break
            else:
                L.insert( 0, sequence[remainder] )
                num = d - 1
    else:
        L.append( sequence[num] )
    return "".join( L )


def twentySix2Ten(s):
    l = len( s )
    sum = 1    #实现从A对应1
    if l > 1:
        for i in range( l - 1 ):
            index = sequence.index( s[i] )
            # print( index )
            num = pow( 26, l - 1 ) * (index + 1)
            # print( num )
            l = l - 1
            sum = sum + num
        sum = sum + sequence.index( s[-1] )
    else:
        sum = sum + sequence.index( s[-1] )
    return sum


def getInput(title, message):
    def return_callback(event):
        print('quit...')
        root.quit()

    def close_callback():
        messagebox.showinfo('message', 'no click...')

    root = Tk(className=title)
    root.wm_attributes('-topmost', 1)
    screenwidth, screenheight = root.maxsize()
    width = 500
    height = 200
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)
    root.resizable(0, 0)
    lable = Label(root, height=2)
    lable['text'] = message
    lable.pack()
    entry = Entry(root)
    entry.bind('<Return>', return_callback)
    entry.pack()
    entry.focus_set()
    root.protocol("WM_DELETE_WINDOW", close_callback)
    root.mainloop()
    str = entry.get()
    root.destroy()
    return str

def MineralSort(target_values):
    mineral2num = dict()
    num2mineral = dict()
    res = dict()
    numMineralType = 0

    for item in target_values:
        if item.strip() == "":
            continue
        line = item.strip().split(';')
        if len(line) == 1:
            continue
        line.sort()
        for each in line:
            if each not in mineral2num:
                numMineralType += 1
                mineral2num[each] = numMineralType
                num2mineral[numMineralType] = each
        length = len(line)
        for i in range(length - 1):
            for j in range(i + 1, length):
                temp = str(mineral2num[line[i]]) + '-' + str(mineral2num[line[j]])
                if temp not in res:
                    res[temp] = 1
                else:
                    res[temp] += 1
    result = dict()
    for key in res.keys():
        a, b = list(map(int, key.split('-')))
        temp = num2mineral[a] + '&' + num2mineral[b]
        result[temp] = res[key]
    return result

if __name__ == '__main__':
    # cur_path = os.path.abspath('.')
    # inputFile = "中国矿床文献整合表.xlsx"

    # inPath = os.path.join(cur_path, inputFile)
    # outPath = os.path.join(cur_path, outputFile)

    inPath = tkinter.filedialog.askopenfilename()
    directory = "/".join(inPath.split('/')[:-1])
    # outputFile = "result2.xlsx"
    # outPath = os.path.join(dictory, outputFile)
    # column = "W,X"       # 将需要处理的列用逗号隔开，比如“W,X"
    column = getInput("输入框", "请输入需要处理的列名，并用英文逗号隔开，不要有空格：")
    column = column.replace('，',',').upper()
    title = dict()
    workBook = xlrd.open_workbook(inPath)
    sheet1_content = workBook.sheet_by_name('sheet')    # 如果sheet名改变，请修改

    columns = column.split(',')
    finalResult = dict()
    for target in columns:
        num_target = twentySix2Ten(target)-1

        target_values = sheet1_content.col_values(num_target)   # 不包含第一行
        title[target] = target_values[0]
        target_values = target_values[1:]
        finalResult[target] = MineralSort(target_values)

    # init = pd.DataFrame([])

    # for key in finalResult:
    #     temp = finalResult[key]
    #     a = pd.DataFrame(temp.keys())
    #     b = pd.DataFrame(temp.values())
    #     name_columns.append(key + '列 ' + title[key])
    #     name_columns.append("数量")
    #     init = pd.concat([init, a], axis=1)
    #     init = pd.concat([init, b], axis=1)
    # init = init.fillna('')
    # init.columns = name_columns
    # writer = pd.ExcelWriter(outPath)
    # init.to_excel(writer)
    # writer.save()

    for key in finalResult:
        temp = finalResult[key]
        tempList = []
        for k,v in temp.items():
            tempList.append(k.split('&')+[v])
        tempList.sort(key=lambda x:(x[0],x[1]))
        # print(tempList)
        # print(pd.DataFrame(tempList))
        sortDic = dict()
        count = 0
        for item in tempList:
            if item[0] not in sortDic:
                count += 1
                sortDic[item[0]] = count

        for item in tempList:
            if item[1] not in sortDic:
                count += 1
                sortDic[item[1]] = count

        countList = []
        print(sortDic)
        statDic = dict()
        for item in tempList:
            a, b, c = item[0], item[1], item[2]
            statDic[a] = statDic.get(a, 0) + c
            statDic[b] = statDic.get(b, 0) + c

            a, b = sortDic[a], sortDic[b]
            countList.append([a, b])


        df1 = pd.concat([pd.DataFrame(countList), pd.DataFrame(tempList)], axis=1)
        statList = []
        for k in sortDic.keys():
            statList.append([sortDic[k], k, statDic[k]])
        statList.sort(key=lambda x:x[0])

        df2 = pd.DataFrame(statList)
        # print(statList)
        
        # save step

        outputFile1 = key + '_'+ title[key] + "_test.xlsx"
        outputFile2 = key + '_'+ title[key] + "_testlink.xlsx"
        outPath1 = os.path.join(directory, outputFile1)
        outPath2 = os.path.join(directory, outputFile2)

        name_columns = ['source_id', 'target_id', 'Source', 'Target', 'Amount']
        df1 = df1.fillna('')
        df1.columns = name_columns
        writer = pd.ExcelWriter(outPath1)
        df1.to_excel(writer)
        writer.save()

        name_columns = ['id', 'mineral', 'Total']
        df2 = df2.fillna('')
        df2.columns = name_columns
        writer = pd.ExcelWriter(outPath2)
        df2.to_excel(writer)
        writer.save()





        # sortDic = dict()
        # num = 0
        # for item in a:
        #     x = item.split('&')[0]
        #     if x not in sortDic:
        #         num += 1
        #         sortDic[x] = num
        # for item in a:
        #     x = item.split('&')[1]
        #     if x not in sortDic:
        #         num += 1
        #         sortDic[x] = num














