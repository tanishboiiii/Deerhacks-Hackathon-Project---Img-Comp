import os
from flask import Flask, request, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import shutil
from model import gagan

app = Flask(__name__)
# MODEL = model.Classifier()

@app.route('/')
def hello_flask():
   return render_template("index.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        os.rename(f.filename, "photo.jpg")
        gagan("photo.jpg")
        
        shutil.move("savedImage.jpg",
                    "static/images/savedImage.jpg")

        return render_template("display.html", name=f.filename)



if __name__ == '__main__':
   app.run(port = 8000,debug=True)