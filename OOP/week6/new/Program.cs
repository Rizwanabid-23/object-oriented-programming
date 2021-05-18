using System;
using System.Collections;
namespace MailSystem
{
    public sealed class MailUser_CRUD   //singleton pattern
    {
        private MailUser_CRUD() //private constructor
        {
         }
        private static MailUser_CRUD instance = null;   

        public static MailUser_CRUD get_instance
        {
            get
            {
                if (instance == null)
                {
                    instance = new MailUser_CRUD();
                }
                return instance;
            }
        }
        private ArrayList allUsers = new ArrayList();   //declaring private list to hold admin names and passwords
        public void addUser(string userName, string userPin)    //adds admin 
        {
            MailUser u1 = new MailUser();   //calls class MailUser from line48
            u1.setName(userName);
            u1.setPin(userPin);
            allUsers.Add(u1);   //appending objects in list
        }
        public string isValidUser(string name, string password)     // a function to check if admin exists
        {
            for (int i = 0; i < allUsers.Count; i++)
            {
                MailUser user = (MailUser)allUsers[i];
                if (user.getPin() == password && user.getName() == name)
                {
                    return "admin"; //only if admin exists
                }
            }
            //if its not admin,check if its a user
            users_manager check = users_manager.get_instance;   //creating object of another class
            string a = check.isValidUser(name, password);   //calling a function of class (line99)
            return a;   //returning string
        }
    }


    class MailUser // a class which works corresponding to MailUser_CRUD for admin related work
    {
        private string userName;
        private string userPin;
        public void setName(string name)
        {
            this.userName = name;
        }
        public void setPin(string pin)
        {
            this.userPin = pin;
        }
        public string getName()
        {
            return this.userName;
        }
        public string getPin()
        {
            return this.userPin;
        }
    }


    public sealed class users_manager   //a singleton class for users
    {
        string logged_in;   //a variable to store which user is logged in
        private users_manager() //private constructor
        {

        }
        private static users_manager instance = null;   
        public static users_manager get_instance    // this checks if this class has been called single time or multiple imes
        {
            get
            {
                if (instance == null)
                {
                    instance = new users_manager();
                }
                return instance;
            }
        }
        private ArrayList user_list = new ArrayList();  //declaring a list to store users
        public void addUser(string username, string password)   //a function to add users
        {
            M_users u1 = new M_users();     //creating a object of class M_users from line127
            u1.setName(username);
            u1.setPin(password);
            user_list.Add(u1);  //appending the object in list
        }
        public string isValidUser(string name, string password) //a function to check if the user exists
        {
            for (int i = 0; i < user_list.Count; i++)
            {
                M_users user = (M_users)user_list[i];
                if (user.getPin() == password && user.getName() == name)
                {
                    logged_in = name;
                    return "user";  //if user exists

                }
            }
            return "false"; //if user does not exist
        }
        public void printUsers()    // a function to print all users
        {
            for (int i = 0; i < user_list.Count; i++)
            {
                M_users user = (M_users)user_list[i];   //takes out objects from list and convert them to class of M_users
                Console.WriteLine(user.getName());  
            }
        }
        public string get_loggedin()    //a function to check which user is logged in
        {
            return logged_in;
        }
    }

    class M_users       // a class which works correspondingly with class user_manager to work for users only
    {
        private string userName;
        private string userPin;
        public void setName(string name)
        {
            this.userName = name;
        }
        public void setPin(string pin)
        {
            this.userPin = pin;
        }
        public string getName()
        {
            return this.userName;
        }
        public string getPin()
        {
            return this.userPin;
        }
    }

    public sealed class message_manager   // a class to manage messages
    {
        private ArrayList message_list= new ArrayList();    //declaring array to store sender,receiver and message
        private message_manager()   //private constructor
        {
        }
        private static message_manager instance= null;
        public static message_manager getInstance
        {
            get
            {
                if(instance==null)
                {
                    instance= new message_manager();
                }
                return instance;
            }
        }
        public void send_messages(string sender,string receiver, string message)    //a function to store messages
        {
            messages m=new messages();
            m.set_sender(sender);
            m.set_receiver(receiver);
            m.set_message(message);
            message_list.Add(m);    //adds information to message_list
        }
        public void received_messages(string logged_in) //gets the user who is logged in and displays his received messages
        {
            string rec;
            Console.WriteLine("Message"+"    "+"Sender");
            for(int i=0;i<message_list.Count;i++)
            {
                messages msg=(messages)message_list[i];
                rec=msg.get_receiver();
                if(rec==logged_in)  //checking if looged in user matches the user from list
                {
                    Console.WriteLine(msg.get_message()+"   "+msg.get_sender());
                }
                
            }
        }
    }

