import os
from flask import Flask, redirect, url_for, session, request, render_template
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# GitHub OAuth endpoints
CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
AUTHORIZATION_BASE_URL = 'https://github.com/login/oauth/authorize'
TOKEN_URL = 'https://github.com/login/oauth/access_token'
USER_API_URL = 'https://api.github.com/user'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    github = OAuth2Session(CLIENT_ID)
    authorization_url, state = github.authorization_url(AUTHORIZATION_BASE_URL)
    session['oauth_state'] = state
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    github = OAuth2Session(CLIENT_ID, state=session.get('oauth_state'))
    token = github.fetch_token(
        TOKEN_URL,
        client_secret=CLIENT_SECRET,
        authorization_response=request.url
    )
    session['oauth_token'] = token
    user = github.get(USER_API_URL).json()
    session['username'] = user.get('login')
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('home'))
    return render_template("dashboard.html", username=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=8000)
