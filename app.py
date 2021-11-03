from flask import (render_template,
                    url_for, request)
from models import db, Pet, app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-pet', methods=['GET', 'POST'])
def add_pet():
    print(request.form)
    return render_template('addpet.html')


@app.route('/pet')
def pet():
    return render_template('pet.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')
