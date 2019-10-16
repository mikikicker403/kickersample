
#-*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('program start')
#logging.disable(logging.CRITICAL)

sched=[(6,8),(6,12),(6,7),(7,8),(7,10),(8,9),(8,10),(9,12),(9,10),(10,11),(10,12),(11,12)]

sched2=[(6.0,8.0),(6.5,12.0),(6.5,7.0),(7.0,8.0),
(7.5,10.0),(8.0,9.0),(8.0,10.0),(9.0,12.0),
(9.5,10.0),(10.0,11.0),(10.0,12.0),(11.0,12.0)]

sched3=[(6.0,8.0,2),(6.5,12.0,1),(6.5,7.0,2),
(7.0,8.0,2),(7.5,10.0,3),(8.0,9.0,2),
(8.0,10.0,1),(9.0,12.0,2),
(9.5,10.0,4),(10.0,11.0,2),
(10.0,12.0,3),(11.0,12.0,7)]


def bestTimeToParty(schedule):
    #(問題)時刻刻みが細くなるとループが増えて時間がかかってしまう
    def celebrityDensity(sched,start,end):
        count=[0]*(end+1)#初期化0~end+1個->多くできる0-start-1まで無駄
        for i in range(start,end+1):
            count[i]=0#これもいらない
            for c in sched:
                if c[0]<=i and c[1]>i:
                    count[i]+=1#各時間の滞在人数リストを返す
        return count
    start=schedule[0][0]
    end=schedule[0][1]
    for c in schedule:
        start=min(c[0],start)#初めて来客の時刻を探す
        end=max(c[1],end)#最後に退場の時刻を探す
    count=celebrityDensity(schedule,start,end)#各時刻の滞在人数リストが返る
    maxcount=0
    for i in range(start,end+1):#滞在人数の最大値と時刻を調べる
        if count[i]>maxcount:
            maxcount=count[i]
            time=i
    print('Best time to attend the party is at',time,'O\'clock',':',maxcount,'celebrities will be attending!')

def bestTimeToPartySmart(schedule):
    def sortlist(tlist):#選択ソート
        #最も小さい値を前に置くように並び替えてゆく
        for ind in range(len(tlist)):
            small_pos=ind
            small_value=tlist[small_pos][0]
            for i in range(ind,len(tlist)):
                if tlist[small_pos][0]>tlist[i][0]:
                    small_pos=i#小さい値の位置を記録
                    small_value=tlist[i][0]
            #print('smallest value is',small_value)
            tmp=tlist[ind]
            tlist[ind]=tlist[small_pos]
            tlist[small_pos]=tmp
            #print(tlist)

    def chooseTime(times):
        #最大人数が滞在している時刻と人数を返す
        rcount=0
        maxcount=time=0
        for t in times:
            if t[1]=='start':
                rcount+=1
            elif t[1]=='end':
                rcount-=1
            if rcount>maxcount:#最大値が更新された時刻と人数を記録
                maxcount=rcount
                time=t[0]
        return maxcount,time

    times=[]
    for c in schedule:
        times.append((c[0],'start'))
        times.append((c[1],'end'))
    sortlist(times)
    maxcount,time=chooseTime(times)
    print('Best time to attend the party is at',time,'0\'clock',':',maxcount,'celebrities will be attending!')


def bestTimeToPartySmart2(schedule,ystart,yend):
    print('You visit in',ystart,'until',yend)
    def sortlist(tlist):#選択ソート
        #最も小さい値を前に置くように並び替えてゆく
        for ind in range(len(tlist)):
            small_pos=ind
            small_value=tlist[small_pos][0]
            for i in range(ind,len(tlist)):
                if tlist[small_pos][0]>tlist[i][0]:
                    small_pos=i#小さい値の位置を記録
                    small_value=tlist[i][0]
            #print('smallest value is',small_value)
            tmp=tlist[ind]
            tlist[ind]=tlist[small_pos]
            tlist[small_pos]=tmp
            #print(tlist)

    def chooseTime(times,ystart,yend):
        #最大人数が滞在している時刻と人数を返す
        rcount=0
        maxcount=time=0
        for t in times:
            if t[1]=='start':
                rcount+=1
            elif t[1]=='end':
                rcount-=1
            if t[0]>=ystart and t[0]<yend:
                print('customer is changing:',rcount)
                if rcount>maxcount:#最大値が更新された時刻と人数を記録
                    maxcount=rcount
                    time=t[0]
        return maxcount,time

    times=[]
    for c in schedule:
        times.append((c[0],'start'))
        times.append((c[1],'end'))
    sortlist(times)
    print(times)
    maxcount,time=chooseTime(times,ystart,yend)
    print('You meet max',maxcount,'customers at',time,'0\'clock')

def anothermethod_bestTimeToParty(schedule):
    #個人が到着した時に滞在している人数の最大の客に合わせて訪れる
    maxcount=pos=0
    for i in range(len(schedule)):
        rcount=1
        for j in range(len(schedule)):
            if i==j:
                continue
            if (schedule[i][0]>= schedule[j][0]) and (schedule[i][0]<schedule[j][1]):#先に来ている
                rcount+=1
        if maxcount<rcount:
            maxcount=rcount
            pos=i
    print('max customer is',maxcount,'.start time is',schedule[pos][0],'O\'clock')
    print(schedule[pos])

def bestTimeToPartyWithweight(schedule):
    def sortlist(tlist):#選択ソート
        #最も小さい値を前に置くように並び替えてゆく
        for ind in range(len(tlist)):
            small_pos=ind
            small_value=tlist[small_pos][0]
            for i in range(ind,len(tlist)):
                if tlist[small_pos][0]>tlist[i][0]:
                    small_pos=i#小さい値の位置を記録
                    small_value=tlist[i][0]
            #print('smallest value is',small_value)
            tmp=tlist[ind]
            tlist[ind]=tlist[small_pos]
            tlist[small_pos]=tmp
            #print(tlist)

    def chooseTime(times):
        #最大人数が滞在している時刻と人数を返す
        weightcount=0
        maxcount=time=0
        for t in times:
            if t[1]=='start':
                weightcount+=t[2]
            elif t[1]=='end':
                weightcount-=t[2]
            if weightcount>maxcount:#最大値が更新された時刻と人数を記録
                maxcount=weightcount
                time=t[0]
        return maxcount,time

    times=[]
    for c in schedule:
        times.append((c[0],'start',c[2]))
        times.append((c[1],'end',c[2]))
    sortlist(times)
    print(times)
    weightcount,time=chooseTime(times)
    print('Your best time is',time,'O\'clock','because weight is',weightcount)
if __name__=='__main__':
    print(sched)
    bestTimeToParty(sched)

    print(sched2)
    bestTimeToPartySmart(sched2)

    print(sched2)
    bestTimeToPartySmart2(sched2,11,12)
    bestTimeToPartySmart2(sched2,8,10)

    print(sched2)
    anothermethod_bestTimeToParty(sched2)

    print(sched3)
    bestTimeToPartyWithweight(sched3)
    pass


    
