import wikipedia as wiki
#h="https://en.wikipedia.org/wiki/"
h=""
for j in range(49,55):
    file=open("url1000_0"+str(j)+".dat","w")
    for num in range(1000):
        nam=wiki.random(1)
        nam=nam.replace(" ", "_")
        file.write(str(h)+str(nam)+"\n")
    file.close()
    
