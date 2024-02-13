from flask import Flask, render_template

app = Flask(__name__, template_folder="pages")


@app.route("/")
def home():
    return render_template("index.html")


# Define a route that takes a parameter for the train line
@app.route("/train/<train_line>")
def train_schedule(train_line):
    # Here you can dynamically generate the schedule for the selected train line
    # For demonstration purposes, let's just return a simple message
    return render_template("line.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
