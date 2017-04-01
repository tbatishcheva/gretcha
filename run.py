from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)
