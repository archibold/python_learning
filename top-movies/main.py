from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
Bootstrap5(app)

# CREATE DB

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    year: Mapped[int]
    description: Mapped[str]
    rating: Mapped[float]
    ranging: Mapped[int]
    review: Mapped[str]
    img_url: Mapped[str]

class RateBookForm(FlaskForm):
    ranging = StringField("Your rating")
    review = StringField("Your review")
    submit = SubmitField("Done")

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Books))
    all_books = result.scalars().all()
    return render_template("index.html", movies=all_books)

@app.route("/edit",methods=["GET", "POST"])
def edit():
    form = RateBookForm()
    id = request.args.get("id")
    book = db.get_or_404(Books, id)
    form.ranging.default = book.ranging
    form.review.default = book.review
    print(book.review)
    print(book.ranging)
    if form.validate_on_submit():
        print('---------')
        print(float(form.ranging.data))
        print(form.review.data)
        print('---------')
        book.ranging = float(form.ranging.data)
        book.review = form.review.data
        print(book.review)
        print(book.ranging)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=book, form=form)


if __name__ == '__main__':
    app.run(debug=True)
