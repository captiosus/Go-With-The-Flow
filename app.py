from flask import Flask, render_template, request, session, redirect, url_for, session
import utils, time

app = Flask(__name__)

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
            utils.sess = utils.genToken();
            session['token'] = utils.sess;
            utils.logtime = time.gmtime()
            return redirect(url_for('calender'))
        else:
            return render_template("login.html", err=err)
    return render_template("login.html")

@app.route("/logout")
def logout():
  return render_template("logout.html")


@app.route("/calender")
def calender():
    if 'token' not in session:
        return render_template("login.html")
    else:
        if session['token'] == utils.sess:
            if (time.gmtime())[3] - (utils.logtime)[3] < 1 and (time.gmtime())[2] == (utils.logtime)[2] and (time.gmtime())[1] == (utils.logtime)[1] and (time.gmtime())[0] == (utils.logtime)[0]:
                return render_template("calender.html")
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.debug = True
    app.secret_key="david veller"
    app.run(host="0.0.0.0", port=8000)
