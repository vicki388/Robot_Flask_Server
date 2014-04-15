from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/straight/')
@app.route('/straight/<x>')
def hello(name=None):
    return render_template('straight.html', x=x)

if __name__ == '__main__':
    app.run(debug=True)
