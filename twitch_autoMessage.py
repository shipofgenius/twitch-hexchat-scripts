__module_name__ = "twitch auto message"
__module_version__ = "1.0"
__module_description__ = "Sends a random customized message to the channel on a timer. Hexchat plugin for Twitch subscription hype."

################## TO DO ###########################
# Abilty for mods to add custom messages
# Command that lists current messages and index 
# Editable messages by index
# mods should be able to set timer
####################################################

def function():
	




# Init. Hook all messages. Call #Main. Verify script has loaded
hexchat.hook_print("Channel Message", message_cb)		
print("Script loaded: " + str(datetime.datetime.now()))
