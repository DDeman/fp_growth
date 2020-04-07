#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '任晓光'
__mtime__ = '2020/3/29'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
class treeNode():
    def __init__(self,nameValue,numOccur,parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}
    def inc(self,numOccur):
        self.count += numOccur
    def disp(self,ind = 1):
        print(' '*ind,self.name,' ',self.count)
        for child in self.children.values():
            child.disp(ind + 1)
def updateHeader(nodeToTest,targetNode):

    while nodeToTest.nodeLink != None:
        nodeToTest = nodeToTest.nodeLink

    nodeToTest.nodeLink = targetNode

def updateTree(items,myTree,headerTable,count):
    # print(items)
    if items[0] in myTree.children:
        myTree.children[items[0]].inc(count)
    else:
        myTree.children[items[0]] = treeNode(items[0],count,myTree)
        if headerTable[items[0]][1] == None:
            headerTable[items[0]][1] = myTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1],myTree.children[items[0]])
    if len(items) > 1:
        updateTree(items[1:],myTree.children[items[0]],headerTable,count)


def createTree(data, minSup=3):
    headerTable = {}
    for trans in data:
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + 1
            #             print(headerTable)

    lessThanMinsup = list(filter(lambda k: headerTable[k] < minSup, headerTable.keys()))
    for k in lessThanMinsup:
        del (headerTable[k])
    freqItemSet = set(headerTable.keys())

    #     print('freqItemSet',freqItemSet)

    if len(freqItemSet) == 0:
        return None, None

    for k in headerTable:
        headerTable[k] = [headerTable[k], None]
    myTree = treeNode('%%', 1, None)
    #     print('this is headerTable',headerTable)
    for tranSet, count in data.items():
        localD = {}
        for item in tranSet:
            localD[item] = headerTable[item][0]
        # print(localD)
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: (p[1], p[0]), reverse=True)]
            # print('khiwejqr',orderedItems)
            updateTree(orderedItems, myTree, headerTable, count)
    return myTree, headerTable


def createinitset(data):
    retDict = {}
    for trans in data:
        fest = frozenset(trans)
        retDict.setdefault(fest,0)
        retDict[fest] += 1
    return retDict
if __name__ == '__main__':
    data = [['牛奶', '鸡蛋', '面包', '薯片']
        , ['鸡蛋', '爆米花', '薯片', '啤酒']
        , ['牛奶', '面包', '啤酒']
        , ['牛奶', '鸡蛋', '面包', '爆米花', '薯片', '啤酒']
        , ['鸡蛋', '面包', '薯片']
        , ['鸡蛋', '面包', '啤酒']
        , ['牛奶', '面包', '薯片']
        , ['牛奶', '鸡蛋', '面包', '黄油', '薯片']
        , ['牛奶', '鸡蛋', '黄油', '薯片']]

    retDict = createinitset(data)
    myTree, headerTable = createTree(retDict, 1)
    # print(myTree.disp())