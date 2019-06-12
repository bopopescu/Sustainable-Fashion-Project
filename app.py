from flask import Flask, redirect, render_template
from flask_session.__init__ import Session
from tempfile import mkdtemp

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return redirect("/home")

@app.route("/home", methods=["GET", "POST"])
def home():
    """Sustainable, but make it fashion"""
    return render_template("home.html")

@app.route("/gartheaux", methods=["GET", "POST"])
def gartheaux():
    return render_template("gallery:artheaux.html")

@app.route("/partheaux", methods=["GET", "POST"])
def partheaux():
    return render_template("allpoststemplate.html")

@app.route("/gfancy", methods=["GET", "POST"])
def gfancy():
    return render_template("gallery:fancy.html")

@app.route("/pfancy", methods=["GET", "POST"])
def pfancy():
    return render_template("allpoststemplate.html")

@app.route("/grich", methods=["GET", "POST"])
def grich():
    return render_template("gallery:rich.html")

@app.route("/prich", methods=["GET", "POST"])
def prich():
    return render_template("allpoststemplate.html")

@app.route("/gangelbaby", methods=["GET", "POST"])
def gangelbaby():
    return render_template("gallery:angelbaby.html")

@app.route("/pangelbaby", methods=["GET", "POST"])
def pangelbaby():
    return render_template("allpoststemplate.html")
