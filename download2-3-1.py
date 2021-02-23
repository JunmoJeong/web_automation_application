import sys
import io
import urllib.request as req


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url = "http://www.encar.com"
mem = req.urlopen(url)

#print("geturl",mem.geturl())
#print("status",mem.status) # 200(정상), 404(요청페이지 없음), 403(reject), 500(server 에러)
#print("headers", mem.getheaders())

#print("info",mem.info())
#print("code", mem.getcode())
print("read", mem.read())
