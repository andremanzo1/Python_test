from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)
# route decorator binds a function to a URL
@app.route('/')
def hello():
  return '<p>Ryan W: Lmao, Mark G: lol </p>'


@app.route('/Andre')
def acronym():
    return render_template('template.html')



# Link to repository: 