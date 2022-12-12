import requests

class Post:
  def __init__(self, json):
    self.id = json['id']
    self.title = json['title']
    self.subtitle = json['subtitle']
    self.body = json['body']
