 # Get 10000 random pages from Wikipedia.
import urllib2
import os
import shutil
#Make the directory to store the HTML pages.
print "Deleting the old randompages directory"
shutil.rmtree('randompages')

print "Created the directory for storing the pages"
os.mkdir('randompages')

num_page = raw_input('Number of pages to retrieve:: ')

for i in range(0, int(num_page)):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    infile = opener.open('http://en.wikipedia.org/wiki/Special:Random')

    page = infile.read()

    # Write it to a file.
    # TODO: Strip HTML from page
    f= open('randompages/file'+str(i)+'.html','w')
    f.write(page)
    f.close()

    print "Retrieved and saved page",i+1
