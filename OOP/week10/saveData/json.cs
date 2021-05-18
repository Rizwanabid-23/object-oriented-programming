using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace saveData
{
    class json:mainClass
    {
        public override void save_csv(string data)
        {
            throw new NotImplementedException();
        }
        public override void save_js(string data)
        {
            string first = get_ID(data, 0);
            string second = get_ID(data, 1);

            File.AppendAllText("D:\\semester2\\OOP\\week10\\saveData\\data.json", null);
            data = "{Country:" + first + ";Wins:" + second + "}";
            File.AppendAllText("D:\\semester2\\OOP\\week10\\saveData\\data.json", data+"\n");
        }
        private string get_ID(string statement, int position)
        {
            int idx = 0;
            int comma = 0;
            string word = "";
            while (idx < statement.Length)
            {
                char c = statement[idx];
                if (c == ',')
                {
                    comma++;
                }
                else if (comma == position)
                {
                    word = word + c;
                }
                idx++;
            }
            return word;
        }
    }
}
