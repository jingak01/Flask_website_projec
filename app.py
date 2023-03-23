from flask import Flask, render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#secrate key
app.config['SECRET_KEY'] = 'My flask application secret key'

#initializing DB
db= SQLAlchemy(app)


#create model
class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False, unique=True)
    date_added =db.Column(db.DateTime, default=datetime.now)

    #create a string

    def __repr__(self):
        return '<name %r>' % self.name

with app.app_context():
    db.create_all()

#create a Form Class
class NamerForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    # email = StringField('Email',validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/")
def Index():
    First_name = 'Akshay jingar'
    stuff = 'This is <strong>random stuff</strong> i created for website.'
    Fav_topping = ['Paneer','Chili','cheese','carrot','jelepino',41]

    return render_template('index.html', 
                            First_name = First_name,
                            stuff = stuff,
                            Fav_topping = Fav_topping
                            )



@app.route("/name",methods=['GET','POST'])
def name():
    name = None
    Form=NamerForm()

    #validate Form
    if Form.validate_on_submit():
        name = Form.name.data
        Form.name.data = ''
        flash('Form submitted sucessfully!....')

    return render_template('name.html',
                           name = name,
                           Form = Form)


@app.route("/user/<name>")
def user(name):
    return render_template('user.html',user_name = name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_error():
    return render_template('500.html'),500

#create a form class



if __name__ == "__main__":
    app.run(debug=True)

