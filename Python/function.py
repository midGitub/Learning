#函数的定义
#定义一个函数 用def关键字
#函数体的代码块同样也要用冒号:和缩进来划分
def my_abs(x):
	if(x>=0):
		return x;
	else:
		return -x;

print(my_abs(-1))
print(my_abs(0))
print(my_abs(1))

#函数的返回值

#return 语句表示了一个函数的返回值。
#python属于弱类型的语言，声明函数的时候也并不用声明返回类型，
#所以python函数可以返回任意类型的返回值

#另外 其实python的每一个函数都是有返回值的，即使在定义函数的时候没有return语句，
#这个时候就会有一个默认的返回值 None
#而当只写了return，没有返回具体的值的时候，返回的也是一个None。
def Test_return(str):
	print("Test_return_",str)

print(Test_return("hello"))

def Test_return2(str):
	return;

print(Test_return2("hey~"))

#pass关键字
#要想定义一个空函数，直接留空代码块是不合法的，
#跟分支语句里的一样，想要一个空的代码块，需要用pass关键字标记
def Test_Empty():
	pass

print(Test_Empty())

#而用pass关键字标记过的代码块，若代码块内还有其他的语句，还是会被执行的，
#这个时候就相当于没有pass关键字了。
#所以pass其实只是一个占位的作用。相当于告诉解释器说：hey，这里是个代码块，是我的地盘。
def Test_Pass():
	print("before pass")
	pass
	print("after pass")
Test_Pass();


#参数类型检查
#由于python是弱类型的语言，所以调用函数的时候同样也能传任意类型的参数，
#这样就会导致函数内部执行的可能会出错，
#像上面的绝对值函数，如果传入一个字符串参数就报错了 print(my_abs("haha"))

#isinstance() 内置的一个函数，可以用来检查参数类型 修改上面的绝对值函数
def my_abs2(x):
	if not isinstance(x,(int,float)):
		print("type error")
		return

	if(x>=0):
		return x;
	else:
		return -x;

print(my_abs2("haha"))
print(isinstance("",str))

#isinstance还可以传一个tuple类型的参数，用来检查是否属于其中的某一种类型
print(isinstance(False,(bool,str)))

#多个返回值
#python的函数也可以有多个返回值
def Test_Return():
	return 1,0;
print(Test_Return())

x,y=Test_Return();
print(x,y)

#python函数的多个返回值实际上返回的是一个tuple，python把这多个返回值填到了一个tuple里再返回，
#所以实际上还是只有一个返回值的。只是这个tuple可以按照顺序把元素赋值给多个变量，所以看上去好像有多个返回值
r=Test_Return()#这里的r其实是一个tuple
print(r)
print(isinstance(r,tuple))

#默认参数
#与其他语言的默认参数一样，默认参数从右往左写就是了
def Test_DefaultArg(x,y=3,z=4):
	pass

#但是有一条，python的默认参数的默认值是在函数定义时就确定了的，
#所以如果默认参数的值是个对象，那么之后每次函数执行都会影响到这个默认值
#所以python的默认参数值不能是个对象引用
def Test_DefaultArg(l=[]):
	l.append("end")
	print(l)
Test_DefaultArg();
Test_DefaultArg();#第二次调用的时候发现默认值保留了上一次调用的结果

#可变参数
#python的可变参数 竟然是个指针 
#带星号的形参，其实是一个tuple 而*number则是一个指向这个tuple的指针 实际上是个指向tuple引用的指针
def calc(*numbers):
	print("***",numbers)#从这个输出可以看出numbers就是个tuple
	print("len",len(numbers))
	for x in numbers:
		print(x);

calc(1,2,3,4)
calc([5,6,7])#如过传一个list进去，则也只是占一个参数的位置
#若想传把一个list或tuple像多个参数那样传进去，则在list或tuple前加*
#那么传递的就是这个list的引用的引用
calc(*[7,8,9])

#关键字参数
#如果说上面的可变参数是指针的话，那么这个关键字参数就是指针的指针了。
#这个关键传递的是个dict,调用的时候可传可不传，不传其实就是个空的dict
def person(name,age,**kw):
	print(name,age,kw);

person("mot",25,city="oo",job="pp")
#说到指针又搞复杂了，这里还是简单的当成C#的param来用吧

#当要把一个dict像多个关键字参数那样传的时候，像可变参数那样，在dict前加两个星号 **
person("czp",25,**{"city":"hz","job":"mn"})

#注意这里对可变参数和关键字参数的list或tuple和dict传递的都是对原变量的一份拷贝
#函数内做的修改并不会影响到原来的变量

#命名关键字参数
#在函数定义时就确定了这个函数将会接收什么关键字的参数，就是命名关键字参数了
def person2(name,age,*,city,job):
	print(name,age,city,job);
person2("mot",25,city="hz",job="mn")
#像这样的定义，函数就将只会接收city和job关键字的关键字参数，若传递了其他关键字的参数则会报错
#这里注意当使用了可变参数的时候，用来定义命名关键字参数的*可以用可变参数来代替
#也就是写在可变参数后面的形参 都将被视为命名关键字参数 像下面这样
def person3(name,age,*args,city,job):
	print(name,age,args,city,job);
person3("mot",25,3,4,5,6,job="mn",city="hz")#这里注意调用时的命名关键字参数顺序不用跟声明时一致

#使用命名关键字参数还有一个好处就是可以为命名关键字参数设定默认值
#并且因为有关键字限定，这个默认值参数不用依照从右往左写的原则
def person4(name,age,*args,city="hz",job):
	print(name,age,args,city,job)
person4("mot",25,3,4,5,job="mn")

#小结
#函数这块 除了可变参数和关键字参数以及命名关键字参数，其余的都是基础，跟其他语言差不多。
#而可变参数又与C#的param关键字类似，用法也还算简单，
#关键字参数，尤其是命名关键字参数比较复杂，不过应该也比较少用到。
