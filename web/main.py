import os
import logging
from flask import Flask, render_template
from lib.file import get_folder_contents, get_random_image

IMAGE_DIRECTORY = os.path.join(os.getcwd(), "static/img")

# set up flask and instrumentation
app = Flask(__name__)

@app.route("/")
def main():
    image = get_random_image(IMAGE_DIRECTORY)
    return render_template("index.html", image=image)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=5000))