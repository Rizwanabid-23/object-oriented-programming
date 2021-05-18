using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace game_framework
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void tick(object sender, EventArgs e)
        {
            update();
        }
        public void update()
        {
            game g = new game(5);

            gameObject obj1 = new gameObject(enemy1);
            gameObject obj2 = new gameObject(enemy2);

            g.addObject(obj1);
            g.addObject(obj2);
        }
    }
}
