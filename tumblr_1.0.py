import pytumblr, time, random
import re
import sys
import os
from time import sleep

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    cls()
    restart_program()
    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
 
    
    """Add as many tags as you want"""
tags = [
'Anime',
'Cartoons'
 
    ]
 
client = pytumblr.TumblrRestClient(
   '<consumer_key>',
    '<consumer_secret>',
    '<oauth_token>',
    '<oauth_secret>'
)

tag = random.choice (tags)
for c in client.tagged(tag):
      if not c["reblog_key"] in open('posts.txt').read():
        if random.randint(1,1) == 1:
        
            f = open('posts.txt', 'a')
            f.write(c["reblog_key"] + "\n")
            f.close()
             
            client.like(c["id"],c["reblog_key"])
            #"""Change the CHANGEME name"""
            client.reblog('CHANGEME.tumblr.com',id=c["id"], reblog_key=c["reblog_key"]) 
            print ("Liked & Rebloged: " + tag + " - " + c["blog_name"] + ".tumblr.com" + " - " + c["slug"] + c["reblog_key"])
            client.follow(c["blog_name"] + ".tumblr.com")
            print ("Followed: " + tag + " - " + c["blog_name"] + ".tumblr.com")
        else:
        #    client.follow(c["blog_name"] + ".tumblr.com")
            print ("Followed: " + tag + " - " + c["blog_name"] + ".tumblr.com")
        t = random.randint(20,40)
        countdown(t)




print ("Couldnt Get Any Posts!")
print ("Waiting..")
te = random.randint(10,20)
countdown(te)

