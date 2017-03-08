#装饰器函数
#乍看@log，打在一个函数定义的上边，还以为是类似C#的特性标签的一个东西。
#而实际上这个装饰器函数就是给原函数又封装了一层，中间干了点别的事。
#而比较神奇的地方在于虽然封装了一层函数，但是调用的时候只需要调原函数就行了。
#一个decorator

def log(func):
	def wrapper(*args,**kw):
		print("begin call");
		res= func(*args,**kw);
		print("end call");
		return res
	return wrapper;

@log
def f():
	print("real func");

f();

#这里定义@log f()的时候 实际上等同于做了一个 f=log(f);的操作。
#把f这里的函数作为参数传给上边定义的log函数。
#而log函数又返回了一个wrapper函数，所以这样定义之后f就指向了wrapper函数。
#wrapper再调用由log带进来的func，并干了些事情。 这里实际上是个闭包了应该。
#而wrapper函数又定义了一个可变参数可关键字参数，
#这就使得不管func有什么类型的参数，都可以通过wrapper的完美地传递；
#因为后面调f()的时候实际上调起的是wrapper，传给f的参数之后会由wrapper完整地传递给原始的f()函数。
#然后由于原始的f()函数可能会有返回值，所以为了保证正确的结果，在wrapper内调用f()的时候必须将其返回值返回。


#其实这种写法在其他语言中一般直接就是wrapper函数的这块定义，之后调用也是调的wrapper函数。
#C#里的话，借助委托可以达到类似的一种效果，但是之后调用的也一定是个委托，直接修改原函数是不可能的。
#python的这种写法比较巧妙的就是 做的装饰器之后 调用的还是原来的函数变量。并且@func这种写法也很简洁。
#只是在其他语言中好像并不怎么用到类似这样的特性，估计python里应该也并不会常用这个特性吧。


#可以带参数的装饰器
def log_witharg(arg):
	def decorator(func):
		def wrapper(*args,**kw):
			print(arg,"begin call");
			res=func(*args,**kw);
			print("end call");
			return res;
		return wrapper;
	return decorator;

@log_witharg("hello fff")
def f2():
	print("f2222");
f2();

#这里定义了一个可以带一个参数的装饰器，在定义@log_witharg("hello fff") def f2()
#这步操作相当于是 先执行了log_witharg函数，并返回了一个decorator，然后再调这个返回的decorator函数，
#并传入此时定义的f2,这之后走的就是正常的无参的装饰器流程了。与上边的一致。
#定义log_witharg的时候可以传入任意的参数，算是扩展性更强吧，但我还是觉得这个用处不是很大。

#functools.wraps(func)装饰器。
#这个装饰器是python内置的一个装饰器，用来将func的函数属性复制给被装饰的函数。
#python里边函数具有一些属性，像是__name__什么的(怎么感觉像是个对象？),
#这个装饰器就是用来把一个函数的属性赋给另一个函数的。
#像上边的两个装饰器的定义，虽然改变了原函数的执行逻辑，但是原函数变量的指向也被更改了，
#那么它的一些原有的函数属性就也跟着变了，
#所以为了不引起错误，应该用这个装饰器把原函数的属性复制给之后的装饰器函数。
#修改上边的log_witharg:

import functools;

def log_witharg2(arg):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print(arg,"begin call");
			res=func(*args,**kw);
			print("end call");
			return res;
		return wrapper;
	return decorator;

@log_witharg2("hello fff")
def f3():
	print("f2222");
f3();
print(f3.__name__)#输出的是f3
print(f2.__name__)#输出的是wrapper

#functools.wraps装饰器被包含在python内置的functools模块里，所以得先import进来。
#直接将装饰标记打在装饰函数上边即可。因为functools.wraps本身也是一个装饰器，并且是一个带参数的装饰器，参数是个函数