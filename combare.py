#! python3

import re

'''

class name: rebase
class function: 正则匹配的基础类

'''
class rebase():
    # 正则匹配的基础类
    reStr = ''
    def __init__(self):
       pass
        

    def constructionRe(self, Str):
        self.reStr = Str

    def changeLen(self, srcStr, strlen):
        if(len(srcStr) == strlen):
            return srcStr
        elif (len(srcStr) > strlen):
            return srcStr[:strlen]
        else:
            reStr = srcStr
            reStr = reStr + '\\w{'
            reStr = reStr + str(strlen - len(srcStr))
            reStr = reStr + '}'
            return reStr
            
        

    def isWantedPacket(self, srcStr):
        print(self.reStr)
        self.ReStr = re.compile(self.reStr,re.I)
        mo = self.ReStr.search(srcStr)

        res = (mo != None)

        return res

'''

class name: Eth
class function: 以太报文格式

'''
class Eth(rebase):
    #正则匹配的ETH类
    ETHdict ={}
    def __init__(self):
        super(Eth,self).__init__()
        
        self.ETHdict['Dmac'] = '\\w{12}'
        self.ETHdict['Smac'] = '\\w{12}'
        self.ETHdict['anyETH'] = '\\w{0,16}'
        self.ETHdict['ETHNTYpe'] = '\\w{4}'
        self.ETHdict['playload'] = '.*'

    def setDmac(self,Dmac):
        tmp = self.changeLen(Dmac, 12)
        self.ETHdict['Dmac'] =tmp

    def setSmac(self, Smac):
        tmp = self.changeLen(Smac, 12)
        self.ETHdict['Smac'] = Smac

    def setEthNeType(self, ENT):
        tmp = self.changeLen(ENT, 12)
        self.ETHdict['ETHNTYpe'] = ENT

    def setETHplayLoad(self, playload):
        self.ETHdict['playload'] = playload

    '''
    def settag1(self, tag1):
        self.tag1 = tag1

    def settag2(self, tag2):
        self.tag2 = tag2
    '''
    def combationETH(self):
        self.reStr = self.reStr + self.ETHdict['Dmac']
         
        self.reStr = self.reStr + self.ETHdict['Smac']        
      
        self.reStr = self.reStr + self.ETHdict['anyETH']

        self.reStr = self.reStr + self.ETHdict['ETHNTYpe']

        self.reStr = self.reStr + self.ETHdict['playload']

        
            
'''

class name: IP4
class function: IPv4报文格式

'''      
class IP4(rebase):
    #IPv4基础类
    IP4dict ={}
    def __init__(self):
        super(IP4,self).__init__()
        self.IP4dict['L2'] = '.*'
        self.IP4dict['Ver'] = '4'
        self.IP4dict['TT'] = '\\w{17}'
        self.IP4dict['Protocol'] = '\\w{2}'
        self.IP4dict['HC'] = '\\w{4}'
        self.IP4dict['SIP'] = '\\w{8}'
        self.IP4dict['DIP'] = '\\w{8}'
        self.IP4dict['playload'] = '.*'
        #rebase.reStr = ''

    def setProtocol(self, Protocol):
        tmp = self.changeLen(Protocol, 2)
        self.IP4dict['Protocol'] = tmp

    def setSIP(self, SIP):
        tmp = self.changeLen(SIP, 8)
        self.IP4dict['SIP'] = tmp

    def setDIP(self, DIP):
        tmp = self.changeLen(DIP, 8)
        self.IP4dict['DIP'] = tmp

    def seltIP4Playload(self, playload):
        self.IP4dict['playload'] = playload

    def seltIPL2(self, L2):
        self.IP4dict['L2'] = L2

    
    def combationIP4(self):
        #rebase.reStr = rebase.reStr + self.IP4dict['L2']
        
        self.reStr = self.reStr + self.IP4dict['Ver']
        self.reStr = self.reStr + self.IP4dict['TT']
        self.reStr = self.reStr + self.IP4dict['Protocol']
        self.reStr = self.reStr + self.IP4dict['HC']
        self.reStr = self.reStr + self.IP4dict['SIP']
        self.reStr = self.reStr + self.IP4dict['DIP']
        self.reStr = self.reStr + self.IP4dict['playload']



        
'''

class name: IP4oETH
class function: IPv4报文 on 以太报文： ETH + IPv4

'''  
class IP4oETH(Eth, IP4):

    def __init__(self):
        super(IP4oETH, self).__init__()
       # super(IP4oETH, self).__init__(IP4)
        self.ETHdict['ETHNTYpe'] = '0800'
        self.ETHdict['playload'] = ''
        self.IP4dict['L2'] = ''
        
    
    def combationIP4oEth(self):
        
        self.combationETH()
        self.combationIP4()


        
    
        
        

    
        
    
        
        
        
