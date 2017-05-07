__module_name__ = "Twitch Auto Greet"
__module_version__ = "1.0"
__module_description__ = "Checks if a message is the first message from a user. Responds with a greeting"

### TO DO ##################################
#- status commands - *heartbeat , listofusers
# ~~replace stripAnsi with native strip~~
#- emote variables - randomize emotes
#- check stream status
############################################

import datetime,hexchat,re,time,random

# Main
def hello_cb(word, word_eol, userdata):
	nick = hexchat.strip(word[0])
# Set Greeting Messages - say[space]message | nick = username 
# @ = highlights name in chat
	listGreet =["say Hi there @" + nick + "! cjrLove",   
			"say Good to see you @" + nick + "!",
			"say Welcome to the kitchen @" + nick + "!",
			"say Hi @" + nick + "! Welcome to the kitchen :)",
			"say cjrLove What's up @" + nick + "!? cjrLove",
			"say Hello @" + nick + "! Good to see ya cjrLove"]			
	if firstMessage(nick) :
		print(nick + "'s first message")
		time.sleep(random.randint(1, 5))
		hexchat.command(random.choice(listGreet))
	return hexchat.EAT_NONE
	
# # Strip color ansi 	
# #def stripAnsi(s):
# #	ansi_escape = re.compile("\x03(?:\d{1,2}(?:,\d{1,2})?)?", re.UNICODE)
# #	reStr = ansi_escape.sub('', s)
# #	return reStr

# Check if user has messaged the channel yet
def firstMessage(nick):
	for usr in listUsers:
		if (nick.lower() == usr.lower()):
			return False
	listUsers.append(nick)	
	return True
	
#check exclusions
def excludeUser(nick):
	for ex in listExclude:
		if (ex.lower() == nick.lower()):
			return False
	
listUsers = ['dummy'] 
listExclude = ['nightbot','twitchnotify','trugamer_maniac']

hexchat.hook_print("Channel Message", hello_cb)		
print("Script loaded: " + str(datetime.datetime.now()))





