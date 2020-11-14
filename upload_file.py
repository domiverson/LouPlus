from flask import Flask, request
import os
from werkzeug.utils import secure_filename # 获取上传文件名

UPLOAD_FOLDER = '/home/shiyanlou/Code'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return '{} upload successed!'.format(filename)
    return '''<!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p>
    <input type=file name=file>
    <input type=submit value=Upload>
    </p>
    </form>'''