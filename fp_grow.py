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
    def __init__(self,nameValue,count,parent=None):
        self.name = nameValue
        self.count = count
        self.parent = parent
        self.linknode = None
        self.children = {}
    def inc(self,count):
        self.count += count

    def disp(self,ind):
        print(' '*ind,' ',self.name,'   ',self.count)
        for child in self.children.values():
            child.disp(ind+1)

def createtrainset(data):
    retDict = dict()
    for item in data:
        retDict.setdefault(frozenset(item),0)
        retDict[frozenset(item)] += 1
    return retDict

def createTree(retDict,minSub=3):
    headnode = {}
    for item in retDict.items():
        for tran in item[0]:
            headnode[tran] = headnode.get(tran,0) + 1

    lessThanminSub = list(filter(lambda k:headnode[k] < minSub,headnode.keys()))
    for i in lessThanminSub:
        del(headnode[i])
    # print(headnode)
    freqItemSet = set(headnode.keys())
    print('this is freq',freqItemSet)
    if len(headnode) == 0:
        return None,None,None

    for k in headnode:
        headnode[k] = [headnode[k],None]
    mytree = treeNode('***',1)
    # print(headnode)
    for item in retDict:
        # print(item)
        count = retDict[item]
        localD = dict()
        for tem in item:
            if tem in headnode:
                localD[tem] = headnode[tem][0]
        if len(localD) > 0:

            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: (p[1], p[0]), reverse=True)]
        # print(orderedItems)
        updatatree(orderedItems,mytree,headnode,count)
        '''
        for fe in orderedItems:
            if fe in mytree.children:
                mytree.children[fe].inc(count)
            else:
                mytree.children[fe] = treeNode(fe,count,mytree)
                if headnode[fe][1] == None:
                    headnode[fe][1] = mytree.children[fe]
                else:
                    nodeTotest = headnode[fe][1]
                    targettest = mytree.children[fe]
                    while nodeTotest.linknode != None:
                        nodeTotest = nodeTotest.linknode
                    nodeTotest.linknode = targettest
        '''
    return mytree, headnode,freqItemSet

def updatatree(orderedItems,mytree,headnode,count):
    if orderedItems[0] in mytree.children:
        mytree.children[orderedItems[0]].inc(count)
    else:
        mytree.children[orderedItems[0]] = treeNode(orderedItems[0],count,mytree)
        if headnode[orderedItems[0]][1] == None:
            headnode[orderedItems[0]][1] = mytree.children[orderedItems[0]]
        else:
            nodeTotest = headnode[orderedItems[0]][1]
            targettest = mytree.children[orderedItems[0]]
            while nodeTotest.linknode != None:
                nodeTotest = nodeTotest.linknode
            nodeTotest.linknode = targettest
    if len(orderedItems) > 1:
        updatatree(orderedItems[1:],mytree.children[orderedItems[0]],headnode,count)

def print_headnode(headnode):
    def preint(headnode, name):
        node_next = headnode[name][1]
        while node_next is not None:
            print(node_next.name, node_next.count, end='-->')
            node_next = node_next.linknode
    for name in headnode:
        print('')
        print(name,headnode[name][0],end='-->')
        preint(headnode,name)

###挖掘频繁项集

def pattern_base(headnode,name_=[]):
    if headnode is None:
        # print(name_)
        return
    headnode_name_list = [i for i in headnode]
    # print(headnode_name_list)
    # print('this is headnode',headnode)
    for i in range(len(headnode_name_list)-1,-1,-1):
        name = headnode_name_list[i]
        # print(i)
        temp = dict()
        count = headnode[name][0]
        node_next = headnode[name][1]
        while node_next is not None:
            node_par = node_next
            tem = []
            while node_par.parent is not None:
                tem.append(node_par.parent.name)
                node_par = node_par.parent
            # print(node_next.name, node_next.count, end='-->')
            tem.pop()
            '''
            if tem != []:
                temp[frozenset(tem)] = node_next.count
            else:
                name_.append(name)
                name_.append(node_next.count)
                print(name_)
                # print(node_next.count)
            '''
            temp[frozenset(tem)] = node_next.count
            node_next = node_next.linknode


        # print('++++',name)
        print(name,'%%%%%%%%%%%%%%%%%%5',temp)
        mytree_, headnode_, fre_set_ = createTree(temp)
        # print(headnode_)
        # print(fre_set)
        pattern_base(headnode_,name_)

# def pattern_base(headnode,name):
#     headnode_name_list = [i for i in headnode]
#     for i in range(len(headnode_name_list) - 1, -1, -1):
#         name = headnode_name_list[i]
#         temp = dict()
#         count = headnode[name][0]
#         node_next = headnode[name][1]
#         while node_next is not None:
#             node_par = node_next
#             tem = []
#             while node_par.parent is not None:
#                 tem.append(node_par.parent.name)
#                 node_par = node_par.parent
#             # print(node_next.name, node_next.count, end='-->')
#             tem.pop()
#             if tem != []:
#                 temp[frozenset(tem)] = node_next.count
#             else:
#                 print(node_next.count)
#             node_next = node_next.linknode
#         print('%%%%%%%%%%%%%%%%%%5', temp)
#         mytree, headnode, fre_set = createTree(temp)
#         # print(fre_set)
#         pattern_base(headnode)

# def tttt(headnode):
#
#     headnode_name_list = [i for i in headnode]
#     for i in range(len(headnode_name_list)-1,-1,-1):
#         name = headnode_name_list[i]
#         pattern_base(headnode, name)




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
    # data = [[]]
    retDict = createtrainset(data)
    # print(retDict)

    # retDict = {frozenset({'鸡蛋'}): 2}
    # retDict = {frozenset({}):2}
    mytree, headnode,freqItemSet = createTree(retDict)
    # print(headnode)
    pattern_base(headnode)

'''
    mytree.disp(1)
    print(headnode)
    # for i in headnode:

    def print_headnode(headnode):
        def preint(headnode, name):
            temp = []
            count = headnode[name][0]
            node_next = headnode[name][1]
            # node_par = headnode[name][1]
            # while node_par.parent is not None:
            #     temp.append(node_par.parent.name)
            #     node_par = node_par.parent
            # print('^^^^')
            # print(temp)
            # print('^^^^^^')

            while node_next is not None:
                node_par = node_next
                tem = []
                while node_par.parent is not None:
                    tem.append(node_par.parent.name)
                    node_par = node_par.parent
                # print(node_next.name, node_next.count, end='-->')
                node_next = node_next.linknode
                tem.pop()
                temp.append(tem)
            data = createtrainset(temp)
            print(data)
        for name in headnode:
            # print(name, headnode[name][0], end='-->')
            preint(headnode, name)

    print_headnode(headnode)
    print('****')
    print(mytree.children['鸡蛋'].parent.name)
    '''