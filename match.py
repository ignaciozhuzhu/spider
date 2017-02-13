# encoding: UTF-8 
import re 
s='<a href="changes#detail21ddd<a href="changes#detail23';
#result = s.replace("20215c2c10d3d1a3a", "") #只能用于字符串替换
#print result;
result, number = re.subn('<a href="changes#detail(100|[1-9]?[0-9])', "", s) #可以用于正则的替换
a='a'
b=111
print '%s%s'%(a,b)
#print number;