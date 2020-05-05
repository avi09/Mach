import pandas as dd
from igraph import * 

import sys
import numpy as ss
from numpy.linalg import norm
ny=1
def dq(r,g,i1,i2,a,md2,x2):
    global ny
    g2=[i for i in g]
    g2[i1]=i2
    nt=i2
    x=ts(r,g)
    g2=align(g2)
    md=r.modularity(g2)
    return (a*(md-md2))+((1-a)*(x-x2))
    
def ts(r,g):
    global ny
    g2=[i for i in g]
    s=0
    x=[]
    for j in range(len(g2)):
        if g2[j]==ny:
            x.append(j)
    for x1 in x:
        for x2 in x:
             if x1!=x2:
                s+=sim(list(r.vs[x1].attributes().values()),list(r.vs[x2].attributes().values()))

    return s
def align(x):
    y={}
    nn=0
    for i in x:
        if not i in y.keys():
            y[i]=nn
            nn+=1
    for i in range(len(x)):
        x[i]=y[x[i]]
        
    return x     
def sim(a,b):
    return ss.dot(a,b)/(norm(a)*norm(b))

g=Graph()
n=dd.read_csv("./data/fb_caltech_small_edgelist.txt")
nn=[]
nx=[]
for i in range(len(n.iloc[:,:])):
    nn.append((int(n.iloc[:,0][i].split(" ")[0]),int(n.iloc[:,0][i].split(" ")[1])))

    nx.append(nn[i][0])
    nx.append(nn[i][1])

nx=list(set(nx))
g.add_vertices(len(nx))
g.add_edges(nn)

n=dd.read_csv("./data/fb_caltech_small_attrlist.csv")
for i in n.columns:
    g.vs[str(i)]=list(n.loc[:,i])
it=1
mg=1
gr=[]
for i in range(len(nx)):
    gr.append(i)
a=float(sys.argv[1])
while mg>0 and it<=16:
    tm=[]
    x2=ts(g,gr)
    md2=g.modularity(gr)
    for i in range(len(nx)):
        mg=0
        y=set(gr)
        for j in y:
            if not j==gr[i]:
                gg=dq(g,gr,i,j,a,md2,x2)
                if gg>mg:
                    mg=gg
                    tm=[i,j]
        if mg>0:
            gr[tm[0]]=tm[1] 
    an=align(gr)

st=set(an)
nn=[]
for i in st:
    tm=[]
    for j in range(len(an)):
        if an[j]==i:
            tm.append(j)
    nn.append(tm)

print(nn)
if a<0.8 and a>0:
    y='communities_'+str(a)[2]
elif a==1.0:
    y='communities_1'
else:
    y='communities_0'
f=open(y+'.txt',"w+")
for i in nn:
    x=str(i)
    f.writelines(str(x)[1:len(x)-1]+"\n")
f.close()
    
            


    