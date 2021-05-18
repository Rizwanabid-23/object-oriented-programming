using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace saveData
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string data=this.textBox1.Text;
            csv csv = new csv();
            csv.save_csv(data);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string data = this.textBox1.Text;
            json json = new json();
            json.save_js(data);
        }
    }
}
