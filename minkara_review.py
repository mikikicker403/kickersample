#-*- coding:utf=8-*-
import gethtml_and_soup
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('program start')
logging.disable(logging.DEBUG)
#logging.disable(logging.CRITICAL)

import re,sys,random,time,pickle
import sqlite3 as db
import queue
import threading

class Send_To_Semaphore(threading.Thread):
    def __init__(self,url,semaphore):
        self.semaphore=semaphore

    def run(self):
        self.semaphore.put(url)

class Get_From_Queue(threading.Thread):
    def __init__(self,queue,queue2):
        super(Get_From_Queue,self).__init__()
        self.queue=queue
        self.queue2=queue2
    def run(self):
        rdelete=re.compile(r'\r')
        ndelete=re.compile(r'\n')
        while True:
            url=self.queue.get()
            logging.warning('NAME:{name}---{url}'.format(name=self.getName(),url=url))
            #print(url)
            if url == None:
                break
            time.sleep(10)
            ob=gethtml_and_soup.Gethtml_and_soup(url,random.randint(10,30))
            try:
                html=ob.gethtml()
                soup=ob.getsoup()
            except Exception as e:
                print(e,':row33')
            try:
                ob.title=ob.soup.find('h1').text
                ob.title=rdelete.sub('',ob.title)
                ob.title=ndelete.sub('',ob.title)
            except Exception as e:
                print(e,':row39')
                ob.title='=NO DATA='
            try:
                ob.content=ob.soup.find('div',{'class':'userCarPhotoMemo'}).text
                ob.content=rdelete.sub('',ob.content)
                ob.content=ndelete.sub('',ob.content)
            except Exception as e:
                print(e,'NAME:{name}--:row46'.format(name=self.getName()))
                ob.content='=NO DATA='
            try:
                ob.owner=ob.soup.find('h2',{'class':'car_title car_header'}).text
            except Exception as e:
                print(e,'NAME:{name}--:row51'.format(name=self.getName()))
                ob.owner='=NO DATA='

            #print(ob.title,ob.owner,ob.url,ob.content)
            logging.debug('{title}({owner})--{url}--{content}'.format(title=ob.title,owner=ob.owner,url=ob.url,content=ob.content))
            self.queue2.put((ob.url,ob.title,ob.owner,ob.content))


class Minkara:
    def __init__(self,url):
        self.baseurl=url+'&pn={page}'
        self.urlheader='https://minkara.carview.co.jp'
        self.links={}

    def getlinks(self):
        for i in range(1,50):
            print('page:',i)
            self.url=self.baseurl.format(page=i)
            self.ob=gethtml_and_soup.Gethtml_and_soup(self.url,random.randint(10,30))
            try:
                html=self.ob.gethtml()
            except Exception as e:
                print(e)
                break
            self.ob.getsoup()
            self._spoitlink()
            self._getdetail()
            self.save_contents()

    def _spoitlink(self):
        ret=self.ob.soup.findAll('div',{'class':'contents-right505'})
        if len(ret)==0:
            print('div class contents-right505 not found.maybe entry is finished')
            raise
        for w in ret:
            #print(w.find('a').text)
            #print(w.find('a').get('href'))
            self.links.setdefault(self.urlheader+w.find('a').get('href'),{})
            self.links[self.urlheader+w.find('a').get('href')]['linktext']=w.find('a').text

    def _getdetail(self):
        rdelete=re.compile(r'\r')
        ndelete=re.compile(r'\n')
        for url in self.links.keys():
            ob=gethtml_and_soup.Gethtml_and_soup(url,random.randint(10,30))
            try:
                html=ob.gethtml()
                soup=ob.getsoup()
                title=ob.soup.find('h1').text
                title=rdelete.sub('',title)
                title=ndelete.sub('',title)
                content=ob.soup.find('div',{'class':'userCarPhotoMemo'}).text
                content=rdelete.sub('',content)
                content=ndelete.sub('',content)
                owner=ob.soup.find('h2',{'class':'car_title car_header'}).text
            except Exception as e:
                print(e)
                print('url:{url}'.format(url=url))
                title='=NODATA='
                content='=NODATA='
                owner='=NODATA='

            self.links[url]['title']=title
            self.links[url]['content']=content
            self.links[url]['ownerdetail']=owner


class Minkara_carview(Minkara):
    def __init(self,url):
        super().__init__('')

