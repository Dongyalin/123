#!python3

__illChar = '*'

def __isPacket(dataStr):
    #检验是不是报文内容
    if dataStr.isalpha() == False :
        if(len(dataStr) == 0):
            return False

    if(dataStr[0] == 'q') or (dataStr[0] == 'p'):
        return False

    return True

def __rmNotPacket(inputStr):

    outStr = ''

    for item in inputStr:
        isLowerAphPacket = ((item >= 'a') and (item <= 'f'))
        isUpperAphPacket = ((item >= 'A') and (item <= 'F'))
        if (item.isdecimal()) or isLowerAphPacket or isUpperAphPacket :
            outStr = outStr + item

    return outStr



def qwindows2ste(qwdws):
    #将设备上Q窗报文转换为字符串

    data1 = qwdws.split('\n')
    res = []

    for item in data1:
        res1 = item.strip()
        res1 = res1.split(' ')#将每行数据以空格进行分割
        for res_item in res1:
            new_data = res_item.strip(' ')#去除分割之后字符串两端的空格
            if __isPacket(new_data) == True:
                res.append(new_data)
  
    res_str = ''.join(res)
    res_str = res_str.rstrip(__illChar)

    res_str = __rmNotPacket(res_str)

    return res_str
    
