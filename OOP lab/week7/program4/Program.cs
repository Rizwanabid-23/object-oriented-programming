using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

namespace program1
{
    class firstWindow:Form
    {

        public Button Button1;
        public TextBox textbox1;
        public Label outputLabel;
        public firstWindow()
        {
            init();
            addControls();
        }
        private void init()
        {
            this.Size = new Size(500,500);
            this.Text = "First program";
            this.Location = new Point(400,300);

            textbox1= new TextBox();
            textbox1.Location= new Point(190,170);
            textbox1.Size= new Size(100,100);

            Button1 = new Button();
            Button1.Text = "Click Me";
            Button1.Location = new Point(190,200);
            Button1.Size = new Size(100,30);
            Button1.Click += new EventHandler(button1_click);
        }
        private void button1_click(object sender, EventArgs e){
                textbox1.BackColor = System.Drawing.Color.Yellow;
                
                
        }
        private void addControls()
        {
            this.Controls.Add(Button1);
            this.Controls.Add(textbox1);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            firstWindow firstWindow = new firstWindow();
            Application.EnableVisualStyles();
            Application.Run(firstWindow);
        }
    }
}
