from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
from werkzeug.exceptions import HTTPException

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    def to_dict(self):  # This is a dictionary comprehension function created inside the Cafe class definition. It will be used to turn rows into a dictionary before sending it to jsonify.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.get('/random')
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })

@app.get('/all')
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.get('/search')
def get_search_cafe():
    location = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).filter_by(location=location.capitalize()))
    cafes = result.scalars().all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={"not found": "Sorry, no cafes here"})

# HTTP POST - Create Record
@app.post('/add')
def post_add_cafe():
    data = request.form
    name = str(data.get("name", "")).strip()
    map_url = str(data.get("map_url", "")).strip()
    if not name:
        return jsonify({"error": "no name"})
    if not map_url:
        return jsonify({"error": "map_url"})
    cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url='request.form.get("img_url")',
        location='sd',
        has_sockets=False,
        has_toilet=True,
        has_wifi=True,
        can_take_calls=False,
        seats=4,
        coffee_price=5,
    )
    db.session.add(cafe)
    db.session.commit()
    return "ok"

# HTTP PUT/PATCH - Update Record
@app.patch('/update-price/<cafe_id>')
def patch_update_price(cafe_id):
    print(request.form.get("new_price"))
    if not request.form.get("new_price"):
        return jsonify({"error": "no new_price"}), 400
    cafe = db.get_or_404(Cafe, cafe_id)
    cafe.coffee_price = request.form.get("new_price")
    db.session.commit()
    return cafe_id

# HTTP DELETE - Delete Record''''
@app.delete('/delete/<int:cafe_id>')
def delete_cafe(cafe_id):
    print(cafe_id)
    try:
        cafe = db.get_or_404(Cafe, cafe_id)
    except HTTPException:
        return jsonify({"error": "not found"}), 404
    else:
        db.session.delete(cafe)
        db.session.commit()
        return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
