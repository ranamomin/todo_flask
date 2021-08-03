from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')

# changing anything will reload the app automatically because of debug=True
app.run(debug=True)