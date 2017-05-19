__module_name__ = "twitch subhype"
__module_version__ = "1.0"
__module_description__ = "Hexchat plugin for Twitch subscription hype."

import datetime,hexchat,re,time

# Main
def hello_cb(word, word_eol, userdata):
	
	listStr = ["just subscribed","subscribed for"]
	for str in listStr:
		if word[1].find(str) != -1:
			hexchat.command("say !hype cjrChia <3 !SUB HYPE! <3 cjrChia <3 !SUB HYPE! <3 cjrChia <3 !SUB HYPE! <3 cjrChia <3 SUB HYPE <3 cjrChia <3 SUB HYPE <3 cjrChia <3 SUB HYPE <3 cjrChia ")

# Init. Hook all messages. Call #Main. Verify script has loaded
hexchat.hook_print("Channel Message", hello_cb)		
print("Script loaded: " + str(datetime.datetime.now()))