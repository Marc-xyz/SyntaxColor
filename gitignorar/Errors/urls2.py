# Get 10000 random pages from Wikipedia.
#Make the directory to store the HTML pages.

for i in range(10):
    opener = build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    infile = opener.open('http://en.wikipedia.org/wiki/Special:Random')

    page = infile.read()

    # Write it to a file.
    # TODO: Strip HTML from page
    f= open('randompages/file'+str(i)+'.html','w')
    f.write(page)
    f.close()

    print ("Retrieved and saved page",str(i+1))
