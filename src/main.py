from flask import Flask, render_template

app = Flask(__name__, template_folder="pages")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/train/<train_line>")
def train_schedule(train_line):
    return render_template("line.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
