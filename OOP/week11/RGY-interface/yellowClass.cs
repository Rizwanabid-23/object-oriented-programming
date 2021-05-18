using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;

namespace RGY
{
    class yellowClass:mainClass
    {
        Color textboxcolour=Color.Yellow;
        public yellowClass()
        {
            this.textboxcolour = System.Drawing.Color.Yellow;
        }
        public mainClass nextState()
        {
            return new redClass();
        }
        public mainClass prevState()
        {
            return new greenClass();
        }
        public Color GetColor()
        {
            return textboxcolour;
        }
    }
}
