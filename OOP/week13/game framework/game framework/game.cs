using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;
using System.Windows.Forms;

namespace game_framework
{
    class game
    {
        int speed;
        public game(int move_speed)
        {
            this.speed = move_speed;
        }
        public void addObject(gameObject objs)
        {
             PictureBox p= objs.return_picturebox();
             p.Top =p.Top + this.speed;
        }
    }
}
