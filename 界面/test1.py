#! python3

import re 

def Mactpye(macstr):
    tmplist = []
    macstr = macstr.strip(" ")
    tmplist = macstr.split("-")
    tmpsrc = ''
    isHex = re.compile(r"^[0-9a-fA-F]{2}$")
    for item in tmplist:
        if(isHex.search(item)):
            tmpsrc = tmpsrc + item
   
    



    

Mactpye("   a0-11-FF-ee-4y-     ")



def IP2Hex(strip):
    strip = strip.strip(" ")
    tmplist = strip.split(".")
    returnstr = ''
    for item in tmplist:
        if item.isdecimal():
            tmpint=int(item)
            tmphex=hex(tmpint)
            tmpstr = str(tmphex)
            tmpstr = tmpstr.lstrip("0x")
            tmpstr = tmpstr.rjust(2,"0")
            returnstr = returnstr + tmpstr

    print(returnstr)
    
IP2Hex("")
    
