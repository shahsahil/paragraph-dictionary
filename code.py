import requests
import json
import re
from pprint import pprint

def fetchFromInternet(word):
	url = "https://api.pearson.com/v2/dictionaries/ldoce5/entries?headword="+word+"&apikey=AccessKey" #please register in pearson developer api website and put your own access key
	res = requests.get(url)
	jsonstring = (res.text.encode('ascii', errors='ignore')).decode('ascii')
	global parsed
	parsed = json.loads(jsonstring)
	return res.status_code
	
def parseJSON(h):
	global parsed
	r=""
	try:
		for x in parsed['results']:
			r=r+"Headword: "+x['headword']+"\n"
			if 'definition'in x['senses'][0]:
				r=r+"Definition: "+''.join(x['senses'][0]['definition'])+"\n"
			if 'examples' in x['senses'][0]:
				#pprint(x['senses'][0]['examples'])
				if 'text' in x['senses'][0]['examples'][0]:
					r=r+"Example: "+x['senses'][0]['examples'][0]['text']+"\n"
			r=r+"\n"
			if h:
				break
	except:
		global word
		print("ATTENTION"+word)
	return r;
	
f=open('sample-input.txt','r')
words= set(f.read().split())
print(words)
HeadwordLimit = False
for word in words:	
	if(len(word)>3):
		word = re.sub(r'[^\w\s]','',word)
		parsed=""	
		fetch = fetchFromInternet(word)
		print("*********************************************************")
		if fetch==200:
			print(parseJSON(HeadwordLimit))