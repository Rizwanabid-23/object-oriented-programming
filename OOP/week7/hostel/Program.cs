using System;
using System.Collections;

namespace week7
{
    class Program
    {
        static void Main(string[] args)
        {
            dayScholar ds= new dayScholar();
            hostellite h= new hostellite();
            ArrayList dayScholar_list= new ArrayList();
            ArrayList hostellite_list= new ArrayList();
            while(true)
            {   Console.Clear();
                Console.WriteLine("Student Management System");
                Console.WriteLine("");
                Console.WriteLine("1: Add student");
                Console.WriteLine("2: Search student");
                Console.WriteLine("Enter option: ");
                int option=int.Parse(Console.ReadLine());
                if(option==1)
                {
                        Console.Clear();                       
                        Console.WriteLine("Enter name of student: ");
                        string name= Console.ReadLine();
                        Console.WriteLine("Enter session: ");
                        int session=int.Parse(Console.ReadLine());
                        Console.WriteLine("Enter entery test marks: ");
                        float entry_test=float.Parse(Console.ReadLine());
                        Console.WriteLine("Enter high school marks: ");
                        float hs_marks= float.Parse(Console.ReadLine());
                        Console.WriteLine("Is student dayscholar (y/n) ? ");
                        string status= Console.ReadLine();
                        if(status=="y")
                        {
                            ds.name=name;
                            ds.session=session;
                            ds.entryTestMarks=entry_test;
                            ds.HSmarks=hs_marks;
                            Console.WriteLine("Enter pick-up point: ");
                            string pick_up= Console.ReadLine();
                            Console.WriteLine("Enter bus number: ");
                            int bus_num= int.Parse(Console.ReadLine());
                            Console.WriteLine("Enter distance: ");
                            float distance= float.Parse(Console.ReadLine());
                            ds.pickUp= pick_up;
                            ds.bus_no=bus_num;
                            ds.distance=distance;
                            dayScholar_list.Add(ds);
                        }
                        if(status=="n")
                        {
                            Console.WriteLine("Is student a hostellite (y/n) ?");
                            string opinion= Console.ReadLine();
                            if(opinion=="y")
                            {
                                Console.WriteLine("Enter room number: ");
                                int room_no=int.Parse(Console.ReadLine());
                                Console.WriteLine("Is fridge available (yes/no)?");
                                string isFridgeAvailable= Console.ReadLine();
                                Console.WriteLine("Is internet available (yes/no)? ");
                                string isInternetAvailable= Console.ReadLine();
                                h.name=name;
                                h.session=session;
                                h.entryTestMarks=entry_test;
                                h.HSmarks=hs_marks;
                                h.room_number=room_no;
                                h.fridge=isFridgeAvailable;
                                h.internet=isInternetAvailable;
                                hostellite_list.Add(h);
                            }
                            else
                            {
                                Console.WriteLine("Aray kehna kya chahtay ho?");
                                Console.ReadKey();
                            }
                        }
                        Console.WriteLine("press any key to continue...");
                        Console.ReadKey();
                }
                if(option==2)
                {
                    Console.Clear();
                    Console.WriteLine("Search student");
                    Console.WriteLine("Enter name: ");
                    string name= Console.ReadLine();
                    Console.WriteLine("is student day-scholar or hostellite (d/h)?");
                    string status=Console.ReadLine();
                    if(status=="d")
                    {
                        dayScholar days= new dayScholar();
                        Console.WriteLine("Name     Session     High school marks   Entry test    Bus no   Pick up     Distance   Fees");
                        for(int i=0;i<dayScholar_list.Count;i++)
                        {
                            dayScholar day=(dayScholar)dayScholar_list[i];
                            if(day.name==name)
                            {
                                Console.WriteLine(day.name+"        "+day.session+"        "+day.HSmarks+"        "+day.entryTestMarks+"      "+day.bus_no+"        "+day.pickUp+"        "+day.distance+"      "+days.get_fee());

                            }
                        }
                      
                    }
                    if(status=="h")
                    {
                        hostellite hostel= new hostellite();
                        Console.WriteLine("Name     Session     High school marks   Entry test    Room no   Fridge     Internet   Fees");
                        for(int i=0;i<hostellite_list.Count;i++)
                        {
                            hostellite host=(hostellite)hostellite_list[i];
                            if(host.name==name)
                            {
                                Console.WriteLine(host.name+"    "+host.session+"       "+host.HSmarks+"         "+host.entryTestMarks+"       "+host.room_number+"        "+host.fridge+"     "+host.internet+"     "+host.get_fee());

                            }
                        }
                        
                    }
                    Console.WriteLine("Press any key to continue...");
                    Console.ReadKey();
                }   
            }
        }
    }
    class hostellite:student
    {
        public int room_number;
        public string fridge;
        public string internet;
        public float get_fee()
        {
            float fee=base.get_fee();
            fee= fee+2000;
            return fee;
        }
    }
    class dayScholar:student
    {
        public int bus_no;
        public string pickUp;
        public float distance;
    }
    class student
    {
        public string name;
        public int session;
        public float entryTestMarks;
        public float HSmarks;
 
        public float get_fee()
        {
            int subjects=3;            
            float price=4000;
            float fee=price*subjects;
            return fee;
        }
    }
}
