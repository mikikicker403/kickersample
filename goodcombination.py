
#-*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('program start')
#logging.disable(logging.CRITICAL)
import itertools
import requests,bs4,re,time

Talents=['Sing','Dance','Magic','Act','Flex','Code']
Candidates=['Aly','Bob','Cal','Don','Eve','Fay']
CandidateTalents=[['Flex','Code',],['Dance','Magic'],['Sing','Magic'],['Sing','Dance'],['Dance','Act','Code'],['Act','Code']]

CandTal_dic={'Aly':['Flex','Code'],'Bob':['Dance','Magic'],'Cal':['Sing','Magic'],'Don':['Sing','Dance'],'Eve':['Dance','Act','Code'],'Fay':['Act','Code']}

def get_data(keyword=''):
    #keyword='シュアラスター　スポンジ'
    baseurl='https://search.rakuten.co.jp/search/mall/{keyword}/?p={page}'
    result=[]
    def get_soup(url):
        time.sleep(10)
        response=requests.get(url)
        html=response.text
        soup=bs4.BeautifulSoup(html)
        return soup
    for i in range(1,10):
        url=baseurl.format(keyword=keyword,page=1)
        try:
            soup=get_soup(url)
        except Exception as e:
            print(e)
            brak
        ret=soup.find_all('div',{'class':'dui-card searchresultitem'})
        for w in ret:
            title=re.sub(r'[\u3000| |　]','_',w.find('a',{'data-track-action':'title'}).text)
            shop=re.sub(r'[\u3000| |　]','_',w.find('a',{'data-track-action':'shop'}).text)
            result.append((keyword,shop))
            print(title,keyword,shop)
    write_TupToCsv(result)
    return result
def write_TupToCsv(tup,fname='test.csv'):
    basetex='{keyword},{shop}\n'
    savetex=''
    for w in tup:
        print(w)
        savetex+=basetex.format(keyword=w[0],shop=w[1])
    with open(fname,'a') as f:
        f.write(savetex)
        
def write_DicToCsv(dic,fname='test.csv'):
    tex='{ability},{person}\n'
    all_tex=''
    for person in dic.keys():
        for ab in dic[person]:
            all_tex+=tex.format(ability=ab,person=person)
    with open(fname,'a') as f:
        f.write(all_tex)

def read_CsvToDic(fname='test.csv'):
    dic={}
    with open(fname,'r') as f:
        for l in f.readlines():
            lt=l.strip().split(',')
            dic.setdefault(lt[1],[])
            dic[lt[1]].append(lt[0])

    for k in dic.keys():
        tmp=dic[k]
        tmp2=tuple(set(tmp))
        dic[k]=tmp2
    return dic
        
        

    


def Hire4Show(candList,candTalents,talentList):
    n=len(candList)#a number of people
    hire=candList[:]#all people
    for i in range(2**n):
        Combination=[]
        num=i
        for j in range(n):
            if (num%2==1):
                Combination=[candList[n-1-j]]+Combination
            num=num//2
        if Good(Combination,candList,candTalents,talentList):
            if len(hire)>len(Combination):
                hire=Combination
    print('Optimum Solution:',hire)

def Good(Comb,candList,candTalents,AllTalents):
    #Good(Combination,candList,candTalents,talentList):
    for tal in AllTalents:
        cover=False
        for cand in Comb:
            candTal=candTalents[candList.index(cand)]
            if tal in candTal:
                cover=True
    if not cover:
        return False
    return True

def Good2(comb,talents,dic):
    #Good(Combination,candList,candTalents,talentList):
    all_ability=[]
    for person in comb:
        ability=dic[person]
        all_ability+=ability
    for ab in talents:
        if not (ab in all_ability):
            return False
    return True

def Good3(comb,talents,dic):
    #Good(Combination,candList,candTalents,talentList):
    all_ability=[]
    num=0
    for person in comb:
        ability=dic[person]
        all_ability+=ability
    for ab in talents:
        ability_set=set(all_ability)
        if (ab in ability_set):
            num+=1
    return num

def Hire4Show2(dic):
    num=99999999999
    hire=[]
    for i in range(1,len(dic.keys())+1):
        for ele in itertools.combinations(dic.keys(),i):
            if Good2(ele,Talents,dic):
                if num>len(ele):
                    hire=ele
                    num=len(ele)
                    print('len(ele) is 更新:',ele,len(ele))
    print('Optimum Solution:',hire)

def Hire4Show3(dic):
    num=0
    counter=0
    hire=[]
    for i in range(1,len(dic.keys())+1):
        for ele in itertools.combinations(dic.keys(),i):
            print(ele)
            num=Good3(ele,Talents,dic)
            if num>counter:
                hire=ele
                counter=num
                print('len(ele) is 更新:',ele,len(ele),'// num:',counter)
    print('Optimum Solution:',hire,',fill condition:',num,',length:',len(hire))
if __name__=='__main__':

    #Hire4Show2(CandTal_dic)
    #Hire4Show3(CandTal_dic)
    #write_DicToCsv(CandTal_dic,'test.txt')
    #dic=read_CsvToDic('test.txt')
    #for v in dic.values():
    #    print(v)
    get_data('ブリス　スポンジSP')
    get_data('シュアラスター　スポンジ')
    get_data('ブリス　スポンジSP')
    get_data('フエキ　工業用 KGM')
    get_data('リンレイ　水アカスポットクリーナー')
    pass


    
