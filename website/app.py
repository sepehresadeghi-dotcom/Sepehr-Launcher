from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def aboutus():
    return render_template("about.html", pn="rezaaaa")


@app.route("/contact")
def contactus():
    return render_template("contact.html")


@app.route("/blog")
def showBlog():
    return render_template("blog.html")


@app.route("/game")
def game():
    return render_template("game.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/game_assistant")
def game_assistant():
    return render_template("game_assistant.html")


if __name__ == "__main__":
    app.run(debug=True)