from flask import Flask


app = Flask(__name__)




if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(debug=True)