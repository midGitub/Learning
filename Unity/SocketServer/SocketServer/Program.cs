using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using System.Net.Sockets;
using System.Net;
using System.Threading;
namespace SheepsServer
{
    public class Server
    {
        public Socket socket;
        public string ip = "192.168.229.1";
        public int port = 8888;
        public List<Socket> ClientList;
        public Server()
        {
            ClientList = new List<Socket>();
            socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            IPAddress address = IPAddress.Parse(ip);
            IPEndPoint ipe = new IPEndPoint(address, port);
            socket.Bind(ipe);
            socket.Listen(1000);
            Thread listenproccess = new Thread(ListenClientConnect);
            listenproccess.Start();
        }

        void ListenClientConnect()
        {
            while (true)
            {
                Socket client = socket.Accept();
                ClientList.Add(client);
                Console.WriteLine("Client " + client.RemoteEndPoint.ToString() + " accepted!");
                ThreadPool.QueueUserWorkItem(ReceiveMsg, client);
            }
        }


        void ReceiveMsg(object clientsocket)
        {
            while (true)
            {
                Socket client = (Socket)clientsocket;
                byte[] buffer = new byte[1024];

                int len = client.Receive(buffer);

                byte[] data = new byte[len];
                Array.Copy(buffer, 0, data, 0, len);

                string clientaddress = client.RemoteEndPoint.ToString();
                string resp = Encoding.UTF8.GetString(data);

                Console.WriteLine("receive from Client " + clientaddress + " :" + resp);
               
                for (int i = 0; i < ClientList.Count; i++)
                {
                    ClientList[i].Send(System.Text.Encoding.UTF8.GetBytes(resp));
                    Console.WriteLine("send :"+resp);
                }
                    
            }


        }


        public void CloseServer()
        {

            if (socket != null)
            {
                socket.Close();
                socket.Dispose();
                socket = null;
            }

        }
        static void Main(string[] args)
        {
            Server server = new Server();
            Console.ReadLine();
            server.CloseServer();
        }
    }


}
