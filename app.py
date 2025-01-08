from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():   
    return render_template('home.html')

@app.route("/about")
def about():   
    return render_template('about.html')

@app.route("/membership")
def membership():   
    return render_template('membership.html')

@app.route("/gallery")
def gallery():   
    return render_template('gallery.html')

@app.route("/contact")
def contact():   
    return render_template('contact.html')

@app.route("/login")
def login():   
    return render_template('login.html')

@app.route("/registeration")
def registeration():   
    return render_template('registeration.html')

if __name__ == "__main__":
    app.run(debug=True)


