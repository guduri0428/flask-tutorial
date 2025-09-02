import os
from flask import Flask

def create_app(test_config=None):

    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite')
    )

    if test_config is None:
        # Load the instance config, if it exists when not testing
        app.config.from_pyfile('config.py',silent=True)
    else:
        # Load the test config if it passed in
        app.config.from_mapping(test_config)
    
    try:
        # ensure the instance folder exists
        os.makedirs(app.instance_path)
    except OSError:
        pass
    

    # a simple page that shows hello
    @app.route("/hello")
    def hello():
        a = app.instance_path
        return "Hello World..!" + str(a)
    return app