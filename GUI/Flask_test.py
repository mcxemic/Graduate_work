from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def index():
    return 'Lalalala'

@app.route('/option')
def interface():
    return render_template('option.html')

if __name__ == "__main__": ##run app
    app.run(debug=True) ##start server
