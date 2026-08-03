import os
from flask import Blueprint, request, flash
from flaskr.config import Config
from werkzeug.utils import secure_filename

files_bp =Blueprint("files", __name__, url_prefix="/api/files")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENTIONS

@files_bp.post("")
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
    file = request.files['file']
    print(file.filename)
    if file.filename == '':
        flash('no seletected file')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
        return 'OK'