from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/")
def hello():
    return render_template("base.html")

prod_list=[]


class product:
    id=0
    name=""
    sale_price=0
    purchase_price=0
    
    def __init__(self,identity,naam,sale_P,purchase_P):
        self.id=identity
        self.name=naam
        self.sale_price=sale_P
        self.purchase_price=purchase_P
    def stock(self):
        self.stock=0
    def print_file(self):
        file1=open("data.txt","a")
        record=self.id+","+self.name+","+str(self.sale_price)+","+str(self.purchase_price)+","+str(self.stock)
        print(record,file=file1,sep="\n")
        file1.close()
        
        
class viewProd:
    id=0
    name=""
    sale_price=0
    purchase_price=0
    stock=0
        
        
        

@app.route("/addProducts")
def addProd():
    return render_template("addProduct.html")


@app.route("/addProducts", methods=['GET', 'POST'])
def addForm():
    data = request.form
    Id = data['ID']
    data2 = request.form
    name = data2['name']
    data3=request.form['sale_price']
    sPrice=data3
    data4=request.form['purchase_price']
    pPrice=data4
    
    p=product(Id,name,sPrice,pPrice)
    p.stock()
    p.print_file()
    return render_template("addProduct.html")



def viewStock():  
    prod_list.clear()
    file1=open("data.txt","r")
    record=file1.read().splitlines()
    for i in record:
        identity = get_ID(i, 0)
        name = get_ID(i, 1)
        sale_price= get_ID(i,2)
        purchase_price=get_ID(i,3)
        stock=get_ID(i,4)
        p=viewProd()
        p.id=identity
        p.name=name
        p.sale_price=sale_price
        p.purchase_price=purchase_price
        p.stock=stock
        prod_list.append(p)
    file1.close()


def get_ID(dataTocheck, postion):
    idx = 0
    commaFound = 0
    word = ""
    while idx < len(dataTocheck):
        c = dataTocheck[idx]
        if c == ',':
            commaFound += 1
        elif (commaFound == postion):
            word = word + c
        idx += 1
    return word


@app.route("/viewStock")
def view():
    viewStock()
    return render_template("viewProduct.html",prod_list=prod_list)


@app.route("/addStock")
def st():
    return render_template("stock.html")


@app.route("/addStock",methods=['GET','POST'])
def addStock():
    stoc=0
    data=request.form
    identity=data['ID']
    data2=request.form
    stoc=data2['stock']
    viewStock()
    for i in prod_list:
        if i.id==identity:
            s=i.stock
            stoc=int(i.stock)+int(stoc)
            file=open("data.txt","rt")
            record=file.read()
            record=record.replace(i.stock,str(stoc))
            file.close()
            
            file=open("data.txt","wt")
            file.write(record)
            file.write("\n")
            file.close()
            
    return render_template("stock.html")


    

app.run(debug=True, host='192.168.10.15')

