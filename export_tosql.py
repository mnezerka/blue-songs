import sys
import re

with open(sys.argv[1]) as f:
    sqlTitle = sys.argv[1]
    data = f.read()
    data = data.replace('\r', '');
    lines = data.split("\n");
    for line in lines:
        t = re.search('{title: (.*)}', line)
        if t:
            title = t.group(1)
        #print line

    #print '\\n'.join(data.split("\n"));
    #print "\\n".join(data.split("\n"));

    sqlData = "\\n".join(lines)

    print "INSERT INTO songs (name, data) VALUES ('%s', '%s')" % (title, sqlData)