class Minkara_review:

    def __init__(self,url):
        self.baseurl=url+'&pn={page}'
        self.urlheader='https://minkara.carview.co.jp'
        self.links={}
            
    def getlinks(self):
        for i in range(1,50):
            print('page:',i)
            self.url=self.baseurl.format(page=i)
            self.ob=gethtml_and_soup.Gethtml_and_soup(self.url,random.randint(10,30))
            try:
                html=self.ob.gethtml()
            except Exception as e:
                print(e)
                break
            self.ob.getsoup()
            self._spoitlink()
            self._getdetail()
            self.save_contents()

    def getlinks_multi(self):
        for i in range(1,50):
            print('page:',i)
            self.url=self.baseurl.format(page=i)
            self.ob=gethtml_and_soup.Gethtml_and_soup(self.url,random.randint(10,30))
            try:
                html=self.ob.gethtml()
                soup=self.ob.getsoup()
                self._spoitlink()
            except Exception as e:
                print(e)
                break
        self._getdetail_multi()
        self.save_contents()
    def getlinks_multi_semaphore(self):
        for i in range(1,50):
            print('page:',i)
            self.url=self.baseurl.format(page=i)
            self.ob=gethtml_and_soup.Gethtml_and_soup(self.url,random.randint(10,20))
            try:
                html=self.ob.gethtml()
                soup=self.ob.getsoup()
                self._spoitlink()
            except Exception as e:
                print(e)
                break
        self._getdetail_multi()
        self.save_contents()

    def getlinks_multi_queue(self):
        for i in range(1,50):
            print('page:',i)
            self.url=self.baseurl.format(page=i)
            self.ob=gethtml_and_soup.Gethtml_and_soup(self.url,random.randint(10,20))
            try:
                html=self.ob.gethtml()
                soup=self.ob.getsoup()
                self._spoitlink()
            except Exception as e:
                print(e)
                break
        self._getdetail_multi_queue()
        self.save_contents()


    def _spoitlink(self):
        ret=self.ob.soup.findAll('div',{'class':'contents-right505'})
        if len(ret)==0:
            print('div class contents-right505 not found.maybe entry is finished')
            raise
        for w in ret:
            #print(w.find('a').text)
            #print(w.find('a').get('href'))
            self.links.setdefault(self.urlheader+w.find('a').get('href'),{})
            self.links[self.urlheader+w.find('a').get('href')]['linktext']=w.find('a').text

    def _getdetail(self):
        rdelete=re.compile(r'\r')
        ndelete=re.compile(r'\n')
        for url in self.links.keys():
            ob=gethtml_and_soup.Gethtml_and_soup(url,random.randint(10,30))
            try:
                html=ob.gethtml()
                soup=ob.getsoup()
                title=ob.soup.find('h1').text
                title=rdelete.sub('',title)
                title=ndelete.sub('',title)
                content=ob.soup.find('div',{'class':'userCarPhotoMemo'}).text
                content=rdelete.sub('',content)
                content=ndelete.sub('',content)
                owner=ob.soup.find('h2',{'class':'car_title car_header'}).text
            except Exception as e:
                print(e)
                print('url:{url}'.format(url=url))
                title='=NODATA='
                content='=NODATA='
                owner='=NODATA='

            self.links[url]['title']=title
            self.links[url]['content']=content
            self.links[url]['ownerdetail']=owner
    def _getdetail_multi(self):
        rdelete=re.compile(r'\r')
        ndelete=re.compile(r'\n')
        self.threadings=[]
        #i=1
        for url in self.links.keys():
            #print('number:{num}'.format(num=i))
            ob=gethtml_and_soup.Gethtml_and_soup_multi(url,random.randint(10,30))
            ob.start()
            self.threadings.append(ob)
            print('gethtml_and\soup_multi_finish:{url}'.format(url=url))
            #i+=1

        for ob in self.threadings:
            ob.join()
        else:
            print('threading is completed !!')

        for ob in self.threadings:
            ob.title=ob.soup.find('h1').text
            ob.title=rdelete.sub('',ob.title)
            ob.title=ndelete.sub('',ob.title)
            ob.content=ob.soup.find('div',{'class':'userCarPhotoMemo'}).text
            ob.content=rdelete.sub('',ob.content)
            ob.content=ndelete.sub('',ob.content)
            ob.owner=ob.soup.find('h2',{'class':'car_title car_header'}).text
            print(ob.title,ob.owner,ob.url,ob.content)
        for ob in self.threadings:
            url=ob.url
            self.links[url]['title']=ob.title
            self.links[url]['content']=ob.content
            self.links[url]['ownerdetail']=ob.owner


    def _getdetail_multi_queue(self):
        rdelete=re.compile(r'\r')
        ndelete=re.compile(r'\n')
        self.threadings=[]
        putqueue=queue.Queue()
        resultqueue=queue.Queue()

        #get_queue
        ob1=Get_From_Queue(putqueue,resultqueue)
        ob1.setName('no1')
        ob1.start()
        ob2=Get_From_Queue(putqueue,resultqueue)
        ob2.setName('no2')
        ob2.start()
        ob3=Get_From_Queue(putqueue,resultqueue)
        ob3.setName('no3')
        ob3.start()
        threadings=[ob1,ob2,ob3]
        for url in self.links.keys():
            #print('number:{num}'.format(num=i))
            putqueue.put(url)
        else:
            putqueue.put(None)
            putqueue.put(None)
            putqueue.put(None)
            for ob in threadings:
                ob.join()
                resultqueue.put(None)
                
        while True:
            tup=resultqueue.get()
            if tup ==None:
                print('find resultque None!resultqueue.get finish')
                break
            else:
                print('not find resultque None.')
            url=tup[0]
            title=tup[1]
            ownerdetail=tup[2]
            content=tup[3]
            #print(url,title,ownerdetail,content)
            self.links[url]['title']=title
            self.links[url]['content']=content
            self.links[url]['ownerdetail']=ownerdetail
        







    def save_contents(self,fname='minkara_contents.html'):
        total_tex=''
        baseheader='<a href="#{id}">#{id}</a> / '
        total_header=''
        basehtml='''
<!DOCTYPE html>
<html lang='ja'>
<head>
    <meta charset='UTF-8'>
    <title>contents</title>
</head>
<body>
    {header}
    <hr>
    {total_tex}
</body>
</html>
        '''
        basetex='''
title:<h2 class="title" id="{id}">{title} {id}</h2></br>
url:<a href="{url}">{url}</a></br>
owner:{owner}</br>
=contents=</br>
<p><font size="4">{contents}</font></p></br>
<hr></br></br>
        '''
        pickle.dump(self.links,open('test.dump','wb'))
        for id,url in enumerate(self.links.keys()):
            #print(self.links[url].items())
            #print(len(self.links[url].items()))
            try:
                title=self.links[url]['title']
            except Exception as e:
                print(e)
                title='=NO TITLE='
            try:
                contents=self.links[url]['content']
            except Exception as e:
                print(e)
                contents='= NO CONTENTS ='
            try:
                owner=self.links[url]['ownerdetail']
            except Exception as e:
                print(e)
                owner='=NO DATA='
            tex=basetex.format(id=id,title=title,url=url,contents=contents,owner=owner)
            total_tex+=tex
            total_header+=baseheader.format(id=id)
        else:
            savehtml=basehtml.format(header=total_header,total_tex=total_tex)

        with open(fname,'w') as f:
            f.write(savehtml)
            print(fname,'save completed')
    def load_data(self):
        d=pickle.load(open('test.dump','rb'))
        self.links=d
    def insertdb(self):
        self.load_data()
        with db.connect('minkara.db') as con:
            con.execute('create table if not exists contents(url text,title text,owner text,contents text)')
        for k in self.links.keys():
            url=k
            title=self.links[k].get('title','= NO TITLE =')
            owner=self.links[k].get('ownerdetail','= NO DATA =')
            contents=self.links[k].get('content','= NO CONTENTS =')
            insertsql='insert into contents(url,title,owner,contents) values(?,?,?,?)'
            with db.connect('minkara.db') as con:
                try:
                    con.execute(insertsql,(url,title,owner,contents))
                    con.commit()
                except Exception as e:
                    print(e,':r329')

