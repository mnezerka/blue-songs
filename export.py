import codecs
import os
import sys
import re

def processFile(fPath, fArtist):

    with open(fPath, 'rb') as f:
        sqlTitle = fPath
        sqlArtist = fArtist

        # read first 4 bytes
        header = f.read(4)

        # check if we have BOM...
        bom_len = 0
        encodings = [
            ( codecs.BOM_UTF32, 4 ),
            ( codecs.BOM_UTF16, 2 ),
            ( codecs.BOM_UTF8, 3 )
        ]

        # ... and remove appropriate number of bytes    
        for h, l in encodings:
            if header.startswith(h):
                bom_len = l
                break
        f.seek(0)
        f.read(bom_len)

        data = f.read()
        data = data.replace('\r', '').replace("'", "''");
        lines = data.split("\n");
        for line in lines:
            t = re.search('{title: (.*)}', line)
            if t:
                sqlTitle = t.group(1)

        sqlData = "\\n".join(lines)

        return "INSERT INTO songs (name, artist, data) VALUES ('%s', '%s', '%s');" % (sqlTitle, sqlArtist, sqlData)

root = '.'
for d in os.listdir(root):
    if os.path.isdir(d) and not d.startswith('.'):
        for f in os.listdir(os.path.join(root, d)):
            if f.endswith('.txt'):
                fPath = os.path.join(root, d, f) 
                print processFile(fPath, d)
