from flask import Flask, render_template, request, session
import utils

app = Flask(__name__)

def verify(): return True;
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


@app.route("/calendar")
def calendar():
  if verify():
      days="Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
      months = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}
      month="October"
      firstday=2
      return render_template("calendar.html",month=month,days=days, firstday=firstday, numdays=months[month])


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
