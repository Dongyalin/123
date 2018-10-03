#! python3

from combation import *
from splitQ import *

import re

import combare

data = r'''(1/64)
q0w  505bc2df 5adbd8c8 e9828959 08004500  
q8w  00280000 40003506 dac9dfcb c80bc0a8  
q16w 028701bb 1a339aca c91e0000 00005004   
q24w 0000c502 0000**** ******** ********           

(2/64)
22222222 22222222 22222222 22222222
22222222 22222222 22222222 22222222
22222222 22222222 22222222 22222222
22222222 22222222 22222222 22222222

(3/64)
q0w  d8c8e982 8959505b c2df5adb 08004500
q8w  00287340 40004006 c3f9c0a8 02876a75
q16w d5f13034 01bbb42a 138cf630 35125010
q24w 03fd8358 0000**** ******** ********

'''
data1 = r'''
22222222 22222222 22222222 22222222s
22222222 22222222 22222222 22222222
22222222 22222222 22222222 22222222
22222222 22222222 22222222 22222222
'''

print('data: \n' + data)
print(' ')

res = split2Q(data)
print(res)


'''
res = {}

data1 = data.split('(')
for data1_item in data1:
    if len(data1_item):
        data2 = data1_item.split('/64)\n')
        
        res[data2[0]] = data2[1]
        
res11 =   qwindows2ste(res['1'])   

'''

res1 = qwindows2ste(res['1'])
print(res1)



tmpp = combare.Eth()

tmpp.setDmac(r'505bc2df5a')
tmpp.setEthNeType(r'0800')

tmpp.combationETH()
res11 = tmpp.isWantedPacket(res1)
print(res11)


tmpip4 = combare.IP4()
tmpip4.setSIP('c0a8028711')

tmpip4.combationIP4()

srcstr11 = qwindows2ste(res['3'])
print(srcstr11)
res12 = tmpip4.isWantedPacket(srcstr11)
print(res12)

tmpip4oEth = combare.IP4oETH()

tmpip4oEth.setSIP('c0a8028711')

tmpip4oEth.combationIP4oEth()
res13 = tmpip4oEth.isWantedPacket(srcstr11)
print(res13)

