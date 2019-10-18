
#-*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('program start')
#logging.disable(logging.CRITICAL)

B=[[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def show_board(board):
    for w in board:
        for w2 in w:
            print(w2,end=' ')
        else:
            print('\n')
    else:
        print('-'*20)

def noConflicts(board,current,qindex,n):
    for j in range(current):
        if board[qindex][j]==1:
            return False
    k=1
    while qindex-k>=0 and current-k>=0:
        if board[qindex-k][current-k]==1:
            return False
        k+=1
    k=1
    while qindex+k<n and current-k>=0:
        if board[qindex+k][current-k]==1:
            return False
        k+=1
    return True
def noConflicts2(board,current):
    for i in range(current):
        if (board[i]==board[current]):#水平チェック
            return False
        if (current-i==abs(board[current]-board[i])):#斜めチェック左上左下
            return False
    return True


def FourQueens(n=4):
    board=[[0]*n for i in range(n)]
    for i in range(n):
        board[i][0]=1
        for j in range(n):
            board[j][1]=1
            if noConflicts(board,1,j,n):
                for k in range(n):
                    board[k][2]=1
                    if noConflicts(board,2,k,n):
                        for m in range(n):
                            board[m][3]=1
                            if noConflicts(board,3,m,n):
                                print(board)
                            board[m][3]=0
                    board[k][2]=0
            board[j][1]=0
        board[i][0]=0
    return

def FourQueens2(n=4):
    #noConflicts(board,column,row,n)
    #board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    board=[[0]*n for i in range(n)]
    #print(board)
    for i in range(n):
        board[i][0]=1
        for j in range(n):
            board[j][1]=1
            if not noConflicts(board,1,j,n):
                board[j][1]=0
                continue
            for k in range(n):
                board[k][2]=1
                if not noConflicts(board,2,k,n):
                    board[k][2]=0
                    continue
                for m in range(n):
                    board[m][3]=1
                    if not noConflicts(board,3,m,n):
                        board[m][3]=0
                        continue
                    print(board)
        board[i][0]=0
    return 

def EightQueens(n=8):
    board=[-1]*n
    for i in range(n):
        board[0]=i
        for j in range(n):
            board[1]=j
            if not noConflicts2(board,1):
                continue
            for k in range(n):
                board[2]=k
                if not noConflicts2(board,2):
                    continue
                for l in range(n):
                    board[3]=l
                    if not noConflicts2(board,3):
                        continue
                    for m in range(n):
                        board[4]=m
                        if not noConflicts2(board,4):
                            continue
                        for o in range(n):
                            board[5]=o
                            if not noConflicts2(board,5):
                                continue
                            for p in range(n):
                                board[6]=p
                                if not noConflicts2(board,6):
                                    continue
                                for q in range(n):
                                    board[7]=q
                                    if noConflicts2(board,7):
                                        print(board)

    return

def EightQueens2(count,n=8):
    board=[-1]*n
    num=0
    for i in range(n):
        board[0]=i
        for j in range(n):
            board[1]=j
            if not noConflicts2(board,1):
                continue
            for k in range(n):
                board[2]=k
                if not noConflicts2(board,2):
                    continue
                for l in range(n):
                    board[3]=l
                    if not noConflicts2(board,3):
                        continue
                    for m in range(n):
                        board[4]=m
                        if not noConflicts2(board,4):
                            continue
                        for o in range(n):
                            board[5]=o
                            if not noConflicts2(board,5):
                                continue
                            for p in range(n):
                                board[6]=p
                                if not noConflicts2(board,6):
                                    continue
                                for q in range(n):
                                    board[7]=q
                                    if noConflicts2(board,7):
                                        print(board)
                                        num+=1
                                        if num==count:
                                            return

    return

def EightQueens3(count,n=8,location=[-1,-1,-1,-1,-1,-1,-1,-1]):
    board=[-1]*n
    num=0
    for i in range(n):
        board[0]=i
        if location[0]>=0:
            board[0]=location[0]
        for j in range(n):
            board[1]=j
            if location[1]>=0:
                board[1]=location[1]
            if not noConflicts2(board,1):
                continue
            for k in range(n):
                board[2]=k
                if location[2]>=0:
                    board[2]=location[2]
                if not noConflicts2(board,2):
                    continue
                for l in range(n):
                    board[3]=l
                    if location[3]>=0:
                        board[3]=location[3]
                    if not noConflicts2(board,3):
                        continue
                    for m in range(n):
                        board[4]=m
                        if location[4]>=0:
                            board[4]=location[4]
                        if not noConflicts2(board,4):
                            continue
                        for o in range(n):
                            board[5]=o
                            if location[5]>=0:
                                board[5]=location[5]
                            if not noConflicts2(board,5):
                                continue
                            for p in range(n):
                                board[6]=p
                                if location[6]>=0:
                                    board[6]=location[6]
                                if not noConflicts2(board,6):
                                    continue
                                for q in range(n):
                                    board[7]=q
                                    if location[7]>=0:
                                        board[7]=location[7]
                                    if noConflicts2(board,7):
                                        print(board)
                                        num+=1
                                        if num==count:
                                            return

    return
if __name__=='__main__':
    #noConflicts(board,column,row,n):
    #ret=noConflicts(B,1,0,4)
    #print(ret)
    #ret=noConflicts(B,1,1,4)
    #print(ret)
    #ret=noConflicts(B,1,2,4)
    #print(ret)
    FourQueens2()
    print('#'*10)
    FourQueens()
    #print('#'*10)
    #EightQueens(8)
    #print('#'*10)
    #EightQueens2(2,8)
    #print('#'*10)
    #EightQueens3(100,8,[-1,4,-1,-1,-1,-1,-1,0])
    #print('#'*10)

    pass


    
