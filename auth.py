from app import app


def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'profile' not in session:
      # Redirect to Login page here
      return redirect('/')
    return f(*args, **kwargs)

  return decorated

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/dashboard')
@requires_auth
def dashboard():
    return render_template('dashboard.html',
                          userinfo=session['profile'],
                          userinfo_pretty=json.dumps(session['jwt_payload'], indent=4))

# Here we're using the /callback route.
@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return redirect('/dashboard')

# /server.py

@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri='http://127.0.0.1:5000/callback')

@app.route('/logout')
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('home', _external=True), 'client_id': 'ZjMwTsC1ReuY5060zbDOSfmBgaCC6okg'}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))
    