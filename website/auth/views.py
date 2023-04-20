from flask import Blueprint,render_template,redirect,request,url_for
from flask_login import login_user,logout_user
from ..models import User
from ..app import db
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
from requests_oauthlib import OAuth2Session
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


FB_CLIENT_ID = "571757634883766"
FB_CLIENT_SECRET = "0572d6da0c6dfdb1908e8491129b67ec"

FB_AUTHORIZATION_BASE_URL = "https://www.facebook.com/dialog/oauth"
FB_TOKEN_URL = "https://graph.facebook.com/oauth/access_token"

FB_SCOPE = ["email"]
BASE_URL="https://bb03-2405-4802-1c6a-9840-e4b3-f4a5-195b-eb3f.ngrok-free.app"
auth =  Blueprint('auth', __name__,    
    template_folder="templates",
    static_folder='static',
    static_url_path='/auth/static')

@auth.route('/sign-in',methods=['POST','GET'])
def signinView():
    if request.method == 'POST' :
        data = request.form
        email = data.get('email')
        password = data.get('password')
        remember = data.get('remember')
        user = User.query.filter_by(email=email).first()
        if user.password==password:
            login_user(user,remember=remember)
            return redirect(url_for("home.homeView"))
    return render_template('signin.html')

@auth.route('/sign-up',methods=['POST','GET'])
def signupView():
    return render_template('signup.html')

@auth.route('/logout',methods=['POST','GET'])
def logout():
    logout_user()
    return  redirect(url_for("home.homeView"))



@auth.route("/fb-login")
def facebookLogin():
    facebook = OAuth2Session(
        FB_CLIENT_ID, redirect_uri=BASE_URL + "/authentication/fb-callback", scope=FB_SCOPE
    )
    authorization_url, _ = facebook.authorization_url(FB_AUTHORIZATION_BASE_URL)
    print(authorization_url)
    return redirect(authorization_url)

@auth.route("/fb-callback")
def fbCallback():
    facebook = OAuth2Session(
        FB_CLIENT_ID, scope=FB_SCOPE, redirect_uri=BASE_URL + "/authentication/fb-callback"
    )

    facebook = facebook_compliance_fix(facebook)

    facebook.fetch_token(
        FB_TOKEN_URL,
        client_secret=FB_CLIENT_SECRET,
        authorization_response=request.url,
    )
    facebook_user_data = facebook.get(
        "https://graph.facebook.com/v16.0/me?fields=id,name,email,picture.type(large)"
    ).json()


    print(facebook_user_data)
    # user = User.query.filter_by(email=email).first()
    # if not user:
    #     user = User(email=email,username=username,photo_picture=photo_picture)
    #     db.session.add(user)
    #     db.session.commit()
    return redirect(url_for("home.homeView"))
