using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RGY
{
    class yellowClass:mainClass
    {
       
        public yellowClass()
        {
            this.textboxcolour = System.Drawing.Color.Yellow;
        }
        public override mainClass nextState()
        {
            return new redClass();
        }
        public override mainClass prevState()
        {
            return new greenClass();
        }
    }
}
