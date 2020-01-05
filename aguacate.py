#!/usr/bin/env pythfor m
# -*- coding: utf-8 -*-
# El codi s'ha modificat ja que estava obsoletgit 
import urllib
import io
from bs4 import BeautifulSoup

def Aguacate(string_html): #scraping_like_text_by_url
    html = urllib.urlopen(string_html)
    soup1 = BeautifulSoup(html.read(),"html5lib")
    soup2 = (soup1.get_text()).encode('utf-8')
    return soup2

for i in range(2,3):
    fLlegir= open("./data_URLS/url1000_00"+str(i)+".dat",mode="r")
    for j in range(100,1000):
        html=fLlegir.readline()
        html=html.split("\n")[0]
        nom=html.replace("https://en.wikipedia.org/wiki/","")
        nom=nom.replace("/","\\")
        fEscriure=open("./html_like_text_X/"+str(nom)+"_X.txt",mode = 'w')
        htmlLikeTxt=Aguacate(html)
        fEscriure.write(htmlLikeTxt)
        fEscriure.close()
    fLlegir.close()


######Comentaris per entendre algo en 3 mesos

#html = urllib.urlopen("https://en.wikipedia.org/wiki/Beatriz_Jaguaribe")
#soup1 = BeautifulSoup(html.read(),"html5lib")
'''
Imprimeix el titol del article:
print soup1.title.string
> Plats bruts - Viquipèdia, l'enciclopèdia lliure
'''
#soup2=(soup1.get_text()).encode('utf-8')
#print type(soup2)
#print soup2
#file=open('prova.txt','w')
#file.write(soup2)
#file.close()