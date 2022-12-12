import requests
from flask import Flask, render_template, request

BLOG_API_URL = 'https://api.npoint.io/c790b4d5cab58020d391'
posts = requests.get(BLOG_API_URL).json()
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html', blogs=posts)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  method = request.method
  form = request.form
  if method == 'GET':
    return render_template('contact.html', method='get')
  elif method == 'POST':
    with open('contacts.txt', 'a') as f:
      contact = dict(form)
      f.write(f"{contact}\n")
    return render_template('contact.html', method='post')

@app.route('/post/<id>')
def post(id):
  post = posts[int(id)-1]
  return render_template('post.html', blog=post)


if __name__ == "__main__":
  app.run(debug=True)
