import requests
from flask import Flask, render_template
from post import Post

BLOG_API_URL = 'https://api.npoint.io/c790b4d5cab58020d391'
posts = [Post(blog) for blog in requests.get(BLOG_API_URL).json()]

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html", blogs=posts)

@app.route('/post/<id>')
def get_blog(id):
  post = posts[int(id)-1]
  return render_template("post.html", blog_title=post.title, post_body=post.body)

if __name__ == "__main__":
  app.run(debug=True)