class Minkara_review_in_goods(Minkara_review):
    def __init__(self,keywords):
        super().__init__('')
        self.keywords=' '.join(keywords)
        self.keywords=re.sub(r'　',' ',self.keywords)
        self.keywords=re.sub(r' ','+',self.keywords)
        self.baseurl='https://minkara.carview.co.jp/search/?q={keywords}&c=104'.format(keywords=self.keywords)+'&p={page}'
        logging.warning(self.baseurl)

    #@override 
    def _spoitlink(self):
        logging.warning(self.ob.url)
        ret=self.ob.soup.findAll('ul',{'class':'item'})
        ret2=ret[0].findAll('div',{'class':'textarea'})
        for w in ret2:
            print(w.find('a').text,w.find('a').get('href'))
            url='http:'+w.find('a').get('href')
            self.links.setdefault(url,{})

    #@override
    def getlinks(self):
        for i in range(1,50):
            print('page:',i)
            self.url=self.baseurl.format(page=i)
            self.ob=gethtml_and_soup.Gethtml_and_soup(self.url,random.randint(10,30))
            try:
                html=self.ob.gethtml()
                soup=self.ob.getsoup()
                self._spoitlink()
            except Exception as e:
                print(e)
                break
        for k in self.links.keys():
            insertsql='insert into links(url) values(?)'
            with db.connect('minkara.db') as con:
                try:
                    con.execute('create table if not exists links(url text unique)')
                    con.commit()
                    con.execute(insertsql,(k,))
                    con.commit()
                except Exception as e:
                    print(e,k)
    def getcontents(self):
        self.links={}
        with db.connect('minkara.db') as con:
            ret=con.execute('select * from links')
            ret2=ret.fetchall()
            for w in ret2:
                self.links.setdefault(w,{})
        self._getdetail_multi_queue()



if __name__=='__main__':
    if sys.argv[1]=='keyword':
        print('keyword')
        ob=Minkara_review_in_goods(sys.argv[2:])
        ob.getlinks()
    elif sys.argv[1]=='contents':
        ob=Minkara_review_in_goods(sys.argv[2:])
        ob.getcontents()
        ob.load_data()
        ob.insertdb()
    elif sys.argv[1]=='url':
        url=sys.argv[2]
        ob=Minkara_review(url)
        ob.getlinks_multi_queue()
    elif sys.argv[1]=='carview':
        url=sys.argv[2]
        ob=Minkara_carreview(url)
        ob.getlinks_multi_queue()
    else:
        print('argv[2] is not match')
    print('minkara_review.py is finished')

