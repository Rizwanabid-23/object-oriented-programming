using System;
using System.IO;

namespace week8
{
    class input
    {
        public static void getKey()
        {
            Console.WriteLine("enter your letter:");
            int letter = Console.Read();
            if (letter == keys.M)
            {
                Console.WriteLine("You pressed M");
            }
            else if (letter == keys.A)
            {
                Console.WriteLine("you pressed A");
            }
            else
            {
                Console.WriteLine("unknown key pressed");
            }

        }
    }
    public class keys
    {
        static public int M = 77;
        static public int A = 65;
    }
    class Program
    {
        static void Main(string[] args)
        {

            input.getKey();

        }
    }
}
