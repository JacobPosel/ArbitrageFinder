import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

from urllib.request import Request, urlopen


import sys
import math
#import win32api
#

def webscrape():
    biggerlist = []
    link_list = []# list of web links from oddschecker, requires adjusting due to recent changes to web layout

    print("number links: ", len(link_list))
    print(time.ctime(), '\n')
    for i in range(len(link_list)):
        req = Request(link_list[i], headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        urlopen(req).close()
        page_soup = soup(webpage, "html.parser")


        containers = page_soup.find_all("li", {"class":"_3f0k2k"})
        for container in containers:
            biglist = []
            title_container=container.find_all("div",{"class": "_2tehgH"})
            odds_container =container.find_all("div",{"class": "_1NtPy1"})
            for i in range(len(odds_container)):
                if (odds_container[i].text) == '--':
                    biglist.append(1)
                else:
                    biglist.append(float(odds_container[i].text))
            for i in range(len(title_container)):
                biglist.append(title_container[i].text)
            biggerlist.append(biglist)
    return(biggerlist)
    
        
    

def arb(finallist): #, biggerlist):
    for i in range(len(finallist)):
        if len(finallist[i]) == 4:
            x1 = finallist[i][0]
            y2 = finallist[i][1]
            name1 = finallist[i][2]
            name2 = finallist[i][3]
            x1 = float(x1)
            y2 = float(y2)
            if (x1 >= 100 or x1<0) or (y2 >=100 or y2<0):
                if x1 < 0:
                    x1 = (100/(-1*x1)) + 1
                else:
                    x1 = (x1/100) +1
                if y2 < 0:
                    y2 = (100/(-1*y2)) + 1
                else:
                    y2 = (y2/100) + 1
            z = 0
            stake = 100#float(input('Enter stake: '))
            #if stake == '':
            #break
            x1 = 1/x1
            y2 = 1/y2
            z = x1+ y2
            a = (1 - z)
            Stake1 = (stake*x1)/z
            Stake2 = (stake*y2)/z
            profit = (a/z)*stake
            
            if z < 1:
                print("Arbitrage available")
                print("Stake 1: ", round(Stake1,2) , "," , "Stake 2: ", round(Stake2,2))
                print("profit: ", round(profit,2))
                print("Teams: ", name1, name2)
                print("Odds1 :", finallist[i][0], "Odds2 :", finallist[i][1])
                print("\n")
#            if float(profit) >= 0.5:
#                win32api.MessageBox(0,profit, 'ARB')
                
                
                
                
        elif len(finallist[i]) == 5:
            x1 = finallist[i][0]
            y2 = finallist[i][1]
            z3 = finallist[i][2]
            name1 = finallist[i][3]
            name2 = finallist[i][4]
            if (x1 >= 100 or x1<0) or (y2 >=100 or y2<0) or (z3 >=100 or z3<0):
                if x1 < 0:
                    x1 = (100/(-1*x1)) + 1
                else:
                    x1 = (x1/100) +1
                
                if y2 < 0:
                    y2 = (100/(-1*y2)) + 1
                else:
                    y2 = (y2/100) + 1
                
                if z3 < 0:
                    z3 = (100/(-1*z3)) + 1
                else:
                    z3 = (z3/100) + 1
                        
            x1 = float(x1)
            y2 = float(y2)
            z3 = float(z3)
            z = 0
            stake = 100#float(input('Enter stake: '))
            #if stake == '':
            #break
            x1 = 1/x1
            y2 = 1/y2
            z3 = 1/z3
            z = x1+ y2 + z3
            a = (1 - z)
            Stake1 = (stake*x1)/z
            Stake2 = (stake*y2)/z
            Stake3 = ((stake*z3)/z)
            profit = (a/z)*stake
            if z < 1:
                print("Arbitrage available")
                print("Stake 1: ", round(Stake1,2) , "," , "Stake 2: ", round(Stake2,2), ",", "Stake 3: ", round(Stake3,2))
                print("profit: ", round(profit,2))
        
                print("Teams: ", finallist[i][3], finallist[i][4])
                print("Odds1 :", finallist[i][0], "Odds2 :", finallist[i][1], "Odds3 :", finallist[i][2])
                print("\n")
#            if float(profit) >= 0.5:
#                win32api.MessageBox(0,profit, 'ARB')
                
        else:
            pass

def main():
    while True:
        biggerlist = webscrape()
        arb(biggerlist)
        time.sleep(100)
        print('\n','\n','\n')
        print("------------------------------------")
    
    
    
main()
