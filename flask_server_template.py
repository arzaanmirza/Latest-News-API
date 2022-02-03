from flask import Flask
import json
import os


app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_news():
  pass


if __name__ == "__main__":
    app.run(debug=True)
