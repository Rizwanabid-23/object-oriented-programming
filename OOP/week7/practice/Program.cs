using System;

namespace practice
{
    class Program
    {
        static void Main(string[] args)
        {
            vehicle vehicle= new vehicle();
            car car = new car();
            vehicle.speed();
            vehicle.average();
            Console.WriteLine("");
            car.speed();
            car.average();
            Console.WriteLine("");
            vehicle=car;
            car.speed();
            car.average();
            Console.WriteLine("");
            vehicle.speed();
            vehicle.average();
        }
    }
    class vehicle
    {
        public virtual void speed()
        {
            Console.WriteLine("speed method of vehicle class is called");
        }
        public void average()
        {
            Console.WriteLine("avg method of vehicle class is called");
        }
    }
    class car:vehicle
    {
        public override void speed()
        {
            Console.WriteLine("override method speed is clled from car class");
        }
        public void average()
        {
            Console.WriteLine("average method of car class is called");
        }
    }
}
