from models import Document, db

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_to_db(filename, filepath):
    document = Document(filename=filename, filepath=filepath)

    db.session.add(document)
    db.session.commit()

    return str(document.id), document.filepath
