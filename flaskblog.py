from flask import Flask, render_template, url_for, flash, redirect
from flask import jsonify, request
from werkzeug.wrappers import request
from wtforms.validators import ValidationError
from forms import LoginForm, RegestrationForm

import uuid

"""app = 
Flask app web page following this tutorial
# https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH 
cmmands used to open server in debug mode
flask run to start server connection,
app.run(debug=True)
# This runs the Flask app in debug mode, which is a replacement for previous 2 commands
# You can now simply use 'python filename.py' to start the server

"""

app = Flask(__name__)

app.config['SECRET_KEY'] = 'h5vmpbrhoxkv1dgjoc8ebhmhzfxhcbml'
# Generate a UUID globally
cached_id = str(uuid.uuid4())
posts = [{
    'auther': 'reham shipl',
    'title': 'blog post 1',
    'content': 'first post content',
    'date_posted': 'April 30, 2018'
}, {
    'auther': 'farida mohamed',
    'title': 'farida the best 2',
    'content': 'second post content',
    'date_posted': 'june 30, 2018'
}]


@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html', posts=posts)


@app.route("/about")
def about():
  return render_template('about.html', title='about')





@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegestrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='register', form=form, cached_id=cached_id)

'''@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegestrationForm()
  if request.method == 'POST':
    if form.validate_on_submit():
      flash(f'Account created for {form.username.data}!', 'success')
      return redirect(url_for('home'))
    else:
      errors = form.errors
      return jsonify(errors), 400
  return render_template('register.html', title='register', form=form)
'''

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  print(form)
  if form.validate_on_submit():
    print(form)
    if form.email.data == 'i12@gmail.com' and form.password.data == 'pAssword123':
      flash('You have been logged in!', 'success')
      print("Login successful. valid email and password")

      return redirect(url_for('home'))
    else:
      flash('Login Unsuccessful. Please check email and password', 'danger')
      print("Login Unsuccessful. Please check email and password")
  return render_template('login.html', title='login', form=form)


if __name__ == "__main__":
  app.run(debug=True)
