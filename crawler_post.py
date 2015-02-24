import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse

def ungzip(data):
	try:
		print('unzipping...')
		data = gzip.decompress(data)
		print('done!')
	except:
		print('No need to decompress.')
	return data

def getXSRF(data):
	credential = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
	strlist = credential.findall(data)
	return strlist

def getOpener(head = {
	'Connection': 'Keep-Alive',
	'Accept': 'text/html, application/xhtml+xml, */*',
	'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	}):
	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	header = []
	for key, value in head.items():
		element = (key, value)
		header.append(element)
	opener.addheaders = header
	return opener

url = "http://www.zhihu.com/"
opener = getOpener()
op = opener.open(url)
data = op.read()
data = ungzip(data)
_xsrf = getXSRF(data.decode())

url += 'login'
id = input("Plz input your id: ")
password = input("Pwd: ")
postDict = {
	'_xsrf': _xsrf,
	'email': id,
	'password': password,
	'rememberme': 'y'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

print(data.decode())