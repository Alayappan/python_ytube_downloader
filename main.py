import time
import sys
from pytube import YouTube
import sys

aud=None
res=None
fileext=None
mime=None
if len(sys.argv)==1:
	print 'python main.py <link> [<mime-type(example video/mp4,audio/mp4,..etc)> <resolution if video>]'
	sys.exit()

try:
	if sys.argv[2]!='-1':
		mime=sys.argv[2]
	print mime
except Exception as e:
	print e	
try:
	if sys.argv[3]!='-1':
		res=sys.argv[3]
	print res
except Exception as e:
	print e	

if (sys.argv[1].find('youtube')!=-1):
	yt = YouTube(sys.argv[1])
	#print yt.streams.all()
	ds=yt.streams.filter(mime_type=mime ,res=res)
	print ds.all() 
	if ds.all() !=[]:
		print 'starting download...'
		ds.first().download()
		print 'download finished'
	else:
		print 'there is no format you specified'
	
else:
	print 'the given link is not a youtube link'
	print 'please provide a youtube link'