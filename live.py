import requests,time,json,os,sys

zaman=time.strftime("%d/%m/%Y")


def fileidwrite(id):
	f = open("id.txt", "w")
	f.write(str(id))
	f.close()
def fileidread():
	f = open("id.txt")
	a=f.read()
	print a
	f.close()
	return a

def facebook(end=False):
	access_token="EAAZAzzkWc9V0BAF8mhE8WMcRrvfwqOpAQQF..."
	url = "https://graph.facebook.com/v3.2/me/live_videos"
	querystring = {
		"status":"LIVE_NOW",
		"title":"TEST Live Video ",
		"description": "@mzuvin https://github.com/mzuvin "+str(zaman),
		"access_token": str(access_token)
	}
	if(end):
		response = requests.request("POST", "https://graph.facebook.com/"+str(fileidread())+"/?end_live_video=true&access_token="+access_token)
	else:
		response = requests.request("POST", url, params=querystring)
		liste=json.loads(response.text)
		id=liste['id']
		print liste
		fileidwrite(str(id))
		os.system('ffmpeg -re -i "http://SHOUTcastRadioServerUrl/" -loop 1 -i background.jpg -vcodec libx264 -preset veryfast -maxrate 2500k -bufsize 3368k -vf "format=yuv420p" -g 60 -acodec libmp3lame -b:a 198k -ar 44100 -f flv -s 1280x720 "'+liste['stream_url']+'"')

try:
	arg=str(sys.argv[1])
except:
	arg=""

if(arg=="end"):
	facebook(True)
else:
	facebook()
