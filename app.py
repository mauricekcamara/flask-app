from flask import Flask, redirect, render_template
import os


from controllers.user_controller import user_controller


DB_URL = os.environ.get("DATABASE_URL", "dbname=project2")
SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template('signup.html')


# Register Controllers
app.register_blueprint(user_controller)

if __name__ == "__main__":
    app.run(debug=True)
