__module_name__ = "Celsius Fahrenheit converter"
__module_version__ = "1.0"
__module_description__ = "Hexchat plugin for converting celsius to "

########TO DO###########
# print() log
########################

import datetime,hexchat,re,time,random

# Main | Catch trigger	
def trigger_cb(word, word_eol, userdata):
	words = word[1].split(" ")
	for strng in words:
		if strng.lower() == "!celsius" or "!farehnheit":
			print("found " + strng)
			i = words.index(strng)
			convert(int(words[i+1]),strng)
			break

# convert 
def convert(degrees,unit):
	if isValidInput(degrees) and unit == "!celsius":
		fahrenheit = int(round((9 * degrees) / 5 + 32))
		hexchat.command("say " + str(degrees) + "c degrees Celsius equals " + str(fahrenheit) + " degrees fahrenheit.")
	elif isValidInput(degrees) and unit == "!fahrenheit":
		celsius = int(round((degree - 32) * 5 / 9))
		hexchat.command("say " + str(degrees) + "c degrees Fahrenheit equals " + str(celsius) + " degrees celsius.")
	else:
	    print("Invalid Input for " + unit)

#sanitize input
def isValidInput(s,properlength=10):
    if len(str(s)) > properlength:
        return False
    properHex = "0123456789"
    for char in str(s):
        if not char in properHex:
            return False
            break
    return True


hexchat.hook_print("Channel Message", trigger_cb)		
print("Script loaded: " + str(datetime.datetime.now()))


