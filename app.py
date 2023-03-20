from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)


app.config['SECRET_KEY'] = 'My flask application secret key'
#create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What is your name?",validators=[DataRequired()])
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

