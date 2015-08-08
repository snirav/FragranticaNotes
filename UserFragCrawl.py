__author__ = 'Nirav'

import urllib2
from bs4 import BeautifulSoup
# import numpy as np

userList = [614510, 581227]
for userID in userList:
    userUrl = 'http://www.fragrantica.com/member/' + str(userID)

    userPerfumes = urllib2.urlopen(userUrl, timeout=10)
    userPerfumeSoup = BeautifulSoup(userPerfumes)
    perfumeHas = [int(a.attrs['id'][2:]) for a in userPerfumeSoup.findAll('ul', attrs={'id': 'imam-sortable'})[0].findAll('li')]
    perfumeWants = [int(a.attrs['id'][2:]) for a in userPerfumeSoup.findAll('ul', attrs={'id' :'zelim-sortable'})[0].findAll('li')]
    perfumeHad = [int(a.attrs['id'][2:]) for a in userPerfumeSoup.findAll('ul', attrs={'id': 'imao-sortable'})[0].findAll('li')]

    userLoveHateUrl = 'http://www.fragrantica.com/ajax.php?view=emotion&id=' + str(userID)
    userLoveHatePerfumes = urllib2.urlopen(userLoveHateUrl, timeout=10)
    userLoveHateSoup = BeautifulSoup(userLoveHatePerfumes)
    loveHateList = [[],[],[]]
    lovelikedislikeCount = -1
    for loveHate in userLoveHateSoup.findAll('body')[0]:
        if loveHate.name == 'h3':
            lovelikedislikeCount += 1
        elif loveHate.name == 'a':
            if loveHate.attrs['href'] != None:
                loveHateList[lovelikedislikeCount].append(int(loveHate.attrs['href'].split('.')[0].split('-')[-1]))