    class messages  //a class working correspondingly with message_manager class
    {
        private string sender;
        private string receiver;
        private string message;

        public void set_sender(string sender)
        {
            this.sender=sender;
        }
        public void set_receiver(string receiver)
        {
            this.receiver=receiver;
        }
        public void set_message(string message)
        {
            this.message=message;
        }
        public string get_sender()
        {
            return this.sender;
        }
        public string get_receiver()
        {
            return this.receiver;
        }
        public string get_message()
        {
            return this.message;
        }
    }


    class Program
    {
        static void Main(string[] args)
        {
            int option = 0;
            //creating all objects of class globally
            MailUser_CRUD us = MailUser_CRUD.get_instance;
            users_manager manager = users_manager.get_instance;
            message_manager mes= message_manager.getInstance;
            while (option != 3)
            {
                //first screen which asks if u want to add new admin or sign him up
                option = 0;
                Console.Clear();
                Console.WriteLine("*** Main Screen ***");
                Console.WriteLine(" ");
                Console.WriteLine("1: Sign in");
                Console.WriteLine("2: Sign up admin");
                Console.WriteLine("3: Exit");
                Console.WriteLine("");
                Console.WriteLine("Enter your option: ");
                option = int.Parse(Console.ReadLine());
                us.addUser("a", "1"); //pre defined info for admin

                if (option == 1)
                {
                    Console.Clear();
                    Console.WriteLine("Enter Username: ");
                    string name = Console.ReadLine();
                    Console.WriteLine("Enter Password: ");
                    string password = Console.ReadLine();

                    string found = us.isValidUser(name, password);
                    if (found == "admin")
                    {
                        int admin_option = 0;
                        while (admin_option != 3)
                        {
                            admin_option=0;
                            Console.Clear();
                            Console.WriteLine("-- Admin menu --");
                            Console.WriteLine("1: Add new users");
                            Console.WriteLine("2: View all users");
                            Console.WriteLine("3: Log out");
                            Console.WriteLine("");
                            Console.WriteLine("Ener your option: ");
                            admin_option = int.Parse(Console.ReadLine());

                            if (admin_option == 1)
                            {
                                Console.Clear();
                                Console.WriteLine("-- Add user --");
                                Console.WriteLine("Enter username: ");
                                string Uname = Console.ReadLine();
                                Console.WriteLine("Enter password: ");
                                string Upin = Console.ReadLine();
                                manager.addUser(Uname, Upin);
                            }
                            if (admin_option == 2)
                            {
                                Console.Clear();
                                Console.WriteLine("Following users are enrolled:");
                                manager.printUsers();
                                Console.ReadKey();
                            }
                        }
                    }
                    else if (found == "user")
                    {   int user_option=0;
                        while(user_option!=3)
                        { 
                            Console.Clear();
                            Console.WriteLine("--User menu--");
                            Console.WriteLine("1: Send message");
                            Console.WriteLine("2: Show received messages");
                            Console.WriteLine("3: Log out");
                            Console.WriteLine("");
                            Console.WriteLine("Enter your option: ");
                            user_option = int.Parse(Console.ReadLine());
                            if (user_option == 1)
                            {
                                Console.Clear();
                                Console.WriteLine("Send messages");
                                Console.WriteLine("-------------");
                                Console.WriteLine("Following users are available: ");
                                manager.printUsers();
                                Console.WriteLine("----------------");
                                Console.WriteLine("Enter receiver:");
                                string receiver = Console.ReadLine();
                                Console.WriteLine("Enter message");
                                string message = Console.ReadLine();
                                string sender = manager.get_loggedin();

                                mes.send_messages(sender, receiver, message);
                                Console.ReadKey();
                            }
                            if(user_option==2)
                            {
                                Console.WriteLine("Following messages are received: ");
                                string logged_in=manager.get_loggedin();
                                mes.received_messages(logged_in);
                                Console.WriteLine("Press any key to continue...");
                                Console.ReadKey();
                            }
                        }
                    }
                    else
                    {
                        Console.WriteLine("user not found...");
                    }
                    Console.WriteLine("Press any key to continue...");
                    Console.ReadKey();
                }
                if (option == 2)
                {
                    Console.Clear();
                    Console.WriteLine("* Admin sign up *");
                    Console.WriteLine("Enter username:");
                    string name = Console.ReadLine();
                    Console.WriteLine("Enter password:");
                    string pin = Console.ReadLine();
                    us.addUser(name, pin);
                    Console.WriteLine("Press any key to continue...");
                    Console.ReadKey();
                }

            }
        }

    }
}


