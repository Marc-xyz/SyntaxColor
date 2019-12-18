import wikipedia as wiki
h="https://en.wikipedia.org/wiki/"
for j in range(11,21):
    file=open("url1000_"+str(j)+".dat","w")
    for num in range(1000):
        nam=wiki.random(1)
        nam=nam.replace(" ", "_")
        file.write(str(h)+str(nam)+"\n")
    file.close()
    
