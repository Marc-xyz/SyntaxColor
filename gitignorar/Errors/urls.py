#!/usr/bin/env pythfor m
# -*- coding: utf-8 -*-

''' 
Objectiu: generar un fitxer .txt amb 
          10 mil articles de la Viquipèdia o Wikipedia.
'''
#import wikipediaapi
import wikipedia as wiki
import sys

wiki.set_lang("en")
file=open("urls.txt","w")
stringUrl=[]
m=0
while len(stringUrl)<101:
    try:
        m+=1
        name=wiki.random(1)
        if "disambiguation" not in name:
            print(str(name))
            stringUrl.append(wiki.page(str(name)).url)
    except wiki.exceptions.DisambiguationError as e:
        e='456'
        print("Hola_estic_aqui")
        #name = e.split('\n')[-1]
        #print(name)
        continue
    except wiki.exceptions.PageError as e1:
        e='456'
        print("Hola_estic_alla")
        #name = e.split('\n')[-1]
        #print(name)
        continue
        
for j in range(len(stringUrl)):
    file.write(str(stringUrl[j]))
    file.write("\n")
file.close()
print(stringUrl)


#                         :::Syntaxis:::                            #
#####################################################################
#                         :::Comentari:::                           #


#URL's rellevants en la construcció del codi:
#-------->Comentari sobre la url

#https://ca.wikipedia.org/wiki/Especial:Article_aleatori
#---------> Article aleatori a wiki en catlà

#--------->Aquí hi ha exemples de wikipedia.random() 
#https://www.programcreek.com/python/example/93329/wikipedia.random

#--------->Finalment aquesta no el faig servir
#https://wikipedia-api.readthedocs.io/en/latest/README.html (: (: (:
#https://youtu.be/ATJlFDhYvyw
#https://youtu.be/P60i5TdZNpo
