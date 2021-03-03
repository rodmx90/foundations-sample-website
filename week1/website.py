from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page_title="About")


@app.route('/learning')
def first_page():
    return render_template('learning.html', page_title="Learning")


@app.route('/community')
def second_page():
    return render_template('community.html', page_title="Community")

@app.route('/diversity')
def third_page():
    return render_template('diversity.html', page_title="Diversity")

@app.route('/contact')
def fourth_page():
    return render_template('contact.html', page_title="Contact")

# add additonal pages here using a similar format as above


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
