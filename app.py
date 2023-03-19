from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/user/<name>")
def user(name):
    return render_template('user.html',user_name = name)


@app.route("/love/<l_name>")
def love_one(l_name):
    return render_template('love.html', l_name = l_name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_issue():
    return render_template('500.html'),500



if __name__ == "__main__":
    app.run(debug=True)

