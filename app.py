import mysql.connector as mc
import os
import werkzeug

from dotenv import load_dotenv
from flask import Flask, render_template, url_for, request, redirect, flash

# Load env variables from `.env` file
load_dotenv()

# Initialize Flask App
app = Flask(__name__)

# Set the secret key
app.secret_key = os.getenv('SECRET_KEY')

# Setup MySQL database
db = mc.connect(
    host='localhost',
    user=os.getenv("MYSQL_USERNAME"),
    password=os.getenv("MYSQL_PASSWORD"),
    database="cs50_final"
)
curs = db.cursor(dictionary=True) # curs meaning Cursor
cursE = curs.execute # Just because Im too lazy to type `curs.execute` every single time you know

@app.route("/")
def index():
    banner_img = url_for('static', filename='images/banner.jpg')
    curs.execute("SELECT * FROM blogs ORDER BY pub_date DESC LIMIT 5")
    articles = curs.fetchall()
    return render_template("index.html", banner_img=banner_img, articles=articles, heading="Blog")

@app.route("/about")
@app.route("/archive")
def about():
    banner_img = url_for('static', filename="images/construction.jpg")
    return render_template("base.html", banner_img=banner_img, banner_full=True)

@app.route("/new-post", methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        draft = bool(request.form.get('draft'))
        
        flash('Post Drafted' if draft else 'Post Published')
        return redirect(url_for('.index'))
    banner_img = url_for('static', filename="images/banner.jpg")
    return render_template('new-post.html', banner_img=banner_img, heading="New Post")

@app.errorhandler(werkzeug.exceptions.HTTPException)
def page_not_found(e):
    banner_img = url_for('static', filename=f"images/{e.code}.png")
    return render_template("error.html", banner_img=banner_img, banner_full=True), e.code


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
    db.close()