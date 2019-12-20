from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "82f1d96a3652b640747d5353f0f97eb6 "

posts = [
    {
        'author': 'Ermin Avdic',
        'title': 'Blog post one',
        'content': 'First blog post',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Ermin Avdic',
        'title': 'Blog post two',
        'content': 'Second blog post',
        'date_posted': 'April 20, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)