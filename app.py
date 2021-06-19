import os
import interface
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
paths = []
WORDS = []
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
            outputs = interface.detection_button("computer", paths[0], paths[0])
        else:
            print(paths[0])
            print(paths[1])
            outputs = interface.detection_button("handwritten", paths[1], paths[0])
        with open(outputs[1], "r") as file:
            for line in file.readlines():
                WORDS.append(line)
        print(WORDS)
        path = "./" + outputs[0]
        print(path)
    return render_template('index.html', returned1=WORDS, returned2=path)


@app.route('/code', methods=['GET', 'POST'])
def code():
        code_type = request.form['second_options']
        if code_type == "C++":
            outputs = interface.code_generation("cpp")
            header = []
            source = []
            with open(outputs[0], "r") as file:
                for line in file.readlines():
                    header.append(line)
            with open(outputs[1], "r") as file:
                for line in file.readlines():
                    source.append(line)
            return render_template('index.html', returned1=WORDS, returned4=header, returned5= source)
        else:
            outputs = interface.code_generation("python")
            source = []
            with open(outputs, "r") as file:
                for line in file.readlines():
                    source.append(line)
            return render_template('index.html', returned1=WORDS, returned6=source)




if __name__ == '__main__':
    app.run(debug=True)