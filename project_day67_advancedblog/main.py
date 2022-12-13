from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime


def receive_data(form, post = None):
  if post:
    post.title = form.title.data,
    post.subtitle = form.subtitle.data,
    post.body = form.body.data,
    post.author = form.author.data,
    post.img_url = form.img_url.data
  else:
    post = BlogPost(
      title = form.title.data,
      subtitle = form.subtitle.data,
      date = datetime.today().strftime("%B %d, %Y"),
      body = form.body.data,
      author = form.author.data,
      img_url = form.img_url.data
    )
  return post


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BlogPost(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(250), unique=True, nullable=False)
  subtitle = db.Column(db.String(250), nullable=False)
  date = db.Column(db.String(250), nullable=False)
  body = db.Column(db.Text, nullable=False)
  author = db.Column(db.String(250), nullable=False)
  img_url = db.Column(db.String(250), nullable=False)

class CreatePostForm(FlaskForm):
  title = StringField("Blog Post Title", validators=[DataRequired()])
  subtitle = StringField("Subtitle", validators=[DataRequired()])
  author = StringField("Your Name", validators=[DataRequired()])
  img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
  body = CKEditorField("Blog Content", validators=[DataRequired()])
  submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
  posts = BlogPost.query.all()
  return render_template('index.html', all_posts=posts)

@app.route('/post/<int:id>')
def show_post(id):
  requested_post = BlogPost.query.get(id)
  return render_template('post.html', post=requested_post)

@app.route('/new-post', methods=['GET','POST'])
def new_post():
  form = CreatePostForm()
  if form.validate_on_submit():
    post = receive_data(form)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))
  return render_template('make-post.html', form=form, action='New')

@app.route('/edit-post/<post_id>', methods=['GET','POST'])
def edit_post(post_id):
  post = BlogPost.query.get(post_id)
  form = CreatePostForm(
    title = post.title,
    subtitle = post.subtitle,
    author = post.author,
    body = post.body
  )
  if form.validate_on_submit():
    post = receive_data(form, post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))
  return render_template('make-post.html', form=form, action='Edit')

@app.route('/delete/<id>')
def delete_post(id):
  post = BlogPost.query.get(id)
  db.session.delete(post)
  db.session.commit()
  return redirect(url_for('get_all_posts'))

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

if __name__ == '__main__':
  app.run(debug=True)
