import pytumblr, time, random
import re
import sys
import os
from time import sleep

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
 
    
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

for tag in tags:
    for c in client.tagged(tag):
      if not c["reblog_key"] in open('posts.txt').read():
        if random.randint(1,1) == 1:
        
            f = open('posts.txt', 'a')
            f.write(c["reblog_key"] + "\n")
            f.close()
             
            client.like(c["id"],c["reblog_key"])
            """Change the CHANGEME name"""
            client.reblog('CHANGEME.tumblr.com',id=c["id"], reblog_key=c["reblog_key"]) 
            print "Liked & Rebloged: " + tag + " - " + c["blog_name"] + ".tumblr.com" + " - " + c["slug"] + c["reblog_key"]
            client.follow(c["blog_name"] + ".tumblr.com")
            print "Followed: " + tag + " - " + c["blog_name"] + ".tumblr.com"
        else:
        #    client.follow(c["blog_name"] + ".tumblr.com")
            print "Followed: " + tag + " - " + c["blog_name"] + ".tumblr.com"
        t = random.randint(300,600)
        print "Sleeping for " + str(t) + " seconds."
        time.sleep(t);
        restart_program()




print "Couldnt Get Any Posts...!"
te = random.randint(10,20)
print "Sleeping for " + str(te) + " seconds."
#time.sleep(te);
for i in range(te):
    print 0 + i
    sleep(1)
print "Restart"
restart_program()

