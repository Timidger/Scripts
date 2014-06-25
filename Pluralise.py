#Totally not mind, stole it from 4chan
from re import sub

def correct(text):
    return sub('(\d+) (\w+)\((e?s)\)',
               lambda x: '%s %s%s' % (x.group(1),x.group(2),
               '' if int(x.group(1)) in [0,1] else x.group(3)),
               text)
