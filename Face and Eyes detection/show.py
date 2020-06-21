import os
from flask import Flask, request, render_template,redirect,url_for
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = "C:\\Users\\MEDA\\Desktop\\Face and Eyes detection\\uploads"

app = Flask(__name__,)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    

@app.route('/upload',methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        if request.files:
            file = request.files['fileName']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('click.html') 

if __name__ == '__main__':
    app.run(debug = False)
