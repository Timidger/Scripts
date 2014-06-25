import webbrowser, time, os
home = os.path.expanduser("~")
os.chdir(os.path.join(home + '/Dropbox/Programming/Python/Misc/Scripts/'))
directory = os.getcwd()
try:
    with open(directory + os.sep + 'MyStartupCheck.txt', 'r') as check:
        if check.next() == time.strftime('%j'):
            webbrowser.open('http://google.com')
            exit()
except IOError:
    pass

errday = ('stackexchange.com/', 'procworld.blogspot.com/',
          'reddit.com', 'https://news.ycombinator.com/',)

day_to_address = {
 0: (), #Sunday

 1: ('xkcd.com', 'darklegacycomics.com/',
     'trippingoveryou.com/'), #Monday

 2: ('what-if.xkcd.com/',), #Tuesday

 3: ('xkcd.com',
     'www.escapistmagazine.com/videos/view/zero-punctuation'), #Wed.

 4: ('trippingoveryou.com',),#Thursday

 5: ('xkcd.com',),#Friday

 6: (), #Saturday
                }
for webpage in day_to_address.get(int(time.strftime('%w'))) + errday:
    webbrowser.open('http://' + webpage, 2)

with open(directory + os.sep + 'MyStartupCheck.txt', 'w') as overwrite:
    overwrite.write(time.strftime('%j'))
