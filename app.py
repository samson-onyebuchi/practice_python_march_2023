from flask import Flask 
from config import Config
from posts.blueprint import posts

app = Flask(__name__)
app.config.from_object(Config)


#localhost:5000/blog
app.register_blueprint(posts, url_prefix = '/activities')