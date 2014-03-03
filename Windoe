#!/usr/bin/env python
from Tkinter import *
import sys, feedparser

window = Tk()
ffeed = feedparser.parse("http://feeds.ign.com/ign/articles")

def repop():
    #Buttons and configurations
    #Top level Label
    lbl = Label(window, text="Oppkey RSS feeds").pack()
    #Facebook button
    btnf = Button(window, text="Facebook", background= "#3b5998", command=fbfeed)
    btnf.pack(side=LEFT, fill=BOTH, expand=1)
    btnf.config(fg='white', bd=6)
    #Google+ button
    btng = Button(window, text="Google+", background= "#d34836", command=gofeed)
    btng.pack(side=LEFT, fill=BOTH, expand=1)
    btng.config(fg='white', bd=6)
    #Twitter button
    btnt = Button(window, text="Twitter", background= "#4099FF", command=twfeed)
    btnt.pack(side=LEFT, fill=BOTH, expand=1)
    btnt.config(fg='white', bd=6)



#Feed description display function
def textdis():
    #ffeedd = ffeed.entries[:].description
    #ffeedtime = ffeed.entries[:].published
    #ffeedt = ffeed.entries[].title
    distext = Text(window)
    distext.pack()
    distext.insert(END, (ffeedtime, ffeedd))



#Facebook feed function
def fbfeed():
    btng.pack_forget()
    btnt.pack_forget()
    btnf.pack_forget()
    fdis = Label(window, text="Now displaying the top 3 FB Feeds")
    #backbtn = Button(window, text='Back').pack(side=LEFT, anchor=N)
    quitbtn = Button(window, text='Quit', command=window.quit).pack(side=RIGHT, anchor=N)    
    for i in range(0,3):
        ffeedt = ffeed.entries[i].title
        entbtn = Button(window, text=ffeedt, wraplength=215, command=textdis)
        entbtn.pack()
        ffeedd = ffeed.entries[i].description
        ffeeddtime = ffeed.entries[i].published
        #destext = Text(window)
        #destext.pack()
        #destext.insert(END, (ffeedd))


#Google feed function        
def gofeed():
    gfeed = feedparser.parse("http://planetcallofduty.gamespy.com/show_rss.php")
    print len(gfeed.entries)
    for i in range(0, 4):
        print "\n" + gfeed.entries[i].title + "\n"
        print gfeed.entries[i].link
        print gfeed.entries[i].description
        print i

#Twitter feed function
def twfeed():
    tfeed = feedparser.parse("http://planetcallofduty.gamespy.com/show_rss.php")
    print len(tfeed.entries)
    for i in range(0, 4):
        print "\n" + tfeed.entries[i].title + "\n"
        print tfeed.entries[i].link
        print tfeed.entries[i].description
        print i

#Buttons and configurations
        #Top level Label
lbl = Label(window, text="Oppkey RSS feeds").pack()

        #Facebook button
btnf = Button(window, text="Facebook", background= '#3b5998', command=fbfeed)
btnf.pack(side=LEFT, fill=BOTH, expand=1)
btnf.config(fg='white', bd=6)

        #Google+ button
btng = Button(window, text="Google+", background= '#d34836', command=gofeed)
btng.pack(side=LEFT, fill=BOTH, expand=1)
btng.config(fg='white', bd=6)

        #Twitter button
btnt = Button(window, text="Twitter", background= '#4099FF', command=twfeed)
btnt.pack(side=LEFT, fill=BOTH, expand=1)
btnt.config(fg='white', bd=6)

        #Parent Window and configurations
window.title("Oppkey RSS Feeds")
window.geometry("320x455")
window.wm_iconbitmap('favicon.ico')
window.mainloop()
