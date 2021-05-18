using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace RGY
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        mainClass state;
        private void nextbutton_Click(object sender, EventArgs e)
        {
            state = state.nextState();
          //  textBox1.Text = state.colour;
            
            textBox1.BackColor = state.textboxcolour;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            state = new redClass();
            //  textBox1.Text = state.colour;
            textBox1.BackColor = state.textboxcolour;
        }

        private void prevbutton_Click(object sender, EventArgs e)
        {
            state = state.prevState();
            // textBox1.Text = state.colour;
            textBox1.BackColor = state.textboxcolour;
        }
    }
}
