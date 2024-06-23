from flask import Flask, jsonify, render_template
import data

app = Flask(__name__, template_folder="pages")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/train/<train_line>")
def train_schedule(train_line):
    return render_template("subway_line.html", train_line=train_line)


@app.route("/train/<train_line>/<stop>")
def train_stops(train_line, stop):
    return render_template("stop.html", train_line=train_line, stop=stop)


# Api endpoint
@app.route("/get_data/<subway_line>")
def get_data(subway_line):
    return jsonify(data.data(subway_line))


# for later
# @app.route("/bus/<bus_line>")
# def bus_schedule(bus_line):r
#     return render_template("bus_line.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
