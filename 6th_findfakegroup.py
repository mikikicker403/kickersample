
#-*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('program start')
#logging.disable(logging.CRITICAL)

coinsList=[10,10,10,10,10,10,11,10,10,
10,10,10,10,10,10,10,10,10,
10,10,10,10,10,10,10,10,10]


coinsList2=[10,10,10,10,10,10,9,10,10,
10,10,10,10,10,10,10,10,10,
10,10,10,10,10,10,10,10,10]

coinsList3=[10,10,10,10,10,10,12,10,10,
10,10,10,10,10,10,10,10,10,
10,10,10,10,10,10,10,10,10]
def compare(groupA,groupB):#２つのグループのうち重い方を返す(left/right/equal)
    if sum(groupA)>sum(groupB):
        result='left'
    elif sum(groupA)<sum(groupB):
        result='right'
    elif sum(groupA)==sum(groupB):
            result='equal'
    return result

def splitCoins(coinsList):#coinsListを三分割
    length=len(coinsList)
    group1=coinsList[0:length//3]
    group2=coinsList[length//3:(length//3)*2]
    group3=coinsList[(length//3)*2:length]
    return group1,group2,group3

def findFakeGroup(group1,group2,group3):
    #group1/group2を比較し重い方を調べる。等しければgroup3がfake
    result1and2=compare(group1,group2)
    if result1and2=='left':
        fakeGroup=group1
    elif result1and2=='right':
        fakeGroup=group2
    elif result1and2=='equal':
        fakeGroup=group3
    return fakeGroup

def findFakeGroupAndType(group1,group2,group3):
    #group1/group2を比較する。
    #fake>normal fake type heavy
    #fake<normal fake type light
    #compare(group1,group2) and compare(group1,group3) ->heavy light
    #type識別のため２回計測する
    result1and2=compare(group1,group2)
    result1and3=compare(group1,group3)
    print(result1and2,result1and3)
    if result1and2=='left' and result1and3=='left':#group1 heavy
        fakeGroup=group1
        faketype='heavy'
    elif result1and2=='right' and result1and3=='right':#group1 light
        fakeGroup=group1
        faketype='light'
    elif result1and2=='right' and result1and3=='equal':#group2 heavy
        fakeGroup=group2
        faketype='heavy'
    elif result1and2=='left' and result1and3=='equal':#group2 light
        fakeGroup=group2
        faketype='light'
    elif result1and2=='equal' and result1and3=='right':#group3 heavy
        fakeGroup=group3
        faketype='heavy'
    elif result1and2=='equal' and result1and3=='left':#group3 light
        fakeGroup=group3
        faketype='light'
    return fakeGroup,faketype
def findFakeGroup2(group1,group2,group3,cointype):
    result1and2=compare(group1,group2)
    if cointype=='heavy':
        if result1and2=='left':
            return group1
        elif result1and2=='right':
            return group2
        elif result1and2=='equal':
            return group3
    elif cointype=='light':
        if result1and2=='left':
            return group2
        elif result1and2=='right':
            return group1
        elif result1and2=='equal':
            return group3

def CoinComparison(coinsList):#偽コインは重い。重いコインを探す
    counter=0
    currList=coinsList
    while len(currList)>1:
        group1,group2,group3=splitCoins(currList)
        currList=findFakeGroup(group1,group2,group3)
        counter+=1
    fake=currList[0]
    print('The fake coins is coin',coinsList.index(fake)+1,'in the original list')
    print('Number of weighings:',counter)


def CoinComparison2(coinsList):#偽コインは軽重が不明。異なる重さのコインを探す
    counter=0
    currList=coinsList
    while len(currList)>1:
        group1,group2,group3=splitCoins(currList)
        currList,faketype=findFakeGroupAndType(group1,group2,group3)
        counter+=2#type識別のため二回測っている
    fake=currList[0]
    print('The fake coins is coin',coinsList.index(fake)+1,'in the original list.The fake type is',faketype)
    print('Number of weighings:',counter)

def CoinComparison3(coinsList):#偽コインは軽重が不明。異なる重さのコインを探す。軽重が解れば次から調べる必要がない。
    counter=0
    currList=coinsList
    group1,group2,group3=splitCoins(currList)
    currList,faketype=findFakeGroupAndType(group1,group2,group3)
    counter+=2#type識別の為２回計測
    while len(currList)>1:
        group1,group2,group3=splitCoins(currList)
        currList=findFakeGroup2(group1,group2,group3,faketype)
        counter+=1#type識別が済んでいるので１回の計測で良い
    fake=currList[0]
    print('The fake coins is coin',coinsList.index(fake)+1,'in the original list.The fake type is',faketype)
    print('Number of weighings:',counter)



if __name__=='__main__':
    print(coinsList)
    CoinComparison(coinsList)

    print(coinsList2)
    CoinComparison2(coinsList2)
    print(coinsList3)
    CoinComparison2(coinsList3)

    print('== light ==')
    print(coinsList2)
    CoinComparison3(coinsList2)
    print('== heavy ==')
    print(coinsList3)
    CoinComparison3(coinsList3)
    pass


    
