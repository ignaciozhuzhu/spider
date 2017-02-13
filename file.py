#! /usr/bin/python
# -*- coding: utf-8 -*- 
f=file("hello.txt","w+")

li=["hell是o world\n","he22llo china\n"]

f.writelines(li)

f.close()