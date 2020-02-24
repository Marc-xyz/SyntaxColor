#!/usr/bin/env pythfor m
# -*- coding: utf-8 -*-
import urllib
import io
from bs4 import BeautifulSoup

def Aguacate(string_html): #scraping_like_text_by_url
    html = urllib.urlopen(string_html)
    soup1 = BeautifulSoup(html.read(),"html5lib")
    soup2 = soup1.encode('utf-8')
    return soup2

for i in range(1,2):
    fLlegir= open("./data_URLS/url1000_00"+str(i)+".dat",mode="r")
    for j in range(0,1000):
        html=fLlegir.readline()
        html=html.split("\n")[0]
        nom=html.replace("https://en.wikipedia.org/wiki/","")
        nom=nom.replace("/","\\")
        fEscriure=open("./html_like_csv_Y/pre_csv/"+str(nom)+"_Y.txt",mode = 'w')
        htmlLikeTxt=Aguacate(html)
        fEscriure.write(htmlLikeTxt)
        fEscriure.close()
    fLlegir.close()