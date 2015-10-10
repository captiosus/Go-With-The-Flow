from flask import Flask, render_template, request, session

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


@app.route("/calender")
def calender():
  if verify():
    return render_template("calender.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
