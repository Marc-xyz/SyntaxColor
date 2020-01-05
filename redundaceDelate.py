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


