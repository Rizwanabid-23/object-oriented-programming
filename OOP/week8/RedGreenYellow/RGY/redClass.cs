using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RGY
{
    class redClass:mainClass
    {
        
        public redClass()
        {
            this.textboxcolour =System.Drawing.Color.Red;
        }
        public override mainClass nextState()
        {
            return new greenClass ();
        }
        public override mainClass prevState()
        {
            return new yellowClass ();
        }
    }
}
