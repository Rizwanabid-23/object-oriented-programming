using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace saveData
{
    class csv:mainClass
    {
        public override void save_csv(string data)
        {
            File.AppendAllText("D:\\semester2\\OOP\\week10\\saveData\\data.txt", data+"\n");
        }
        public override void save_js(string data)
        {
            throw new NotImplementedException();
        }
    }
}
