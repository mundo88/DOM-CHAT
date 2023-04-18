from flask import Flask

def create_app():
    app = Flask(__name__)

    create_bluePrint(app=app)

    return app 

def create_bluePrint(app):
    from .auth.views import auth
    from .home.views import home
    app.register_blueprint(home)
    app.register_blueprint(auth,url_prefix='/authentication')
