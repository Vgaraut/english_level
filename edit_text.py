import os
import pysrt as ps
import re
import unicodedata

def remove_accent(text):
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8', 'ignore')

def optimize(source, target):
    path_to = os.makedirs(target)
    path = source
    files = os.listdir(path)
    d=0
    for file in files:
        filename, file_extension = os.path.splitext(file)
        try:
            sub = ps.open(os.path.join(path, file))
        except:
            sub = ps.open(os.path.join(path, file), encoding='iso-8859-1')
        mid=[]
        for i in range(len(sub)):
            x=re.sub(r"(<.*?>)|(\w*[A-Z]{2})|[^\w\s]", ' ',  sub[i].text).replace('\n', ' ').lower()
            mid.append(remove_accent(x))
        with open(os.path.join(path_to, filename + '.txt'), 'w') as fp:
            for item in mid:
                if item.strip():
                    fp.write(item + '\n')            
        d+=1
    return f'{d} files edited'