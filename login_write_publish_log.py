#! /usr/bin/env python
#coding:utf-8

import sys
import re
import urllib2
import urllib
import requests
import cookielib
 
## 这段代码是用于解决中文报错的问题  
reload(sys)  
sys.setdefaultencoding("utf8")  
#####################################################
#loginurl = 'https://accounts.douban.com/login'
#loginurl = 'https://www.zhihu.com/login/email'
#loginurl='https://zs.yayi365.cn/ya/site/resetPassword'
loginurl='http://120.27.147.44:8080/j_acegi_security_check'
logindomain = 'www.baidu.com'
 
class Login(object):
     
    def __init__(self):
        self.name = ''
        self.passwprd = ''
        self.domain = ''
 
        self.cj = cookielib.LWPCookieJar()            
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj)) 
        urllib2.install_opener(self.opener)    
     
    def setLoginInfo(self,username,password,domain):
        '''设置用户登录信息'''
        self.name = username
        self.pwd = password
        self.domain = domain

    def printa(self,url):
        '''将该网址的内容按一定格式存入文件'''

        content = urllib2.urlopen(url).read()
        typeEncode = sys.getfilesystemencoding()
        html = content.decode('utf-8').encode(typeEncode)

        #编号及时间
        myindex0 = html.index('</h1><div><div id="description"><div></div>')
        len0=len('</h1><div><div id="description"><div></div>')
        #print html[myindex0+len0:myindex0+len0+52]

        #更新内容开始
        myindex1 = html.index('<td style="vertical-align:middle">')
        len1=len('<td style="vertical-align:middle">')

        #更新内容结束
        myindex2 = html.index('</td></tr><tr><td>')

        a= html[myindex1+len1:myindex2]
        #lidetailbegin= a.index('(<a href="changes#detail')
        #lidetailend= a.index('</j:text></li>')

        a, number = re.subn('<a href="changes#detail(1000|[1-9]?[0-9]?[0-9])', "", a) #可以用于正则的替换
        a=a.replace('(">detail</a><j:text xmlns:j="jelly:core">)</j:text></li>','');
        print a
       
        a=a.replace('<li>','')
        a=a.replace('<ol>','')
        a=a.replace('</ol>','')
        a=a.replace('<br />','')
        c='\n'.join(a.split())
        c= html[myindex0-50:myindex0]+c
        c=c+'\n----------------------------------------------------------------------------\n'
        print c

        f=file("ChangeLog.txt","a")
        li=c
        f.writelines(li)
        f.close()
        return
 
    def login(self):
        '''登录网站'''     
        loginparams = {'domain':self.domain,'j_username':self.name, 'j_password':self.pwd}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20' }
        req = urllib2.Request(loginurl, urllib.urlencode(loginparams),headers=headers) 
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()  
    def a(self,c):
        countnum=74
        while (countnum > 20):
           webname='http://120.27.147.44:8080/job/prod-deploy-zensuo/'
           userlogin.printa('%s%s'%(webname,countnum))
           countnum = countnum - 1

if __name__ == '__main__':   
    userlogin = Login()
    #此处需要替换为你的登录名和密码
    username = 'username'
    password = 'password'
    domain = logindomain
    userlogin.setLoginInfo(username,password,domain)
    userlogin.login()
    userlogin.a('v')
  #  userlogin.printa("http://120.27.147.44:8080/job/prod-deploy-zensuo/62/")
