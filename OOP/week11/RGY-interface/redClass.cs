using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;

namespace RGY
{
    class redClass:mainClass
    {
        Color textboxcolour=Color.Red;
        public redClass()
        {
            this.textboxcolour =System.Drawing.Color.Red;
        }
        public mainClass nextState()
        {
            return new greenClass ();
        }
        public mainClass prevState()
        {
            return new yellowClass ();
        }
        public Color GetColor()
        {
            return textboxcolour;
        }
    }
}
