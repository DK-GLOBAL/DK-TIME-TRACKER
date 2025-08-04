 from flask import render_template, session, redirect
import traceback

@app.route('/dashboard')
def dashboard():
    try:
        user = session.get('user')
        if not user:
            return redirect('/login')

        # Make sure user has keys: name, role, login_time
        safe_user = {
            "name": user.get("name", "User"),
            "role": user.get("role", "N/A"),
            "login_time": user.get("login_time", "Unknown")
        }

        return render_template('dashboard.html', user=safe_user)

    except Exception as e:
        traceback.print_exc()
        return "Internal Server Error: " + str(e), 500
