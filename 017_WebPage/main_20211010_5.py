# python.py
#   - templates
#      - index.html
#   - static
#      - images
#         - background.png
#      - css
#         - index.css


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/<name>")
def name(name):
    return f"Hello, {name}!"

@app.route("/page")
def page():
    return render_template("WebPage.html")


app.run()