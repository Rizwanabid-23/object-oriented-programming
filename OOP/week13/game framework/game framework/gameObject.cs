using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing;

namespace game_framework
{
    class gameObject
    {
        PictureBox box;
        public gameObject(PictureBox pic)
        {
            pic.BackColor = Color.Red;
            pic.Visible = true;
            this.box = pic;
        }
        public PictureBox return_picturebox()
        {
            return this.box;
        }
    }
}
