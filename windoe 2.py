#!/usr/bin/env python
from Tkinter import *
import sys, feedparser, webbrowser

window = Tk()
f = Frame(window)
f.pack(fill=BOTH, expand=1)




#Facebook feed function
def fbfeed():
    btng.pack_forget()
    btnt.pack_forget()
    btnf.pack_forget()
    fdis.pack()
    ffeed = feedparser.parse("http://www.facebook.com/feeds/page.php?format=rss20&id=266548033369001")  
    def weblink():
        webbrowser.open_new(url)
    for i in range(3):
        url = ffeed.entries[i].link
        ffeedt = ffeed.entries[i].title
        entbtn = Button(f, text=ffeedt, wraplength=215, command=weblink)
        entbtn.pack()
        ffeedd = ffeed.entries[i].description
        ffeedtime = ffeed.entries[i].published
        distext = Text(f, height=4)
        distext.pack(anchor=N)
        distext.insert(END, (ffeedtime, ffeedd))
  

#Google feed function        
def gofeed():
    gfeed = feedparser.parse("http://feeds.ign.com/ign/articles")
    btng.pack_forget()
    btnt.pack_forget()
    btnf.pack_forget()
    gdis.pack()  
    def weblink():
        webbrowser.open_new(url)
    for i in range(3):
        url = gfeed.entries[i].link
        gfeedt = gfeed.entries[i].title
        entbtn = Button(f, text=gfeedt, wraplength=215, command=weblink)
        entbtn.pack()
        gfeedd = gfeed.entries[i].description
        gfeedtime = gfeed.entries[i].published
        distext = Text(f, height=5)
        distext.pack(anchor=N)
        distext.insert(END, (gfeedtime, gfeedd))


#Twitter feed function
def twfeed():
    tfeed = feedparser.parse("http://feeds.ign.com/ign/articles")
    btng.pack_forget()
    btnt.pack_forget()
    btnf.pack_forget()
    tdis.pack()  
    def weblink():
        webbrowser.open_new(url)
    for i in range(3):
        url = tfeed.entries[i].link
        tfeedt = tfeed.entries[i].title
        entbtn = Button(f, text=tfeedt, wraplength=215, command=weblink)
        entbtn.pack()
        tfeedd = tfeed.entries[i].description
        tfeedtime = tfeed.entries[i].published
        distext = Text(f, height=4)
        distext.pack(anchor=N)
        distext.insert(END, (tfeedtime, tfeedd))




#Buttons and configurations


        #Top level Label
lbl = Label(f, text="Oppkey RSS feeds").pack()



        #Facebook button
btnf = Button(f, text="Facebook", background= '#3b5998', command=fbfeed)
btnf.pack(side=LEFT, fill=BOTH, expand=1)
btnf.config(fg='white', bd=6)



        #Google+ button
btng = Button(f, text="Google+", background= '#d34836', command=gofeed)
btng.pack(side=LEFT, fill=BOTH, expand=1)
btng.config(fg='white', bd=6)



        #Twitter button
btnt = Button(f, text="Twitter", background= '#4099FF', command=twfeed)
btnt.pack(side=LEFT, fill=BOTH, expand=1)
btnt.config(fg='white', bd=6)



        #Facebook display label
fdis = Label(f, text="Now displaying the top 3 FB stories")


        #Twitter display label
tdis = Label(f, text="Now displaying the top 3 Twitter stories")



        #Google display label
gdis = Label(f, text="Now displaying the top 3 G+ stories")


        #back button for returning to the previous screen
bckbtn = Button(f, text='Back').place(x=0, y =0)



        #quit button for quiting out of the entire program
quitbtn = Button(f, text='Quit', command=f.quit).place(x=267, y=0)  



        #Parent Window and configurations
window.title("Oppkey RSS Feeds")
window.geometry("320x455")
window.wm_iconbitmap('favicon.ico')
window.mainloop()
