from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  return "<h1>Hello world</h1>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

# set DEBUG = 1
# set FLASK_APP = app.py
# python app.py


 # from flaskblog import db
 # db.create_all()
# from flaskblog import User, Post
# user_1 = User(username='Corey', email="C@demo.com", password='password')
# db.session.add(user_1)
# user_2 = User(username='JohnDoe', email="jd@demo.com", password='password')
# db.session.add(user_2)
# db.session.commit()
# User.query.all()
# User.query.first()
# User.query.filter_by(username='Corey').all()
# User.query.filter_by(username='Corey').all().first()
# user = User.query.filter_by(username='Corey').all().first()
# user.id
# user = User.query.get(1)
# user.posts
# user.id
# post_1 = Post(title='Blog Post 1',content = "First Post content", user_id = user.id)
# post_2 = Post(title='Blog Post 2',content = "Second Post content", user_id = user.id)
# db.session.add(post_1)
# db.session.add(post_2)
# db.session.commit()
# user.posts
# for post in user.posts:
#   print(post.title)
# post = Post.query.first()
# post.user_id
# post.author
# db.drop_all()
# db.create_all()
# User.query.all()
# Post.query.all()




