# -*- coding: utf-8 -*-
"""
Liam Weininger

Final Project
"""
from dotenv import load_dotenv
import sys, json, requests, os; 
load_dotenv()

#Only necessary to set default encoding in Python 2.* - doesn't work on Python 3.*
try:
    sys.setdefaultencoding('utf8')
except Exception:
    pass

headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': os.environ["Client-ID"],
    'Authorization': 'Bearer ' + os.environ["OAUTH"],
}
try:
    response = requests.get('https://api.twitch.tv/helix/streams/followed?user_id=424925203', headers=headers)
except (KeyError, ValueError):
    print("Error - make sure your OAuth is formatted correctly in oauth.txt")
    sys.exit(1)
    
data = response.json()
numStreams = len(data['data'])

print ("\nCHANNEL " + ' '*13 + "GAME" + ' '*37 + "VIEWERS" + ' '*8 + "\n" + '-'*80)

for i in range (0, numStreams): 
    channelName = data["data"][i]["user_name"];
    channelGame = data["data"][i]["game_name"];
    channelViewers = str(data["data"][i]["viewer_count"]);

    #Truncate long channel names/games
    if(len(channelName) > 18):
    	channelName = channelName[:18] + ".."
    if(len(channelGame) > 38):
        channelGame = channelGame[:38] + ".."

    #Formatting
    print ("{} {} {}".format(
	channelName.ljust(20),
	channelGame.ljust(40), 
	channelViewers.ljust(8)
    ))

    if (i == numStreams-1):
        print ('-'*80)