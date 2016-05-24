import math, sys, os, platform, time

print "Please enter your login credentials to play:"

ENTER_USER = "Username:"
ENTER_PASS = "Password:"
ENTER_KEY = "Testing Key:"
ENTER_SV_1 = "Game Server: "
USERNAME = raw_input(ENTER_USER)
PASSWORD = raw_input(ENTER_PASS)
BETA_KEY = raw_input(ENTER_KEY)
IP = "73.146.46.129"
PATCHER_URL = "http://www.nickdoge.cf/current/launcher"
def AskForCred():
	print ENTER_SV_1 + IP
	
AskForCred()
print "launcher: Checking login credentials..."
time.sleep(1)
print "downloader: Checking download server..."
time.sleep(2.4)
print "downloader: successfully connected to // " + PATCHER_URL
time.sleep(0.2)
#print "launcher: Starting Game; no download server"
from toontown.toonbase import ToontownStart

os.environ["PLAYTOKEN"] = USERNAME + ':' + PASSWORD

