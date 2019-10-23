
#-*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('program start')
#logging.disable(logging.CRITICAL)

import networkx as nx
import matplotlib.pyplot as plt

class DrawNetwork:
    def __init__(self,fname):
        self.fname=fname
        self.font_family='Noto Sans CJK JP'
        self.edges=[]
        self.g=nx.Graph()

    def read_file(self):
        with open(self.fname,'r') as f:
            for l in f.readlines():
                lt=l.strip().split(',')
                if len(lt)==2:
                    self.edges.append((lt[0],lt[1]))
                elif len(lt)==3:
                    self.edges.append((lt[0],lt[1],lt[2]))
    def add_data(self):
        self.g.add_edges_from(self.edges)
    def add_nodes(self,dic={}):
        for k in dic.keys():
            for k2,v in dic[k].items():
                print(k,k2,v)
                self.g.nodes[k][k2]=v
        
    def draw_network(self,figname='test.svg'):
        pos=nx.spring_layout(self.g)
        
        #node
        #node_shape s0^>V<dph8
        node_colors=[self.g.nodes.get(w).get('nodecolor','blue') for w in self.g.nodes]
        node_size=[self.g.nodes.get(w).get('nodesize',1) for w in self.g.nodes]
        node_alpha=[self.g.nodes.get(w).get('nodealpha',0.5) for w in self.g.nodes]
        print(node_colors)
        print(node_size)
        print(node_alpha)
        nx.draw_networkx_nodes(self.g,pos,node_color=node_colors,node_size=node_size,alpha=node_alpha)

        #node label
        #font_family font_color:string only //  font_size int only
        #nx.draw_networkx_labels(self.g,pos,font_family=self.font_family,font_size=5,font_color='black',alpha=0.8)
        labeldic={w:i for i,w in enumerate(self.g.nodes)}
        nx.draw_networkx_labels(self.g,pos,labels=labeldic,font_family=self.font_family,font_size=5,font_color='black',style='bold',alpha=1.0)
        

        #edge draw
        #style solid/dashed/dotted dashdot only
        edge_widths=[self.g.edges.get(w).get('edgewidth',1.0) for w in self.g.edges]
        edge_colors=[self.g.edges.get(w).get('edgecolor','black') for w in self.g.edges]
        nx.draw_networkx_edges(self.g,pos,width=edge_widths,edge_color=edge_colors,style='solid',alpha=0.3)
        
        #edge label
        #edgelabeldic={w:float(self.g.edges.get(w).get('width',1)) for w in self.g.edges} 
        #nx.draw_networkx_edge_labels(self.g,pos,edge_labels=edgelabeldic,alpha=0.5)


        plt.xticks([])
        plt.yticks([])
        plt.savefig(figname,dpi=1200)

        self.revlabeldic={}
        self.labeldic=labeldic
        for k,v in labeldic.items():
            print(k,v)
            self.revlabeldic[v]=k
    def search_label_from_id(self,num):
        print('ID:{id} / Label:{label}'.format(id=num,label=self.revlabeldic.get(num,'')))

    def cut_tree(self):
        remove_node=[]
        for w in self.g.degree():
            print(w)
            if w[1]<=1:
                print(w[0],w[1])
                remove_node.append(w[0])
        self.g.remove_nodes_from(remove_node)

if __name__=='__main__':
    ob=DrawNetwork('test.csv')
    ob.read_file()
    node_dic={'リンレイ　水アカスポットクリーナー':{'nodecolor':'r','nodesize':20 },'シュアラスター　スポンジ':{'nodecolor':'r','nodesize':20 },'ブリス　スポンジSP':{'nodecolor':'r','nodesize':20 },'フエキ　工業用 KGM':{'nodecolor':'r','nodesize':20 },'クリンビュー　水垢リムーバー':{'nodecolor':'r','nodesize':20 }}
    ob.add_data()
    ob.add_nodes(node_dic)
    ob.cut_tree()
    ob.draw_network('test.svg')

    
