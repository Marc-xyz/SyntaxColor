#!/usr/bin/env pythfor m
# -*- coding: utf-8 -*-
import wikipedia
file_1=open("url1000_000.dat","r")
lines=file_1.readlines()
for line in lines:
    line=line.replace('\n','')
    line=line.replace('_(disambiguation)','')
    print (line) #Per veure com va el proces 
    name=str(line)+'_X.txt'
    file_2=open(name,'w')
    article=wikipedia.search(line,3)
    article=wikipedia.page(article[-1])
    file_2.write(article.content)
    file_2.close()
file_1.close()

