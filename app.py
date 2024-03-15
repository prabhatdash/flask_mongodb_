from flask import Flask,request,render_template
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["naya"]
collection=db["btech"]


app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def index():  # put application's code here
    return render_template("index.html")

@app.route("/submit",methods=["GET","POST"])
def submit():
    username=request.form["username"]
    password=request.form["password"]
    collection.insert_one({"username":username,"password":password})
    data=collection.find()
    return render_template("dashboard.html",data=data)


if __name__ == '__main__':
    app.run()
