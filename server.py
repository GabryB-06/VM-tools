from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_file():
   #return render_template('upload.html')
   return '''
<html>
   <body>
      <form action = "/uploader" method = "POST" 
         enctype = "multipart/form-data">
         <input type = "file" name="file"/>
         <input type = "submit"/>
      </form>
   </body>
</html>
'''
	
@app.route('/uploader', methods=['POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      
      if f:
         filename = secure_filename(f.filename)
         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
         f.save(file_path)
         return 'File uploaded successfully'+'<br><button onclick="history.back()">Go Back</button>'
         
   return 'No file uploaded'+'<br><button onclick="history.back()">Go Back</button>'

if __name__ == '__main__':
   app.run(debug=True)