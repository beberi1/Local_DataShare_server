from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        files = request.files.getlist('files')  # Get the list of files
        if not files:
            return 'No files selected'
        
        for file in files:
            if file.filename == '':
                return 'No selected file'
            # Save the file
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'Files uploaded successfully'
    return '''
    <!doctype html>
    <title>Upload Files</title>
    <h1>Upload Multiple Files</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=files multiple>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# host ში ჩაწერე შენი აიპი პორტში სასურველი პორტი
# მაგალითად 192.168.9.9:6969 და შედი
