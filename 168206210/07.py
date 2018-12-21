# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:17:07 2018

@author: CXL
"""

start = "hit"
end = "cog"
adict = ["hot", "dot", "dog", "lot", "log"]


def find_path(start, end, paths) :
    if start == end :
        return "start=end"
    else :
        visited = []    #存放路径的队列
        visited.append(start)
        paths.append(end)
        for word in visited :   #遍历队列中每个单词
            for i in range(len(word)) : #遍历单词中每个字母
                for j in range(97, 123) : #遍历26个字母
                    word = visited[-1]
                    newword = word[:i] + chr(j) + word[i+1:] #替换字母                                
                    if newword in paths and newword not in visited :  #新单词在队列中存在且不在路径队列中时
                        visited.append(newword)    #将新单词存入路径队列
                        print (visited)
                    if newword == end :
                        print("最终转换路径为：")
                        return visited


print (find_path(start, end, adict))
