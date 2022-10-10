from flask import Flask, request, jsonify, render_template
import config

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template('templates/index.html')

@app.route("/create_article")
def create_article():
    return render_template('templates/authoring_form.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)