using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

namespace rgy
{
    class window:Form
    {
        public Button next;
        public Button prev;
        public TextBox box;

        public window()
        {
            work();
            addControls();
        }

        private void work()
        {
            this.Size=new Size(600,700);
            this.Text= "red green yellow";
            this.Location=new Point(80,120);

            next=new Button();
            next.Text="Next";
            next.Location=new Point(35,70);
            next.Click += new EventHandler(nxt_color);

            prev= new Button();
            prev.Text="previous";
            prev.Location=new Point(35,35);
            prev.Click += new EventHandler(prev_color);

            box= new TextBox();
            box.PlaceholderText="box";
            box.Location=new Point(33,100);
        }
        public void nxt_color(object sender,EventArgs e)
        {
            box.BackColor=System.Drawing.Color.Red;
        }
        public void prev_color(object sender, EventArgs e)
        {
            box.BackColor=System.Drawing.Color.Yellow;
        }
        private void addControls()
        {
            this.Controls.Add(next);
            this.Controls.Add(prev);
            this.Controls.Add(box);
        }
    }
    class change_color
    {
        public int a=1;
        public int b=2;
        public int c=3;
        public int x=4;
        public int y=5;
        public int z=6;

        void change_next()
        {
            
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            window win= new window();
            Application.EnableVisualStyles();
            Application.Run(win);
        }
    }
}
