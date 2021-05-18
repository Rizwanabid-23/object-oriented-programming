using System;
using System.Collections;

namespace Signin
{
    // class to add user and verify login as well
    class MailUserCRUD{
        private ArrayList allUsers = new ArrayList();
        private void addUser(string name, string pin){ // add user to user class
            users obj = new users();
            obj.userName = name;
            obj.password = pin;
            allUsers.Add(obj);
  

        }
        private void signup(){
            Console.WriteLine("\n*Username: \t");            
            string name = Console.ReadLine();
            Console.WriteLine("\n*Password: \t");
            string password = Console.ReadLine();
            addUser(name, password);
            Console.WriteLine("User added successfully!...");
            Console.ReadKey();

        }
        public void driver(){ // only this is public
        int option = 0;
            while(option != 3){ // options
                Console.Clear();
                Console.WriteLine("#######################################");
                Console.WriteLine("       APPLICATION SIGNIN/ SIGNUP      ");
                Console.WriteLine("#######################################");
                Console.WriteLine("1- Signup");
                Console.WriteLine("2- Signin");
                Console.WriteLine("3- Exit");
                Console.WriteLine("Enter ");
                option = int.Parse(Console.ReadLine());

                if (option == 1){
                    signup();
                }else if(option == 2){
                    signin();
                }            

            }
        }
        private void signin(){
            // user input
            Console.WriteLine("\n*Username: \t");            
            string name = Console.ReadLine();
            Console.WriteLine("\n*Password: \t");
            string password = Console.ReadLine();
            bool found = verifyUsers(name, password);// verify existing user in CURD class
            if (found == true){
                Console.WriteLine("it works!");
            }else{
                Console.WriteLine("Need time!");
            }
            Console.ReadKey();
        }
        private bool verifyUsers(string userName, string password){ // check whole list and verify if user exists
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
            MailUserCRUD obj = new MailUserCRUD();
            obj.driver(); // add user
            

        }

    }
}
