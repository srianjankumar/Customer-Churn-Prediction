from flask import Flask, render_template, request

app = Flask(__name__)# interface between my server and my application wsgi

import pickle
model = pickle.load(open(r'D:/Flask/model.pkl','rb'))

@app.route('/')#binds to an url
def helloworld():
    return render_template("index.html")

@app.route('/login', methods =['POST'])#binds to an url
def login():
    a=request.form["cs"]
    b= request.form["ag"]
    c= request.form["tn"]
    d= request.form["bl"]
    e= request.form["pd"]
    f= request.form["cd"]
    g= request.form["ac"]
    h= request.form["sl"]
    i= request.form["location"]
    if (i=="germany"):
        i1,i2=1,0
    if (i=="spain"):
        i1,i2=0,1
    if (i=="france"):
        i1,i2=0,0
    j= request.form["gender"]
    if (j=="male"):
        j1=1
    else :
        j1=0
    k=[[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h),int(i1),int(i2),int(j1)]]
    output= model.predict(k)
    print(output)  
        
    if (output==1):
        return render_template("index.html",y = "Yes,the customer is likely to leave the Bank")
    else :
        return render_template("index.html",y = "No,the customer will not leave the Bank")

#@app.route('/admin')#binds to an url
#def admin():
   # return "Hey Admin How are you?"

if __name__ == '__main__' :
    app.run(debug= False)
    
