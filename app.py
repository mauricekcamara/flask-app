from flask import Flask, redirect
import os


from controllers.user_controller import user_controller
from controllers.session_controller import session_controller
from controllers.cheerup_controller import cheerup_controller


DB_URL = os.environ.get("DATABASE_URL", "dbname=project2")
SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return redirect('/cheerups')


# Register Controllers
app.register_blueprint(user_controller)
app.register_blueprint(session_controller)
app.register_blueprint(cheerup_controller)

if __name__ == "__main__":
    app.run(debug=True)
