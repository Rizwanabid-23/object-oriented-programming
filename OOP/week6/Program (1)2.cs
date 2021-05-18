using System;
using System.IO;
using System.Collections;

namespace Signin
{
    // class to add user and verify login as well
    class MailUserCRUD{
        private ArrayList allUsers = new ArrayList();
        public void addUser(string name, string pin){ // add user to user class
            users obj = new users();
            obj.userName = name;
            obj.password = pin;
            allUsers.Add(obj);
                 
        }
        public bool verifyUsers(string userName, string password){ // check whole list and verify if user exists
            bool found = false;
            for (int i=0; i<allUsers.Count;i++){
                users user = (users) allUsers[i]; //conversion
                if(user.userName == userName && user.password == password){
                    found = true;
                }

            }
            if (found == false){
                return false;
            }else{
                return true;
            }
        }
    }
    // class holding users info 
    class users{
        public string userName;
        public string password;
        
    }
    // main method 
    class Program
    {
        static void Main(string[] args)
        {
            
            int option = 0;
            MailUserCRUD user = new MailUserCRUD();
            // adding some pre existing users!
            user.addUser("umair", "CS24");
            user.addUser("Talha", "CS39");
            user.addUser("Rizwaan", "CS23");

            while(option != 3){ // options
                Console.Clear();
                Console.WriteLine("#######################################");
                Console.WriteLine("       APPLICATION SIGNIN/ SIGNUP      ");
                Console.WriteLine("#######################################");
                Console.WriteLine("1- Login");
                Console.WriteLine("2- Signup");
                Console.WriteLine("3- Exit");
                Console.WriteLine("Enter ");
                option = int.Parse(Console.ReadLine());    
                // taking input
                Console.WriteLine("\n*Username: \t");            
                string name = Console.ReadLine();
                Console.WriteLine("\n*Password: \t");
                string password = Console.ReadLine();            
                 
                if (option == 1){
                    

                    // objects to CRUD class
                    bool found = user.verifyUsers(name, password);
                    if (found == true){
                        Console.WriteLine("Loggedin successfully!");
                    }else{
                        Console.WriteLine("User Not found");
                    }
                    Console.ReadKey();
                }else if(option == 2){
                    user.addUser(name, password); // add user
                    Console.WriteLine("User added successfully!...");
                    Console.ReadKey();
                }            

            }
        }

    }
}
