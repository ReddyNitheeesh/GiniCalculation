# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 06:53:01 2019

@author: nitheesh reddy gaddam
"""

import pandas as pd

data=pd.read_excel('test.xlsx')

#To find root node
#Finding impurity at each column

#this method accepts three parameter's data,specific column to which gini will be calculated,target column
def calculateGini(data,col,target):
    leftYes=0
    leftNo=0
    rightYes=0
    rightNo=0
    for i1,i2 in zip(data[col],data[target]):
        if i2=='Yes':        
            if i1.strip()==i2.strip():
                leftYes+=1
            else:
                leftNo+=1
        else:
            if i1.strip()==i2.strip():
                rightNo+=1
            else:
                rightYes+=1
    #calculate right gini
    #formula 1-p(yes)**2-p(No)**2
    lefttotal=leftYes+leftNo
    righttotal=rightYes+rightNo            
            
    ginileft=1-(leftYes/lefttotal)**2-(leftNo/lefttotal)**2
    giniright=1-(rightYes/righttotal)**2-(rightNo/righttotal)**2
    #total weighted average multiply with gini of that node
    total=lefttotal+righttotal
    return (lefttotal/total)*ginileft+(righttotal/total)*giniright

##Forming column least by removing target varibable
listColumns=[i for i in data.columns if i.strip() not in 'HeartDisease']
dictGini={}
for col in listColumns:
    dictGini[col]=calculateGini(data,col,'HeartDisease')

##Best split column feature based on Gini
rootColumn=[key for key,value in dictGini.items() if value==min(dictGini.values())][0]






