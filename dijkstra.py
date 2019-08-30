# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:56:33 2019

@author: zforw
"""

import networkx as nx

inf = 2147483647

dis = {}
def Dijkstra(G,st):
    
    for v in G.nodes():
        dis[v] = inf
    dis[st] = 0
    for i in G.nodes:
        for i,j in G.edges:
            if dis[j] > dis[i] + G[i][j]['weight']:
                dis[j] = dis[i] + G[i][j]['weight']
    return
        
        
G = nx.DiGraph()
n,m,s = map(int,input().split())
for i in range(m):
    u,v,c = map(int,input().split())
    G.add_edge(u,v,weight = c)
    
Dijkstra(G,s)
ans = ''
for i in range(1,n+1):
    ans = ans + str(dis[i]) + ' '
print(ans)