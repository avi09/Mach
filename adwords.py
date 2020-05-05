import pandas as dd
import random

from math import e
import sys

if len(sys.argv)==1:
    print('No arguments')
elif sys.argv[1]=='greedy' or sys.argv[1]=='mssv' or sys.argv[1]=='balanced':
    print('Running algorithm for '+sys.argv[1]+" now. This may take some time")

data=dd.read_csv('./bidder_dataset.csv')
q=dd.read_csv('queries.txt',header=None)

def search(q,data):
    an=[]
    for i in range(len(data)):
            if q==data[i][1]:
                an.append([data[i][0],data[i][2]])
    return an

data1=[]
for i in range(len(data.iloc[:,1])):
    data1.append([data.loc[i,'Advertiser'],data.iloc[i,1],data.iloc[i,2]])

budget={}
for i in range(len(data1)):
    if str(data.loc[i,'Budget'])!='nan':
        budget[data1[i][0]]=data.loc[i,'Budget']
budget1=dict(zip(budget.keys(),budget.values()))
rv=0
random.seed(0)
q1=[]
for i in range(len(q)):
    q1.append(q.iloc[i,0])





def greedy(budget,budget1,q1,data1):
    budget1=dict(zip(budget.keys(),budget.values()))
    rv=0
    for i in range(len(q1)):
        x=str(q1[i])
        x=search(x,data1)
        x=sorted(x,key=lambda x:x[1])
        mx=x[-1][1]
        y=[]
        cn=-1
        for k in range(len(x)):
            if x[k][1]==mx:
                cn+=1
        cn1=x[(len(x)-cn-1):]
        cn1=sorted(cn1,key=lambda x:x[0],reverse=True)
        x=x[:len(x)-cn-1]+cn1
        for j in reversed(x):
            if budget1[j[0]]-j[1]>0:
                budget1[j[0]]=budget1[j[0]]-j[1]
                rv+=j[1]
                break
    return rv

def msvv(budget,budget1,q1,data1):
    budget1=dict(zip(budget.keys(),budget.values()))
    rv=0
    for i in range(len(q1)):
        x=str(q1[i])
        x=search(x,data1)
        for j in x:
            j.append(j[1]*(1-(e**(((budget[j[0]]-budget1[j[0]])/budget[j[0]])-1))))
        x=sorted(x,key=lambda x:x[2])
        mx=x[-1][2]
        xy=-1
        for k in range(len(x)):
            if x[k][2]==mx:
                xy+=1
        xx=x[(len(x)-xy-1):]
        xx=sorted(xx,key=lambda x:x[0],reverse=True)
        x=x[:len(x)-xy-1]+xx
        for j in reversed(x):
            if budget1[j[0]]-j[1]>0:
                budget1[j[0]]=budget1[j[0]]-j[1]
                rv+=j[1]
                break
    return rv

def balanced(budget,budget1,q1,data1):
    budget1=dict(zip(budget.keys(),budget.values()))
    rv=0
    for i in range(len(q1)):
        x=str(q1[i])
        x=search(x,data1)
        for j in x:
            j.append(budget1[j[0]])
        x=sorted(x,key=lambda x:x[2])
        mx=x[-1][2]
        xy=-1
        for k in range(len(x)):
            if x[k][2]==mx:
                xy+=1
        xx=x[(len(x)-xy-1):]
        xx=sorted(xx,key=lambda x:x[0],reverse=True)
        x=x[:len(x)-xy-1]+xx
        for j in reversed(x):
            if budget1[j[0]]-j[1]>0:
                budget1[j[0]]=budget1[j[0]]-j[1]
                rv+=j[1]
                break
    return rv

x=0
if sys.argv[1]=='greedy':
    for i in range(-1,100):
        if i==-1:
            print("Original query")
        else:
            random.seed(i)
            random.shuffle(q1)
        y=greedy(budget,budget1,q1,data1)
        if i==-1:
            print("For greedy, iteration 1 - "+str(y))
        else:
            x+=y
    print("The ratio - "+ str(((x/sum(budget.values()))/100)))
x=0
if sys.argv[1]=='mssv':
    for i in range(-1,100):
        if i==-1:
            print("Original query")
        random.seed(i)
        random.shuffle(q1)
        y=msvv(budget,budget1,q1,data1)
        if i==-1:
            print("For mssv, iteration 1 - "+str(y))
        else:
            x+=y
    print("The ratio "+str((x/sum(budget.values()))/100))

x=0
if sys.argv[1]=='balanced':
    for i in range(-1,100):
        if i==-1:
            print("Original query")
        else:
            random.seed(i)
            random.shuffle(q1)
        y=balanced(budget,budget1,q1,data1)
        if i==-1:
            print("For balanced, iteration 1 - "+str(y))
        else:
            x+=y
    print("The ratio "+str(((x/sum(budget.values()))/100)))





