import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as dw

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAxMjRfMjc1%2FMDAxNjExNDgyMjY1MTk1.GUpEhMooiN3Iua1ug0pXDN2rW4cYHtq9RS_rDyImvIcg.8YF5Y5-IcfWfoOdvFgTsJ4MrpWCRn9TJvbjYmAOTBGgg.PNG.charm_sim%2Fimage.png&type=sc960_832"
htmlURL = "http://google.com"


savePath = "/Users/jjmstars/Desktop/jjmstars/Projects/test1.jpg"
savePath2 = "/Users/jjmstars/Desktop/jjmstars/Projects/index.html"


dw.urlretrieve(imgUrl, savePath)
dw.urlretrieve(htmlURL, savePath2)
print("다운로드 완료!!!")
