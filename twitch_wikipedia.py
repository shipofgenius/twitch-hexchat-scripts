__module_name__ = "twitch wikipedia"
__module_version__ = "1.0"
__module_description__ = "Hexchat plugin for searching wikipedia from chat. Wikipedia API: https://github.com/goldsmith/Wikipedia"

import datetime,hexchat,re,time, wikipedia

# Main
def message_cb(word, word_eol, userdata):
	trigger(word)

# Catch  trigger 	
def trigger(word):
	words = word[1].split(" ")
	i = 0
	for strng in words:
		if strng.lower() == "!wiki":
			print("found !wiki")
			i = words.index('!wiki')
			try:
				searchWiki(words[i+1])
			except:
				print("No search input")

# send words index to wiki api			
def  searchWiki(query):
	objWiki = wikipedia.page(query)
	hexchat.command("say " + wikipedia.summary(query,sentences=1) + " " + objWiki.url)
	
hexchat.hook_print("Channel Message", message_cb)		
print("Script loaded: " + str(datetime.datetime.now()))
			
	
			
			
			
	