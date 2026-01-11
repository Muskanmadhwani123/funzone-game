from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("welcome.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form["Username"]
        password = request.form["password"]

        print("Username: ", username)
        print("Password: ",password)
             
    return render_template("login.html")

if __name__== "__main__":
    app.run(debug=True)