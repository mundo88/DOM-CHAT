from flask import Flask,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate

db = SQLAlchemy(session_options={"autoflush": False})
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    create_db(app)
    create_bluePrint(app)
    setupLogin(app)
    migrate.init_app(app, db,render_as_batch=True)
    return app 

def create_db(app):
    from .models import User
    db.init_app(app)
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(email="dom@admin").first(): 
            username = "Dom Studio"
            email = "dom@admin"
            password = "123123"
            photo_picture = "https://i.imgur.com/w8zwbi7.png"
            is_admin = True
            admin = User(username=username, email=email, password=password, photo_picture=photo_picture, is_admin=is_admin)
            db.session.add(admin)
            db.session.commit()
def create_bluePrint(app):
    from .auth.views import auth
    from .home.views import home
    from .dashboard.views import dashboard
    from .chat.views import chat
    from .products.views import products
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(products,url_prefix='/products')
    app.register_blueprint(chat,url_prefix='/chat')
    app.register_blueprint(auth,url_prefix='/authentication')

def setupLogin(app):
    from flask_login import LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    @login_manager.unauthorized_handler     
    def unauthorized_callback():            
        return redirect(url_for('auth.signinView',next=request.url)) 
