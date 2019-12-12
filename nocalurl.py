import wikipedia as wiki
h="https://en.wikipedia.org/wiki/"
file=open("url1000.txt","w")
for j in range(7,10):
    file=open("url1000_"+str(j)+".dat","w")
    for num in range(1000):
        nam=wiki.random(1)
        nam=nam.replace(" ", "_")
        file.write(str(h)+str(nam)+"\n")
    file.close()
    
