import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
paths = []
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload',methods=['GET','POST'])
def upload_file():
    global paths
    if request.method == 'POST' and 'File' in request.files:
        for f in request.files.getlist('File'):
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                # print(filename)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                path = "./uploads/{}".format(filename)
                print(path)
                paths.append(path)
        detection_type = request.form['options']
        if detection_type == "Computer":
            pass
            #images = function(computer, paths[0], paths[0])
        else:
            pass
            #images = function(computer, paths[0], paths[1])
    print(os.path.join(basedir, paths[0].split('/', 2)[1]+ "\\" + paths[0].split('/', 2)[2]))
    print(paths[1])
    return render_template('index.html', returned1=str(os.path.join(basedir, paths[0].split('/', 2)[1] + "\\" + paths[0].split('/', 2)[2])), returned2=str(paths[1]))

if __name__ == '__main__':
    app.run(debug=True)