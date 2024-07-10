from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '588f61dc98d89b26a8f700fad55462de'

posts = [{
    'author': 'Corey Schafer',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 20, 2018'
}, {
    'author': 'Jane Doe',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'April 21, 2018'
}]


@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', posts=posts)
  # return "<h1>Hello world</h1>"


@app.route('/about')
def about():
  # return "<h1>About Page</h1>"
  return render_template('about.html', title='about')


@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
      flash(
          f'You have been logged in successfully with email {form.email.data} !',
          'success')
      return redirect(url_for('home'))
    else:
      flash('Login Unsuccessful. Please check email and password', 'danger')
  return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
