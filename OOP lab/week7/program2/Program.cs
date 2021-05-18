using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

namespace program1
{
    class firstWindow:Form
    {
        public Form form;
  
        public Label outputLabel;
        public firstWindow()
        {
            init();
            addControls();
        }
        private void init()
        {
            this.Size = new Size(500,500);
            this.Text = "Second program";
            this.Location = new Point(400,300);

            outputLabel = new Label();
            outputLabel.Location = new Point(160,170);
            outputLabel.Size = new Size(100,100);
            outputLabel.Text = "Hello world";
        }
        private void addControls()
        {
            this.Controls.Add(outputLabel);
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
