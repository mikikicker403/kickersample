
#-*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('program start')
#logging.disable(logging.CRITICAL)
print('帽子の向きを揃える。連続した帽子はまとめて変えることができる。連続した帽子の組が少ない方を変更させるのが良い')
cap1=['F','F','B','B','B','F','B','B','B','F','F','B','F']
cap2=['F','F','B','B','B','F','B','B','B','F','F','F','F']
cap3=['F','F','B','H','B','F','B','B','B','F','H','F','F']

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

def pleaseConform3(caps):
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
            if t[0]!=t[1]:
                print('People in positions',t[0],'through',t[1],'flip your caps!')
            else:
                print('People at position',t[0],'flip your cap!')



def pleaseConform2(caps):
    print('pleaseConform start')
    start=forward=backward=0
    intervals=[]#連続したcapの組（startpos,endpos,FW)
    caps=caps+['END']
    for i in range(1,len(caps)):
        if caps[start]!=caps[i]:
            intervals.append((start,i-1,caps[start]))
            if caps[start]=='F':
                forward+=1
            else:
                backward+=1
            start=i
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



def pleaseConform4(caps):
    print('pleaseConform start')
    start=forward=backward=0
    intervals=[]#連続したcapの組（startpos,endpos,FW)
    caps=caps+['END']
    for i in range(1,len(caps)):
        if caps[start]!=caps[i]:
            intervals.append((start,i-1,caps[start]))
            if caps[start]=='F':
                forward+=1
            elif caps[start]=='B':
                backward+=1
            start=i
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
            if t[0]==t[1]:
                print('Person at positon',t[0],'flip your cap!')
            else:
                print('People in positions',t[0],'through',t[1],'flip your caps!')


def pleaseConformOnepass(caps):
    caps=caps+[caps[0]]
    for i in range(1,len(caps)):
        if caps[i]!=caps[i-1]:
            if caps[i]!=caps[0]:
                print('people in positions',i,end='')
            else:
                print(' through',i-1,'flip your caps!')

def pleaseConformOnepass2(caps):
    #caps=caps+[caps[0]]
    caps=caps+['END']
    st=0
    en=0
    for i in range(1,len(caps)):
        if caps[i-1]!=caps[i]:
            if st==0:
                st=i
            else:
                en=i-1
            if st==0 or en==0:
                continue
            else:
                if st!=en:
                    print('people in positions',st,'through',i-1,'flip your caps!')
                else:
                    print('person at position',en,'flip your cap!')
                st=en=0



#文字列を13W2B12W5Bのように圧縮する
characters='WWWWWWWWWWWWWBBWWWWWWWWWWWWBBBBB'
def compressText(tex):#ランレングス符号化
    tex=tex+'0'
    answer=''
    num=1
    character=''
    for i in range(1,len(tex)):
        
        if tex[i-1]==tex[i]:
            num+=1
        else:
            character+=str(num)+tex[i-1]
            num=1
            #print(character)
        #print(i,num,tex[i])
    print(character)
        
        
def revcompressText(tex):#ランレングス復号化
    st=0
    en=0
    character=''
    for i in range(1,len(tex)):
        if tex[i].isalpha():
            en=i
            character+=tex[i]*int(tex[st:en])
            #print(character)
            st=i+1
    print(character)
    return character

    pass


if __name__=='__main__':
    print(cap1)
    pleaseConform(cap1)
    print(cap1)
    pleaseConform3(cap1)
    #pleaseConform2(cap1)

    #print(cap2)
    #pleaseConform(cap2)
    
    #print(cap1)
    #pleaseConformOnepass(cap1)
    print(cap1)
    pleaseConformOnepass2(cap1)
    print('empty') 
    pleaseConformOnepass2([])
    print(cap3)
    pleaseConform4(cap3)

    compressText(characters)
    revcharacters='13W2B12W5B'
    revcompressText(revcharacters)
    
    pass


    
