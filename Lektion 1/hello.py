# Kontrollera version av flask:
# py -c "import flask; print(flask.__version__)"'

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello World!</h1><p>Detta är staging-</p>"

app.run()
