using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;

namespace RGY
{
    class greenClass:mainClass
    {
        Color textboxcolour=Color.Green;
        public greenClass()
        {
            this.textboxcolour = System.Drawing.Color.Green;
        }
        public mainClass nextState()
        {
            return new yellowClass();
        }
        public mainClass prevState()
        {
            return new redClass();
        }
        public Color GetColor()
        {
            return textboxcolour;
        }
    }
}
