from app import app
@app.route("/")
def index():
    return "Flask App -_-\n"