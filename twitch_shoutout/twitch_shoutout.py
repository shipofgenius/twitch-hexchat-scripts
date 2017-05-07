__module_name__ = "VIP shoutout"
__module_version__ = "1.0"
__module_description__ = "Hexchat plugin for Twitch shoutouts"

######### TO DO #############
# Add team support
# replae stripAnsi with strip
#
#############################


import datetime,hexchat,re,time,random,csv,os

# Read VIP csv file
vipFile = os.getenv('APPDATA') + "\\HexChat\\addons\\twitch_shoutout\\vip.csv"
vipfile = open(vipFile, 'r')
reader = csv.reader(vipfile)
allRows = list(reader)

# Main
def hello_cb(word, word_eol, userdata):
	#isResponse(word)
	trigger(word)

# Catch shout out trigger (!so)	
def trigger(word):
	words = word[1].split(" ")
	i = 0
	for str in words:
		if str.lower() == "!s" and isMod(word[0]) == True:
			print("found !s")
			i = words.index('!s')
			prntMsg(words[i+1])
	
# Print shout out 
def prntMsg(nick):
	if isVip(nick):
		lstInfo = vipInfo(nick)
		hexchat.command("say Give some cjrChia cjrLove and follow " + nick + " : " + lstInfo[1] + "   <3 ABOUT <3 imGlitch " + lstInfo[0] + " imGlitch")
	else:
		hexchat.command("say Give some cjrChia cjrLove and follow " + nick + ": http://www.twitch.tv/" + nick + " cjrLove cjrLove cjrLove cjrLove cjrLove")

# Strip color ansi 	
def stripAnsi(s):
	ansi_escape = re.compile("\x03(?:\d{1,2}(?:,\d{1,2})?)?", re.UNICODE)
	reStr = ansi_escape.sub('', s)
	return reStr
	
# Is user a VIP?	
def isVip(usr):
	for row in allRows:
		if (row[0].lower() == usr.lower()):
			print(usr + " is a VIP")
			return True
	return False
	
# Get VIP info
def vipInfo(nick):
	for row in allRows:
		if nick.lower() == row[0].lower():
			return row[1],row[2]
			
# Check if command sent is from mod - this needs to be moved to its own module
def isMod(nick):
	members = hexchat.get_list("users")
	for m in members:
		print(m.prefix)
		if m.prefix == "@" and m.nick == stripAnsi(nick):
			print("Found @ AND nick matches")
			return True
	return False
		
listUsers = ['dummy']
hexchat.hook_print("Channel Message", hello_cb)		
print("Script loaded: " + str(datetime.datetime.now()))

############ Deprecated ##################


# CURRENTLY OFF - Determine if user message requires a response			
#def isResponse(word):
	#nick = stripAnsi(word[0])
	#if firstMessage(nick) == True and isVip(nick) == True:
		#prntMsg(nick)
	#return hexchat.EAT_NONE
	
# Check if user has messaged the channel yet
#def firstMessage(u):
#	for usr in listUsers:
#		if (u.lower() == usr.lower()):
#			return False
#		else:
#			listUsers.append(stripAnsi(nick))
#			return True
