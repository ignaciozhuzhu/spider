import requests
from bs4 import BeautifulSoup

mytxt=open('getIpHosts.txt','w') 
mytxt.write('github.com'+'\n'
			'assets-cdn.github.com'+'\n'
			'avatars0.githubusercontent.com'+'\n'
			'avatars1.githubusercontent.com'+'\n'
			'documentcloud.github.com'+'\n'
			'gist.github.com'+'\n'
			'help.github.com'+'\n'
			'nodeload.github.com'+'\n'
			'raw.github.com'+'\n'
			'status.github.com'+'\n'
			'training.github.com'+'\n'
			'github.io'+'\n')
mytxt.close()

content=''
for i in open("getIpHosts.txt"):
    url = "http://ip.chinaz.com/" + i.strip()
    resp = requests.get(url)
    soup=BeautifulSoup(resp.text)
    x=soup.find(class_="IcpMain02")
    m = soup.find(attrs={'class':'IcpMain02'})  
    m = m.find(attrs={'class':'WhwtdWrap bor-b1s col-gray03'})  
    m = m.find_all(attrs={'class':'Whwtdhalf'}) 
    content +=m[1].string.strip()+' '+ i.strip()+'\n'
mytxt=open('getIpHosts.txt','w') 
print content
mytxt.write('# github begin------------------'+'\n'
			+content+
			'# github end------------------'+'\n')

