#-*- coding:utf=8-*-

import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('program start')
#logging.disable(logging.CRITICAL)

import requests,sys
#import urllib
import bs4
import os,time
import threading

'''
'''

class Gethtml_and_soup_multi(threading.Thread):
    def __init__(self,url,sleeptime=15):
        super(Gethtml_and_soup_multi,self).__init__()
        #super().__init__()
        self.url=url
        self.html=''
        self.soup=''
        self.sleeptime=sleeptime
        pass
    def _gethtml(self):
        time.sleep(self.sleeptime)
        #logging.debug(self.url)
        logging.critical(self.url)
        self.html=requests.get(self.url).text
        #return self.html
    def _getsoup(self):
        self.soup=bs4.BeautifulSoup(self.html)
    def run(self):

        self._gethtml()
        self._getsoup()
        pass

class Gethtml_and_soup:
    def __init__(self,url,sleeptime=15):
        logging.debug('Gethtml object create')
        self.url=url
        self.html=''
        self.soup=''
        self.sleeptime=sleeptime

    def gethtml(self):
        time.sleep(self.sleeptime)
        self.html=requests.get(self.url).text
        return self.html
    def getsoup(self):
        self.soup=bs4.BeautifulSoup(self.html)
        return self.soup


if __name__=='__main__':

    url=sys.argv[1]
    ob=Gethtml_and_soup(url)
    ob.gethtml()
    ob.getsoup()
    pass
