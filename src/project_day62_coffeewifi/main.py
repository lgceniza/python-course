from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
  cafe = StringField('Cafe Name', validators=[DataRequired()])
  location = StringField('Location URL', validators=[DataRequired(), URL()])
  opening = StringField('Opening Time', validators=[DataRequired()])
  closing = StringField('Closing Time', validators=[DataRequired()])
  coffee = SelectField('Coffee Rating', validators=[DataRequired()], choices=['✘','☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️'])
  wifi = SelectField('Wifi Rating', validators=[DataRequired()], choices=['✘','💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪'])
  power = SelectField('Power Outlet Rating', validators=[DataRequired()], choices=['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌'])
  submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
  return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
  form = CafeForm()
  if form.validate_on_submit():
    with open('cafe-data.csv', 'a') as f:
      row = f"\n{form.cafe.data},{form.location.data},{form.opening.data},{form.closing.data},{form.coffee.data},{form.wifi.data},{form.power.data}"
      f.write(row)
    return redirect('cafes')
  return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
  with open('cafe-data.csv', newline='') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
      list_of_rows.append(row)
  return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
  app.run(debug=True)
