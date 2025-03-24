from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from users import get_user  

app = Flask(__name__)
app.secret_key = 'clave_secreta'  

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  

@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id) 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = get_user(username)  

        if user and password == '1234':  
            login_user(user)
            return render_template('dashboard.html', user=user)
        
        return "Credenciales incorrectas"

    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)