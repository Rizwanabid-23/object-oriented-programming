using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;

namespace RGY
{
    interface mainClass
    {
      //  Color textboxcolour =new Color();

        mainClass nextState();
        mainClass prevState();

        Color GetColor();
        
    }
}
