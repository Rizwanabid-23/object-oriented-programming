using System;

namespace week11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("do you want to start the game? (Y/N) :");
            char opinion = char.Parse(Console.ReadLine());
            if (opinion == keys.Y)
            {
                scenerio1 first = new scenerio1();
                first.scenerio();
            }
        }
    }
    class scenerio_decider
    {
        public static void first(int option)
        {
            if (option == keys.A)
            {
                scenerio1A second = new scenerio1A();
                second.scenerio();
            }
            if (option == keys.B)
            {
                scenerio1B second = new scenerio1B();
                second.scenerio();
            }
            if (option == keys.C)
            {
                scenerio1C second = new scenerio1C();
                second.scenerio();
            }
        }
        
        public static void second(int option)
        {
        }
    }

    abstract class scenerios
    {
        public abstract void scenerio();
    }

    class scenerio1 : scenerios
    {
        public override void scenerio()
        {
            Console.Clear();
            Console.WriteLine(" A knight charges up the slope at you. His horse pounds at the ground, carrying the heavily armored warrior as if he were a child's doll.\n The knight sets his lance to attack you. How do you defend yourself, O mighty dragon ? ");
            Console.WriteLine("\n A: I take to the air with a quick beat of my wings.");
            Console.WriteLine("\n B: I knock the knight from his horse with a slap of my tail.");
            Console.WriteLine("\n C: I rush into his charge and tear him to pieces with my claws.");
            Console.WriteLine("");
            Console.WriteLine("Enter your option: ");

            char option = char.Parse(Console.ReadLine());
            scenerio_decider.first(option);
        }
    }

    class scenerio1A : scenerios
    {
        public override void scenerio()
        {
            Console.Clear();
            Console.WriteLine("u took option 1: I take to the air with a quick beat of my wings.");
            Console.WriteLine("\n A: Of course! How dare he attack me?");
            Console.WriteLine("\n B: I let him live to warn others of my immense power.");
            Console.WriteLine("\n C: Eh. Now that the threat is ended, he is beneath my concern.");
            Console.WriteLine("");
            Console.WriteLine("Enter your option: ");
            char option = char.Parse(Console.ReadLine());
            scenerio_decider.second(option);
        }
    }
    class scenerio1B : scenerios
    {
        public override void scenerio()
        {
            Console.Clear();
            Console.WriteLine("u took option 2:I knock the knight from his horse with a slap of my tail.");
            Console.WriteLine("\n A: Of course! How dare he attack me?");
            Console.WriteLine("\n B: I let him live to warn others of my immense power.");
            Console.WriteLine("\n C: Eh. Now that the threat is ended, he is beneath my concern.");
            Console.WriteLine("Enter your option: ");
            char option = char.Parse(Console.ReadLine());
            scenerio_decider.second(option);
        }
    }

    class scenerio1C : scenerios
    {
        public override void scenerio()
        {
            Console.Clear();
            Console.WriteLine("u took option3 :I rush into his charge and tear him to pieces with my claws.");
            Console.WriteLine("\n A: Of course! How dare he attack me?");
            Console.WriteLine("\n B: I let him live to warn others of my immense power.");
            Console.WriteLine("\n C: Eh. Now that the threat is ended, he is beneath my concern.");
            Console.WriteLine("Enter your option: ");
            int option = Console.Read();
            scenerio_decider.second(option);
        }
    }


    class keys
    {
        static public int A = 65;
        static public int B = 66;
        static public int C = 67;
        static public int D = 68;
        static public int E = 69;
        static public int F = 70;
        static public int G = 71;
        static public int H = 72;
        static public int I = 73;
        static public int J = 74;
        static public int K = 75;
        static public int L = 76;
        static public int M = 77;
        static public int N = 78;
        static public int O = 79;
        static public int P = 80;
        static public int Q = 81;
        static public int R = 82;
        static public int S = 83;
        static public int T = 84;
        static public int U = 85;
        static public int V = 86;
        static public int W = 87;
        static public int X = 88;
        static public int Y = 89;
        static public int Z = 90;
        static public int up = 38;
        static public int down = 40;
        static public int right = 39;
        static public int left = 37;
        static public int space = 32;
    }
}
