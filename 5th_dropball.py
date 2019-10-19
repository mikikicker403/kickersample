#-*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('program start')
#logging.disable(logging.CRITICAL)


def convertToDecimal2(r,rep):
    number=0
    for i in range(len(rep)):
        num=rep[i]*(r**(len(rep)-1-i))
        print('num:',num,rep[i],r**(len(rep)-1-i))
        number+=num
    return number
def convertToDecimal(r,d,rep):
    number=0
    for i in range(d-1):
        number=(number+rep[i])*r
    number+=rep[d-1]
    return number



def howHardIsTheCrystal(n,d):
    #d:a number of crystal / n:total step of tower
    r=1
    while (r**d<=n):#r**dでnを超えるrを探す
        r=r+1
    print('Radix chosen is',r)
    numDrops=0
    floorNoBreak=[0]*d
    for i in range(d):
        for j in range(r-1):
            floorNoBreak[i]+=1
            Floor=convertToDecimal(r,d,floorNoBreak)
            if Floor>n:
                floorNoBreak[i]-=1
                break
            print('Drop ball',i+1,'from Floor',Floor)
            yes=input('Did the ball break (yes/no)?:')
            numDrops+=1
            if yes=='yes':
                floorNoBreak[i]-=1
                break
    hardness=convertToDecimal(r,d,floorNoBreak)
    return hardness,numDrops

if __name__=='__main__':
    num=convertToDecimal(5,4,[1,2,2,4])#189
    print(num)
    num=convertToDecimal2(5,[1,2,2,4])#189
    print(num)
    howHardIsTheCrystal(128,5)


    
