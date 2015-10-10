from flask import Flask, render_template, request, session
import utils

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    uname = request.form['username']
    pword = request.form['password']
    if util.authenticate(uname, pword):
      session['loggedin'] = True
      return redirect(url_for('calender'))

  return render_template("login.html")

@app.route("/logout")
def logout():
  return render_template("logout.html")


@app.route("/calendar")
def calendar():
  if verify():
      days = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}
      month="January"
      firstday="2"
      return render_template("calendar.html",calendar=utils.calendar(month,firstday,days[month]))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
