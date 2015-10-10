from flask import Flask, render_template, request, session
import utils

app = Flask(__name__)

@app.route("/period")
def period():
    return render_template("periodPopup.html")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    err = "Username already taken"
    if request.method == "POST":
        uname = request.form['username']
        pword = request.form['password']
        if utils.newUser(uname, pword) == 1:
            return render_template("/calender.html")
        else:
            return render_template("register.html", err=err)
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    err = "Incorrect username or password"
    if request.method == "POST":
        uname = request.form['username']
        pword = request.form['password']
        if utils.authenticate(uname, pword) == 1:
            return redirect(url_for('calender'))
        else:
            return render_template("login.html", err=err)
    return render_template("login.html")

@app.route("/logout")
def logout():
  return render_template("logout.html")


@app.route("/calender")
def calender():
  if verify():
    return render_template("calender.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
