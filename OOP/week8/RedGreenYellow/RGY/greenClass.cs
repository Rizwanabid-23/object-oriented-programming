using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RGY
{
    class greenClass:mainClass
    {
        
        public greenClass()
        {
            this.textboxcolour = System.Drawing.Color.Green;
        }
        public override mainClass nextState()
        {
            return new yellowClass();
        }
        public override mainClass prevState()
        {
            return new redClass();
        }
    }
}
