using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RGY
{
    class mainClass
    {

        public System.Drawing.Color textboxcolour;
        public virtual mainClass nextState()
        {
            return null;
        }
        public virtual mainClass prevState()
        {
            return null;
        }
    }
}
