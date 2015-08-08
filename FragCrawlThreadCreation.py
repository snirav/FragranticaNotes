__author__ = 'Nirav'

import threading
import urllib2
from bs4 import BeautifulSoup
import numpy as np
# import pandas as pd


# Spider class for running the threads for all the designers
class mySpider(threading.Thread):

    def __init__(self,siteUrl,designerName):
        threading.Thread.__init__(self)
        self.siteUrl = siteUrl
        self.designerName = designerName

    def run(self):
        print "Starting " + self.designerName
        getNextlevelUrls(self.siteUrl, self.designerName)
        print "Exiting " + self.designerName


def getNextlevelUrls(siteUrl, designerName):
    # f = codecs.open('C:\\Perfumes\\'+designerName+'.txt','w',encoding='utf8')
    notesDictionary = {}
    try:
        designerResponse = urllib2.urlopen(siteUrl + '/designers/' + designerName + '.html', timeout=10)
    except urllib2.URLError, e:
        print "Oops, timed out?", e
    designerSoup = BeautifulSoup(designerResponse)
    links = designerSoup.findAll('a')
    perfumeCount = 0
    print designerName
    # f.write(designerName +'\n')
    for link in links:
        if link.get('href') != None:
            if link['href'].find('/perfume/'+designerName) != -1:

                perfumeCount += 1

                perfumeID = str(link['href'].split('-')[-1].split('.')[0])
                # print(perfumeID)
                print(link.img.get('alt').split(' ', 1)[1])
                userListUrl = siteUrl+'/' + '/ajax.php?view=whoHasHadWant&perfume_id=' + perfumeID
                try:
                    userListResponse = urllib2.urlopen(userListUrl,timeout=10)
                except urllib2.URLError, e:
                    print "URL Fetch time-out",e
                userListSoup = BeautifulSoup(userListResponse)
                perfumeWhoHasHadSigWantCurr = [int(tag.string) for tag in (userListSoup.find('p').findAll('b'))]
                # print perfumeWhoHasHadSigWantCurr

                perfumeUrl = siteUrl+'/'+link['href']
                try:
                    perfumeResponse = urllib2.urlopen(perfumeUrl,timeout=10)
                except urllib2.URLError, e:
                    print "URL Fetch time-out",e
                perfumeSoup = BeautifulSoup(perfumeResponse)

                perfumeNotesTitle = perfumeSoup.findAll('span',attrs={'class':'rtgNote'})
                noteList = [perfumeTitle.img.get('alt') for perfumeTitle in perfumeNotesTitle]
                noteID = [int(perfumeTitle.attrs['title']) for perfumeTitle in perfumeNotesTitle]
                # print(noteList)
                # print(noteID)
                idx = 0
                for ith in noteID:
                    if not(ith in notesDictionary):
                        notesDictionary[ith] = noteList[idx]
                    idx += 1
                perfumeMenWomen = np.sign(np.array([perfumeSoup.title.text.find(' men'), perfumeSoup.title.text.find(' women')]))
                # print(perfumeMenWomen)
                perfumeVotes = perfumeSoup.findAll('table',attrs={'class':'voteLS'})
                perfumeLongevityVotes = np.array([int(a.string) for a in perfumeVotes[0].findAll('td', attrs={'class':'ndSum'})])
                # print(perfumeLongevityVotes)
                perfumeSillageVotes = np.array([int(a.string) for a in perfumeVotes[1].findAll('td', attrs={'class':'ndSum'})])
                # print(perfumeSillageVotes)
                perfumeAttrs = np.append(perfumeMenWomen, np.append(perfumeLongevityVotes, perfumeSillageVotes))
                perfumeNotes = perfumeSoup.findAll('div',attrs={'id':'userMainNotes'})

                # perfumeNotesStr = str(perfumeNotes[0].attrs[u'title'])
                # notesVec = np.zeros(400, dtype = int)
                # perfumeNotesStrSplit = perfumeNotesStr.split(';')
                # for notes in perfumeNotesStrSplit :
                #    individualNotes = notes.split(':')
                #    individualNotesInt = np.array([int(str_tmp) for str_tmp in individualNotes])
                #    notesVec[individualNotesInt[0]] = individualNotesInt[1]
                # print(notesVec)


def crawl(url, designer, designerList):
    threads = []
    if designer == 'All':
        for designer in designerList:
            try:
                t = mySpider(url, designer)
                threads.append(t)
            except Exception as errtxt:
                print errtxt
    else:
            getNextlevelUrls(url, designer)
    [t.start() for t in threads]
    [t.join() for t in threads]
    print "Main Thread Completed!!" 
