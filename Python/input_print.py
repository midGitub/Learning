# print

#可以有分号 也可以没有 写在同一行的语句要用分号隔开 否则以换行隔开就行了
print("hello world");print("other hello")

#print可以有任意个输出，每个输出参数之间以","隔开，输出时会被替换为空格
print("hello","world")

#print还可以输出整数，布尔型或等式都可以
print('hello world',666,3+2,True,3>2)

#input
#输入函数，输入得到的变量为字符串 sublime编译执行不了输入操作，要验证得在命令行下验证
print("inputed ",input());
a=input();
print("input val a ",a);

#input 还可以传入一个字符串参数，作为输出提示语 input输入得到都是字符串类型，要得到其他类型的需要转换
num=input("please Input a Number ");
print(int(num))