import os
import logging
from flask import Flask, render_template

# set up flask and instrumentation
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=5000))
