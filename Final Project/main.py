from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

# default-page


@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/register.html")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run()
