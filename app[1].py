from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Dummy login logic
        pin = request.form.get('pin')
        if pin == '1234':
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid PIN')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return '<h1>Welcome to DK Time Tracker Dashboard</h1>'

if __name__ == '__main__':
    app.run(debug=True)
