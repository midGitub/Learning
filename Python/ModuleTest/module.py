#每个.py脚本都是一个模块
#使用模块可以避免函数或变量名冲突。因为对模块成员的调用必须是  模块名.成员名 的方式。
#但是模块内的变量名也不同跟内置函数或变量重名，不然内置成员就被隐藏了。

#import 
#使用import关键字包含一个模块。相当于include
import sys; #不过注意这个import并不会返回一个模块变量。被import的模块名 本省就是一个模块变量了。
print(sys.argv); #import之后直接通过模块名来访问成员。


#__name__
#__name__是个内置的特殊变量，当一个python被运行时，这个__name__会被赋值为__main__,
#大概是为了标记起始脚本用的吧，相当于main()函数。
#而当这个python不是作为起始脚本被运行，而是因为被import或者被通过模块调用的时候,__name__则会被赋值为模块名

print(__name__)#作为起始脚本运行 输出__main__
import __name__test #被import 输出 模块名 __name__test
__name__test.print__name__() #同样输出 __name__test


#__doc__
#同样也是python的内置变量， 编写模块时，写在第一行的字符串将会被赋值给这个变量，可以当作一个模块注释来使用
#注意一定得是第一行的字符串，如果不是第一行的，那么__doc__将会被赋一个None值
print(__name__test.__doc__)


#作用域
#在C/C++ 或 java c#中，变量都有作用域这个概念，不过遗憾的是python中并没有这个概念。
#在定义一个模块时无法限制某个变量或函数为私有或公有。 也就是一个模块的所有成员都可以被从外部访问到。
#但是python里也有个约定，约定了一些私有成员和公有成员的声明格式，还有一些特殊的内置成员
#像__xxx__这样的一般是python内置的变量，所以为了不会不小心污染了这些变量，尽量不要定义这种格式的变量
#像_xxx或__xxx这样的变量被约定为是私有的，不应该从外部去访问这些变量。
#而像xxx,a_b_c这样的则是可以随意访问的公有变量。

#package包
#包的存在是为了解决可能出现的模块重名的问题。因为编写一个模块的时候可能会与系统模块或者其他模块重名。
#python的包的设计跟java差不多，是按照目录结构来的。在一个目录下放一个__init__.py文件，这个目录就成为一个包了。
#__init__.py文件可以是空的，也可以有python代码，它本省就是这个包的模块代码，但是他的模块名并不是__init__，而是这个目录名。
#包可以有很多层，A包里再放一个B包，B再放一个C包，但是记得每层目录下都得有个__init__.py文件，不然就会被当成普通目录。
#像上面这样的访问C下的一个模块D的话，就是A.B.C.D了。但是A.B.C，A.B，A这些也同样是个模块，他们的模块代码在__init__.py里

#包含一个包里的模块的几种方式
#import a.b.c
#注意被包含的模块名应该是跟包名连在一起的，像这里的a.b.c模块，而不是c模块，后面访问的也应该是a.b.c
import  package_test.module_A
package_test.module_A.log()
package_test.log()
#包含package_test下的模块的同时，package_test模块本身也被import了。

#from ... import ...
#用import包含进来的模块，访问的时候得从第一个包名可是写，这确实有些麻烦的。
#python的from ... import ...方式，可以解放import的这个缺陷
from package_test import module_A
module_A.log()#直接使用模块名module_A即可

#__import__()
#这是个python的内置函数，import其实就是通过这个函数工作的。
#__import__()函数可以接收一个字符串参数，这个参数就是一个模块名，__import__将会包含这个模块，并返回一个模块变量，可以赋值给任意变量
mA=__import__("package_test")
print("this is mA ");mA.log()
mA.module_A.log()#注意这里import了包，但是实际上这个包下的模块也被import进来了
mA=__import__("package_test.module_A");
print("this is mA");mA.module_A.log()


#设置模块的搜索路径sys,path
#像lua有一个package.path储存了模块的查找路径，python也有一个模块的查找路径变量，这个变量在sys模块下的path中，这个path是个list
import sys
print(type(sys.path))
print(sys.path)#输出path的内容，发现包含了当前的运行目录路径，

#像lua的package.path一样，sys.path也可以被修改或添加，但这只是在运行时添加的，运行结束后就被还原了
sys.path.append("F:")
print(sys.path)