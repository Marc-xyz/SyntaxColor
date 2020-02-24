'''Comentari
La primera vegada que vaig fer scraping per extreure els articles de la Wikipedia vaig anar guardant l'url complet fet que és una tonteria perquè tot els urls tenen gran part igual, per tant no cal gastar tanta memòria per una dada tanredundant. . Per solucionar-ho vaig fer servir aquest codi. 
''' 

for i in range(10,49):
    file_1=open("./data_URLS/url1000_0"+str(i)+".dat","r")
    file_2=open("./url1000_00"+str(i)+".dat","w")
    lines=file_1.readlines()
    for line in lines:
        new=line
        new=new.replace("https://en.wikipedia.org/wiki/","")
        file_2.write(new)
    file_1.close()
    file_2.close()


