
#-*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('program start')
#logging.disable(logging.CRITICAL)

import random

deck=('A_C','A_D','A_H','A_S',
'2_C','2_D','2_H','2_S',
'3_C','3_D','3_H','3_S',
'4_C','4_D','4_H','4_S',
'5_C','5_D','5_H','5_S',
'6_C','6_D','6_H','6_S',
'7_C','7_D','7_H','7_S',
'8_C','8_D','8_H','8_S',
'9_C','9_D','9_H','9_S',
'10_C','10_D','10_H','10_S',
'J_C','J_D','J_H','J_S',
'Q_C','Q_D','Q_H','Q_S',
'K_C','K_D','K_H','K_S')
deck2=('A_C','2_C','3_C','4_C','5_C','6_C','7_C','8_C','9_C','10_C','J_C','Q_C','K_C',
'A_D','2_D','3_D','4_D','5_D','6_D','7_D','8_D','9_D','10_D','J_D','Q_D','K_D',
'A_H','2_H','3_H','4_H','5_H','6_H','7_H','8_H','9_H','10_H','J_H','Q_H','K_H',
'A_S','2_S','3_S','4_S','5_S','6_S','7_S','8_S','9_S','10_S','J_S','Q_S','K_S')
def AssistantOrdersCards():
    def outputFirstCard(ns,oneTwo,cards):
        #hidden,other,encode=outputFirstCard(cnumbers,cardh,cards)
        encode=(ns[oneTwo[0]]-ns[oneTwo[1]])%13
        #print(ns,'/encode:',encode)
        if encode >0 and encode <=6:
            hidden=oneTwo[0]#隠すカード
            other=oneTwo[1]#同じマークで見せるカード
        else:
            hidden=oneTwo[1]#隠すカード0-4
            other=oneTwo[0]#同じマークで見せるカード
            encode=(ns[oneTwo[1]]-ns[oneTwo[0]])%13
            #print(ns,'/encode:',encode)
        print('Assistant:First card is:',cards[other])
        return hidden,other,encode
    def sortList2(tlist):#選択ソート
        #最も小さい値を前に置くように並び替えてゆく
        for ind in range(len(tlist)-1):
            small_pos=ind
            small_value=tlist[small_pos]
            for i in range(ind,len(tlist)):
                if tlist[small_pos]>tlist[i]:
                    small_pos=i#小さい値の位置を記録
                    small_value=tlist[i]
            #print('smallest value is',small_value)
            tmp=tlist[ind]
            tlist[ind]=tlist[small_pos]
            tlist[small_pos]=tmp
            #print(tlist)

    def outputNext3Cards(code,ind):
        print('code:',code,'//ind',ind)
        if code==1:
            second,third,fourth=ind[0],ind[1],ind[2]
        elif code==2:
            second,third,fourth=ind[0],ind[2],ind[1]
        elif code==3:
            second,third,fourth=ind[1],ind[0],ind[2]
        elif code==4:
            second,third,fourth=ind[1],ind[2],ind[0]
        elif code==5:
            second,third,fourth=ind[2],ind[0],ind[1]
        elif code==6:
            second,third,fourth=ind[2],ind[1],ind[0]
        print('Assistant:Second card is:',deck[second])
        print('Assistant:Third card is:',deck[third])
        print('Assistant:Fourth card is:',deck[fourth])

    #main
    print('Assistant:Cards are character strings as shown below')
    print('Assistant:Ordering is:',deck)
    
    cards,cind,cardsuits,cnumbers=[],[],[],[]#cards:選ばれたオリジナルカード（テキスト)/cind:deckのポジション/cardsuits:オリジナルカードのマークリスト/cnumbers:オリジナルカードの数値のリスト(0-12)
    numsuits=[0,0,0,0]
    for i in range(5):
        print('Please give card',i+1,end=' ')
        card=input('in above format:')
        cards.append(card)#card mark_number text
        n=deck.index(card)
        cind.append(n)#card position
        cardsuits.append(n%4)#0-3のリスト/0C,1D,2H,3S
        cnumbers.append(n//4)#0-12のリスト
        numsuits[n%4]+=1#mark count
        if numsuits[n%4]>1:
            pairsuit=n%4#0-3/重複しているマーク0C,1D,2H,3S
    
    cardh=[]
    for i in range(5):
        if cardsuits[i]==pairsuit:
            cardh.append(i)#重複しているマークのポジション
    hidden,other,encode=outputFirstCard(cnumbers,cardh,cards)#hidden:隠すカード/other:Firstcard/encode:秘密の数
    remindices=[]
    for i in range(5):
        if i != hidden and i != other:#hidden:隠すカードの位置/other:1stのカード
            remindices.append(cind[i])#残りの３カード
    sortList2(remindices)
    outputNext3Cards(encode,remindices)
    return 

def MagicianGuessesCard():
    print('Magician:Cards are character strings as shown below.')
    print('Magician:Ordering is:',deck)

    cards,cind=[],[]
    for i in range(4):
        print('Please give card',i+1,end=' ')
        card=input('in above format:')
        cards.append(card)
        n=deck.index(card)
        cind.append(n)
        if i==0:
            suit =n%4
            number=n//4
    if cind[1]<cind[2] and cind[1]<cind[3]:
        if cind[2] < cind[3]:
            encode=1
        else:
            encode=2
    elif ((cind[1]<cind[2] and cind[1]>cind[3])or (cind[1]>cind[2] and cind[1]<cind[3])):
        if cind[2]<cind[3]:
            encode=3
        else:
            encode=4
    elif cind[1]>cind[2] and cind[1]>cind[3]:
        if cind[2]<cind[3]:
            encode=5
        else:
            encode=6
    print('encode:',encode)
    hiddennumber=(number+encode)%13
    index=hiddennumber*4+suit
    print('Hidden card is:',deck[index])

def ComputerAssistant():
    def outputFirstCard(ns,oneTwo,cards):
        #hidden,other,encode=outputFirstCard(cnumbers,cardh,cards)
        encode=(ns[oneTwo[0]]-ns[oneTwo[1]])%13
        #print(ns,'/encode:',encode)
        if encode >0 and encode <=6:
            hidden=oneTwo[0]#隠すカード
            other=oneTwo[1]#同じマークで見せるカード
        else:
            hidden=oneTwo[1]#隠すカード0-4
            other=oneTwo[0]#同じマークで見せるカード
            encode=(ns[oneTwo[1]]-ns[oneTwo[0]])%13
            #print(ns,'/encode:',encode)
        print('Assistant:First card is:',cards[other])
        return hidden,other,encode
    def sortList2(tlist):#選択ソート
        #最も小さい値を前に置くように並び替えてゆく
        for ind in range(len(tlist)-1):
            small_pos=ind
            small_value=tlist[small_pos]
            for i in range(ind,len(tlist)):
                if tlist[small_pos]>tlist[i]:
                    small_pos=i#小さい値の位置を記録
                    small_value=tlist[i]
            #print('smallest value is',small_value)
            tmp=tlist[ind]
            tlist[ind]=tlist[small_pos]
            tlist[small_pos]=tmp
            #print(tlist)

    def outputNext3Cards(code,ind):
        if code==1:
            second,third,fourth=ind[0],ind[1],ind[2]
        elif code==2:
            second,third,fourth=ind[0],ind[2],ind[1]
        elif code==3:
            second,third,fourth=ind[1],ind[0],ind[2]
        elif code==4:
            second,third,fourth=ind[1],ind[2],ind[0]
        elif code==5:
            second,third,fourth=ind[2],ind[0],ind[1]
        elif code==6:
            second,third,fourth=ind[2],ind[1],ind[0]
        print('Assistant:Second card is:',deck[second])
        print('Assistant:Third card is:',deck[third])
        print('Assistant:Fourth card is:',deck[fourth])

    print('Assistant:Cards are character strings as shown below.')
    print('Assistant:Ordering is:',deck)
    cards,cind,cardsuits,cnumbers=[],[],[],[]
    numsuits=[0,0,0,0]
    #number=int(input('Please give random number of '+'at least 6 digits:'))
    number=random.randint(100000,999999)
    for i in range(5):
        number=number*(i+1)//(i+2)
        
        n=number%52
        cards.append(deck[n])
        cind.append(n)
        cardsuits.append(n%4)
        cnumbers.append(n//4)
        numsuits[n%4]+=1
        if numsuits[n%4] > 1:
            pairsuit=n%4

    cardh=[]
    for i in range(5):
        if cardsuits[i]==pairsuit:
            cardh.append(i)#重複しているマークのポジション
    hidden,other,encode=outputFirstCard(cnumbers,cardh,cards)#hidden:隠すカード/other:Firstcard/encode:秘密の数
    remindices=[]
    for i in range(5):
        if i != hidden and i != other:#hidden:隠すカードの位置/other:1stのカード
            remindices.append(cind[i])#残りの３カード
    sortList2(remindices)
    outputNext3Cards(encode,remindices)
    guess=input('What is the hidden card?')
    if guess == cards[hidden]:
        print('You are a Mind Reader Extraordinaire!')
    else:
        print('Sorry,not impressed!')
        print('The Answer is',cards[hidden])
    return 

#deck2
def ComputerAssistant3():
    def card_draw():
        while True:
            cards,cind,cardsuits,cnumbers=[],[],[],[]
            numsuits=[0,0,0,0]
            #number=int(input('Please give random number of '+'at least 6 digits:'))
            number=random.randint(100000,999999)
            for i in range(5):
                number=number*(i+1)//(i+2)
            
                n=number%52
                cards.append(deck2[n])
                cind.append(n)
                cardsuits.append(n//13)
                cnumbers.append(n%13)
                numsuits[n//13]+=1
                if numsuits[n//13] > 1:
                    pairsuit=n//13
            if len(set(cards))==len(cards):
                print(cards)
                return cards,cind,cardsuits,cnumbers,numsuits,pairsuit
            else:
                continue

    def outputFirstCard(ns,oneTwo,cards):
        #hidden,other,encode=outputFirstCard(cnumbers,cardh,cards)
        encode=(ns[oneTwo[0]]-ns[oneTwo[1]])%13
        #print(ns,'/encode:',encode)
        if encode >0 and encode <=6:
            hidden=oneTwo[0]#隠すカード
            other=oneTwo[1]#同じマークで見せるカード
        else:
            hidden=oneTwo[1]#隠すカード0-4
            other=oneTwo[0]#同じマークで見せるカード
            encode=(ns[oneTwo[1]]-ns[oneTwo[0]])%13
            #print(ns,'/encode:',encode)
        print('Assistant:First card is:',cards[other])
        return hidden,other,encode
    def sortList2(tlist):#選択ソート
        #最も小さい値を前に置くように並び替えてゆく
        for ind in range(len(tlist)-1):
            small_pos=ind
            small_value=tlist[small_pos]
            for i in range(ind,len(tlist)):
                if tlist[small_pos]>tlist[i]:
                    small_pos=i#小さい値の位置を記録
                    small_value=tlist[i]
            #print('smallest value is',small_value)
            tmp=tlist[ind]
            tlist[ind]=tlist[small_pos]
            tlist[small_pos]=tmp
            #print(tlist)

    def outputNext3Cards(code,ind):
        if code==1:
            second,third,fourth=ind[0],ind[1],ind[2]
        elif code==2:
            second,third,fourth=ind[0],ind[2],ind[1]
        elif code==3:
            second,third,fourth=ind[1],ind[0],ind[2]
        elif code==4:
            second,third,fourth=ind[1],ind[2],ind[0]
        elif code==5:
            second,third,fourth=ind[2],ind[0],ind[1]
        elif code==6:
            second,third,fourth=ind[2],ind[1],ind[0]
        print('Assistant:Second card is:',deck2[second])
        print('Assistant:Third card is:',deck2[third])
        print('Assistant:Fourth card is:',deck2[fourth])
        '''
        if len(set(cnumbers))==len(cnumbers):
            pass
        else:
            if code==1:
                print('当てられるでしょうか？')
            elif code==2:
                print('皆さんにびっくりしてもらいましょう')
            elif code==3:
                print('ちゃんと当てられるでしょうか？')
            elif code==4:
                print('だいたい絞り込まれてきましたか？')
            elif code==5:
                print('えーそれでは当ててもらいましょう')
            elif code==6:
                print('不思議と当たるんですよね')
           
            print('ENCODE:',code)
            '''
    print('Assistant:Cards are character strings as shown below.')
    print('Assistant:Ordering is:',deck2)
    cards,cind,cardsuits,cnumbers,numsuits,pairsuit=card_draw()

    cardh=[]
    for i in range(5):
        if cardsuits[i]==pairsuit:
            cardh.append(i)#重複しているマークのポジション
    hidden,other,encode=outputFirstCard(cnumbers,cardh,cards)#hidden:隠すカード/other:Firstcard/encode:秘密の数
    remindices=[]
    for i in range(5):
        if i != hidden and i != other:#hidden:隠すカードの位置/other:1stのカード
            remindices.append(cind[i])#残りの３カード
    sortList2(remindices)
    outputNext3Cards(encode,remindices)
    guess=input('What is the hidden card?')
    if guess == cards[hidden]:
        print('You are a Mind Reader Extraordinaire!')
    else:
        print('Sorry,not impressed!')
        print('The Answer is',cards[hidden])
    return #EndComputerassistant3


def AssistantOrdersCards2():
    def outputFirstCard(ns,oneTwo,cards):
        #hidden,other,encode=outputFirstCard(cnumbers,cardh,cards)
        minhidden=0
        minother=0
        minencode=99999999999999
        for i in range(len(oneTwo)-1):
            for j in range(i+1,len(oneTwo)):
                encode=(ns[oneTwo[i]]-ns[oneTwo[j]])%13
                if encode >0 and encode <=6:
                    hidden=oneTwo[i]#隠すカード
                    other=oneTwo[j]#同じマークで見せるカード
                else:
                    hidden=oneTwo[j]#隠すカード0-4
                    other=oneTwo[i]#同じマークで見せるカード
                    encode=(ns[oneTwo[j]]-ns[oneTwo[i]])%13
                #print(encode)
                if encode<minencode:
                    minencode=encode
                    minhidden=hidden
                    minother=other
                    
        hidden=minhidden;other=minother;encode=minencode
        print('Assistant:First card is:',cards[other])
        return hidden,other,encode
    def sortList2(tlist):#選択ソート
        #最も小さい値を前に置くように並び替えてゆく
        for ind in range(len(tlist)-1):
            small_pos=ind
            small_value=tlist[small_pos]
            for i in range(ind,len(tlist)):
                if tlist[small_pos]>tlist[i]:
                    small_pos=i#小さい値の位置を記録
                    small_value=tlist[i]
            #print('smallest value is',small_value)
            tmp=tlist[ind]
            tlist[ind]=tlist[small_pos]
            tlist[small_pos]=tmp
            #print(tlist)

    def outputNext3Cards(code,ind):
        if code==1:
            second,third,fourth=ind[0],ind[1],ind[2]
        elif code==2:
            second,third,fourth=ind[0],ind[2],ind[1]
        elif code==3:
            second,third,fourth=ind[1],ind[0],ind[2]
        elif code==4:
            second,third,fourth=ind[1],ind[2],ind[0]
        elif code==5:
            second,third,fourth=ind[2],ind[0],ind[1]
        elif code==6:
            second,third,fourth=ind[2],ind[1],ind[0]
        print('Assistant:Second card is:',deck[second])
        print('Assistant:Third card is:',deck[third])
        print('Assistant:Fourth card is:',deck[fourth])

    #main
    print('Assistant:Cards are character strings as shown below')
    print('Assistant:Ordering is:',deck)
    
    cards,cind,cardsuits,cnumbers=[],[],[],[]#cards:選ばれたオリジナルカード（テキスト)/cind:deckのポジション/cardsuits:オリジナルカードのマークリスト/cnumbers:オリジナルカードの数値のリスト(0-12)
    numsuits=[0,0,0,0]
    for i in range(5):
        print('Please give card',i+1,end=' ')
        card=input('in above format:')
        cards.append(card)#card mark_number text
        n=deck.index(card)
        cind.append(n)#card position
        cardsuits.append(n%4)#0-3のリスト/0C,1D,2H,3S
        cnumbers.append(n//4)#0-12のリスト
        numsuits[n%4]+=1#mark count
        if numsuits[n%4]>1:
            pairsuit=n%4#0-3/重複しているマーク0C,1D,2H,3S
    
    cardh=[]
    for i in range(5):
        if cardsuits[i]==pairsuit:
            cardh.append(i)#重複しているマークのポジション
    hidden,other,encode=outputFirstCard(cnumbers,cardh,cards)#hidden:隠すカード/other:Firstcard/encode:秘密の数
    remindices=[]
    for i in range(5):
        if i != hidden and i != other:#hidden:隠すカードの位置/other:1stのカード
            remindices.append(cind[i])#残りの３カード
    sortList2(remindices)
    outputNext3Cards(encode,remindices)
    return 



def ComputerAssistant2():
    def card_draw():
        while True:
            cards,cind,cardsuits,cnumbers=[],[],[],[]
            numsuits=[0,0,0,0]
            #number=int(input('Please give random number of '+'at least 6 digits:'))
            number=random.randint(100000,999999)
            for i in range(5):
                number=number*(i+1)//(i+2)
            
                n=number%52
                cards.append(deck[n])
                cind.append(n)
                cardsuits.append(n%4)
                cnumbers.append(n//4)
                numsuits[n%4]+=1
                if numsuits[n%4] > 1:
                    pairsuit=n%4
            if len(set(cards))==len(cards):
                print(cards)
                return cards,cind,cardsuits,cnumbers,numsuits,pairsuit
            else:
                continue

    def outputFirstCard(ns,oneTwo,cards):
        #hidden,other,encode=outputFirstCard(cnumbers,cardh,cards)
        encode=(ns[oneTwo[0]]-ns[oneTwo[1]])%13
        #print(ns,'/encode:',encode)
        if encode >0 and encode <=6:
            hidden=oneTwo[0]#隠すカード
            other=oneTwo[1]#同じマークで見せるカード
        else:
            hidden=oneTwo[1]#隠すカード0-4
            other=oneTwo[0]#同じマークで見せるカード
            encode=(ns[oneTwo[1]]-ns[oneTwo[0]])%13
            #print(ns,'/encode:',encode)
        print('Assistant:First card is:',cards[other])
        return hidden,other,encode
    def sortList2(tlist):#選択ソート
        #最も小さい値を前に置くように並び替えてゆく
        for ind in range(len(tlist)-1):
            small_pos=ind
            small_value=tlist[small_pos]
            for i in range(ind,len(tlist)):
                if tlist[small_pos]>tlist[i]:
                    small_pos=i#小さい値の位置を記録
                    small_value=tlist[i]
            #print('smallest value is',small_value)
            tmp=tlist[ind]
            tlist[ind]=tlist[small_pos]
            tlist[small_pos]=tmp
            #print(tlist)

    def outputNext3Cards(code,ind):
        if code==1:
            second,third,fourth=ind[0],ind[1],ind[2]
        elif code==2:
            second,third,fourth=ind[0],ind[2],ind[1]
        elif code==3:
            second,third,fourth=ind[1],ind[0],ind[2]
        elif code==4:
            second,third,fourth=ind[1],ind[2],ind[0]
        elif code==5:
            second,third,fourth=ind[2],ind[0],ind[1]
        elif code==6:
            second,third,fourth=ind[2],ind[1],ind[0]
        print('Assistant:Second card is:',deck[second])
        print('Assistant:Third card is:',deck[third])
        print('Assistant:Fourth card is:',deck[fourth])
        '''
        if len(set(cnumbers))==len(cnumbers):
            pass
        else:
            if code==1:
                print('当てられるでしょうか？')
            elif code==2:
                print('皆さんにびっくりしてもらいましょう')
            elif code==3:
                print('ちゃんと当てられるでしょうか？')
            elif code==4:
                print('だいたい絞り込まれてきましたか？')
            elif code==5:
                print('えーそれでは当ててもらいましょう')
            elif code==6:
                print('不思議と当たるんですよね')
           
            print('ENCODE:',code)
            '''
    print('Assistant:Cards are character strings as shown below.')
    print('Assistant:Ordering is:',deck)
    cards,cind,cardsuits,cnumbers,numsuits,pairsuit=card_draw()

    cardh=[]
    for i in range(5):
        if cardsuits[i]==pairsuit:
            cardh.append(i)#重複しているマークのポジション
    hidden,other,encode=outputFirstCard(cnumbers,cardh,cards)#hidden:隠すカード/other:Firstcard/encode:秘密の数
    remindices=[]
    for i in range(5):
        if i != hidden and i != other:#hidden:隠すカードの位置/other:1stのカード
            remindices.append(cind[i])#残りの３カード
    sortList2(remindices)
    outputNext3Cards(encode,remindices)
    guess=input('What is the hidden card?')
    if guess == cards[hidden]:
        print('You are a Mind Reader Extraordinaire!')
    else:
        print('Sorry,not impressed!')
        print('The Answer is',cards[hidden])
    return 
if __name__=='__main__':
    #AssistantOrdersCards()
    #MagicianGuessesCard()
    #ComputerAssistant()
    #ComputerAssistant2()
    #AssistantOrdersCards2()
    ComputerAssistant3()
    pass


    
