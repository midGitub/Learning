using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using System.IO;
namespace Singleton
{
    #region 恶汉模式
    public class Singleton
    {
        public static readonly Singleton Instance=new Singleton();

        private Singleton()
        {
            Console.WriteLine("here is construction");
        }

        public string name;
  /*      static void Main(string[] args)
        {
            Singleton.Instance.name = "mot";
            Console.WriteLine(Singleton.Instance.name);
            Console.ReadLine();

        }*/
    }
    #endregion

    #region 懒汉模式
    public class Singleton2
    {
        private static Singleton2 instance;//这时后静态类实例得是private的了，防止被修改
        private static readonly object syncLock = new object();//创建一个object用于线程锁

        private Singleton2()
        {
            Console.WriteLine("here is in Singleton2's construction");
        }

        public static Singleton2 Instance//开个只读的全局访问点
        {
            get
            {
                if(instance==null)
                {
                    lock(syncLock)
                    {
                        if(instance==null)//这里得两次判断null，防止有多个线程同时到达锁外边
                        {
                            instance = new Singleton2();
                        }
                    }
                }
                return instance;
            }
        }

        public string name;
    /*    static void Main(string[] args)
        {
            Singleton2.Instance.name = "mot";
            Console.WriteLine(Singleton2.Instance.name);
            Console.ReadLine();

        }*/
    }
    #endregion

    #region 不是很饿的饿汉模式
    public class Singleton3
    {
        public static readonly Singleton3 Instance;
        private Singleton3()
        {
            Console.WriteLine("here is in Singleton3's construction");
        }
        static Singleton3()
        {
            Console.WriteLine("here is in static Singleton3's construction");
            if (Instance == null)
            {
                Instance = new Singleton3();
            }
        }
        public string name;
        static void Main(string []args)
        {
            Singleton3.Instance.name = "mot";
            Console.WriteLine(Singleton3.Instance.name);
            Console.ReadLine();
        }

    }
    #endregion
}
