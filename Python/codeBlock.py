#python 代码块 用缩进来划分代码块，不像其他语言的用{}或then...end
#注意代码块的开始要用:标记起始 从分号开始 的缩进都属于同一块代码
a=100;
if a>0 :
	print("if block")
	print("hello if block",a)
else:
	print("else block")
print("out block")

#从分号后面开始立即就属于一个代码块了，而不是等到换行。
#但是结束一个代码块一定是一个换行，并且是顶格的代码
#所以不能在同一行开始另一个代码块，必须换行。即 else不能和if写在同一行
if(a>0):print("pp") 
else:print("llp")

#pass关键字
#定义了一个代码块之后不能什么也不做就结束，像其他语言那样 if()之后留空 直接else是不可以的
#想定义一个空的代码块的话要使用一个pass关键字 
if(a>0):
	pass
else:
	print("ppp")

#另外，一条语句不能随意的有缩进，因为缩进代表了一个代码块，
#所以如果没有条件或循环分支，或是定义函数等的，代码必须顶格写
#	print("hello") 像这样的代码是不被允许的 它会被归属到上一个代码块，若没有上一个代码块则会运行出错

