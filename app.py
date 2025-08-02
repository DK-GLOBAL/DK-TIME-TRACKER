
from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    name = request.form['name']
    role = request.form['role']
    pin = request.form['pin']
    session['user'] = {'name': name, 'role': role, 'login_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
