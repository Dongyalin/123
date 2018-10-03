#! python3

def split2Q(inputStr):
    #将设备上抓到了报文分解成一个一个独立的
    #放回的是一个字典，key：第几个包；value：具体Q窗
    res = {}

    data1 = inputStr.split('(')

    for data1_item in data1:
        if(len(data1_item)):
            data2 = data1_item.split('/64)\n')

            res[data2[0]] = data2[1]

    return res
