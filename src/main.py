from flask import Flask, render_template

app = Flask(__name__, template_folder="pages")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/train/<train_line>")
def train_schedule(train_line):
    return render_template("subway_line.html", train_line=train_line)


# for later
@app.route("/bus/<bus_line>")
def bus_schedule(bus_line):
    return render_template("bus_line.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
