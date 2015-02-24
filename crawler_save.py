import urllib.request
import http.cookiejar
import os

def makeMyOpener(head = {
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

def saveFile(dat):
	save_path = "/Users/Emanon/testDir/nw/tmp.out"
	os.system("touch %s" % save_path)
	file_obj = open(save_path, 'wb')
	file_obj.write(dat)
	file_obj.close()

oper = makeMyOpener()
uop = oper.open('http://www.baidu.com/', timeout = 1000)
data = uop.read()
print(data.decode())
saveFile(data)