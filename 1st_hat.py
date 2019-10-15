
#-*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('program start')
#logging.disable(logging.CRITICAL)
print('帽子の向きを揃える。連続した帽子はまとめて変えることができる。連続した帽子の組が少ない方を変更させるのが良い')
cap1=['F','F','B','B','B','F','B','B','B','F','F','B','F']
cap2=['F','F','B','B','B','F','B','B','B','F','F','F','F']

def pleaseConform(caps):
    print('pleaseConform start')
    start=forward=backward=0
    intervals=[]#連続したcapの組（startpos,endpos,FW)
    for i in range(1,len(caps)):
        if caps[start]!=caps[i]:
            intervals.append((start,i-1,caps[start]))
            if caps[start]=='F':
                forward+=1
            else:
                backward+=1
            start=i
    intervals.append((start,len(caps)-1,caps[start]))#最後の組み合わせ
    if caps[start]=='F':
        forward+=1
    else:
        backward+=1
    #前後どちらに合わせるか判定
    print('F:{forward} // B:{backward}'.format(forward=forward,backward=backward))
    if forward<backward:
        flip='F'#backwardへチェンジ
    else:
        flip='B'#forwardへチェンジ

    #かぶり直す命令
    for t in intervals:
        if t[2]==flip:
            print('People in positions',t[0],'through',t[1],'flip your caps!')


if __name__=='__main__':
    print(cap1)
    pleaseConform(cap1)

    print(cap2)
    pleaseConform(cap2)


    pass


    
