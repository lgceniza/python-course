from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

ADMIN_EMAIL = 'admin@email.com'
ADMIN_PW = '12345678'

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[validators.DataRequired(), validators.Email()])
  password = PasswordField('Password', validators=[validators.DataRequired(), validators.Length(8)])
  submit = SubmitField('Login')


app = Flask(__name__)
app.secret_key = 'thisisasecret'


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == ADMIN_EMAIL and form.password.data == ADMIN_PW:
      return render_template('success.html')
    else:
      return render_template('denied.html')
  return render_template('login.html', form=form)

if __name__ == '__main__':
  app.run(debug=True)
