using System;
using System.Collections;
namespace lab
{
    public sealed class MailUserCRUD 
{
    // A private constructor to restrict the object creation from outside
    private MailUserCRUD()
    {
    }
    // A private static instance of the same class
    private static MailUserCRUD  instance = null;

    public static MailUserCRUD GetInstance()
    {
        // create the instance only if the instance is null
        if (instance == null)
        {
            instance = new MailUserCRUD();
        }
        // Otherwise return the already existing instance
        return instance;
    }
        private ArrayList allUsers = new ArrayList();
            public void addUser(string name, string pin)
            { // add user to user class
                users obj = new users();
                obj.setName(name);
                obj.setPin(pin);
                allUsers.Add(obj);
            }
            public bool verifyUsers(string userName, string password)
            { // check whole list and verify if user exists
                bool found = false;
                string name;
                string pin;
                for (int i=0; i<allUsers.Count;i++){
                    users user = (users) allUsers[i]; //conversion
                    name = user.getName();
                    pin = user.getPin();
                    if( name == userName && pin == password){
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
    class users{
        private string userName;
        private string password;
        public void setName(string name){
            this.userName = name;
        }
        public string getName(){
            return this.userName;
        }
        public void setPin(string password){
            this.password = password;
        }
        public string getPin(){
            return this.password;
        }       
    }
    // main method 
    class Program
    {
        static void Main(string[] args)
        {
            
            int option = 0;
            // objects to CRUD class
            MailUserCRUD user =  MailUserCRUD.GetInstance();
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
                 
                Program P = new Program();// object to call respective function

                if (option == 1){
                    P.signin();
                }else if(option == 2){
                    
                    P.signup();
                }            

            }
        }
        void signin(){
            // user input
            Console.WriteLine("\n*Username: \t");            
            string name = Console.ReadLine();
            Console.WriteLine("\n*Password: \t");
            string password = Console.ReadLine();
            // objects to CRUD class
            MailUserCRUD obj = MailUserCRUD.GetInstance();
            bool found = obj.verifyUsers(name, password);// verify existing user in CURD class
            if (found == true){
                Console.WriteLine("Loggedin successfully");
            }else{
                Console.WriteLine("User doesn't exists!");
            }
            Console.ReadKey();
        }
        void signup(){
            Console.WriteLine("\n*Username: \t");            
            string name = Console.ReadLine();
            Console.WriteLine("\n*Password: \t");
            string password = Console.ReadLine();
            // objects to CRUD class
            MailUserCRUD obj = MailUserCRUD.GetInstance();
            obj.addUser(name, password); // add user
            Console.WriteLine("User added successfully!...");
            Console.ReadKey();

    }
  }
}