using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 观察者模式
{
    public class Subject
    {
        public Action onStateChanged;//这里用Func或自定义的delegate或开个list数组什么的都行
        public void Notify()
        {
            if (onStateChanged != null)
            {
                onStateChanged();
            }
        }
    }

    public class Observer1
    {
        public void DoSomething()//定义一个事件
        {
            Console.WriteLine("Oh! State Changed!");
        }
    }

    public class Observer2
    {
        public void SayHello()//定义一个事件
        {
            Console.WriteLine("Hello! New State!");
        }
    }


    public interface Eye//先定义一个“眼”的接口
    {
        void ThingHappen();      
    }
    public class Subject2
    {
        public List<Eye> eyes=new List<Eye>();//开一片草丛 用来插眼
        public void Notify()//有事情发生，通知所有插过眼的玩家
        {
            for(int i=0;i<eyes.Count;i++)
            {
                eyes[i].ThingHappen();
            }
        }
    }

    public class Observer3
    {
        public void ChaYan(Subject2 subject)//把眼插到草丛
        {
            subject.eyes.Add(new eye());//Java里边还可以写成匿名类
        }
        class eye : Eye//定义一个“眼”的内部类，实现接口，写好要做的事
        {
            public void ThingHappen()
            {
                Console.WriteLine("Oh!Enemy Passed!");
            }
        }

    }
    
    public class Observer4
    {
        public void ChaYan(Subject2 subject)
        {
            subject.eyes.Add(new eye());
        }
        class eye:Eye
        {
            public void ThingHappen()
            {
                Console.WriteLine("War's Comming!!");
            }
        }
    }


    public class Client
    {
      /*  static void Main(string[] args)
        {
            Subject subject = new Subject();
            Observer1 ob1 = new Observer1();
            Observer2 ob2 = new Observer2();
            subject.onStateChanged += ob1.DoSomething;//注册委托事件  C#中一个委托可以绑定多个事件
            subject.onStateChanged += ob2.SayHello;

            subject.Notify();

            Console.ReadLine();
        }*/
        static void Main(string []args)
        {
            Subject2 subject = new Subject2();
            Observer3 ob3 = new Observer3();
            Observer4 ob4 = new Observer4();
            ob3.ChaYan(subject);
            ob4.ChaYan(subject);

            subject.Notify();

            Console.ReadLine();
        }
    }
}
